import RPi.GPIO as GPIO
import atexit
import time
import logging
import math
import threading
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

in1 = 31
in2 = 33
in3 = 37
in4 = 35
re = 38
le = 40

GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

GPIO.setup(re, GPIO.IN)
GPIO.setup(le, GPIO.IN)

hz = 100
speed = 75

motor1f = GPIO.PWM(in1, hz)
motor1b = GPIO.PWM(in2, hz)
motor2f = GPIO.PWM(in3, hz)
motor2b = GPIO.PWM(in4, hz)

def changeMotorSpeed(motor, dutyCycle):
    motor.changeDutyCycle(dutyCycle)

def stop():
    motor1f.ChangeDutyCycle(0)
    motor1b.ChangeDutyCycle(0)
    motor2f.ChangeDutyCycle(0)
    motor2b.ChangeDutyCycle(0)

def printing():
    print("final rec:", rec)
    print("final lec:", lec)
    right_distance = math.pi / 40 * rec * 6.5 # 6.5 cm wheel diameter (assume for both idc)
    left_distance = math.pi / 40 * lec * 6.5
    print("right motor distance travelled = ", right_distance," cm")
    print("left motor distance travelled = ", left_distance," cm")

atexit.register(stop)

logger = logging.getLogger("PI_controller")
logging.basicConfig(level=logging.DEBUG)
rec = 0
lec = 0
atexit.register(printing)

lock1 = threading.Lock()
lock2 = threading.Lock()

def rightEncoder():
    global re, rec, lock1
    previousrec = GPIO.input(re)

    while True:
        time.sleep(0.001)
        lock1.acquire()
        rightinput = GPIO.input(re)
        
        # if the encoder changed, increment lec
        if rightinput != previousrec:
            rec+=1
            previousrec = rightinput
            
        lock1.release()

def leftEncoder():
    global le, lec, lock2
    previouslec = GPIO.input(le)
    
    while True:
        time.sleep(0.001)
        lock2.acquire()
        leftinput = GPIO.input(le)

        # if the encoder changed, increment lec
        if leftinput != previouslec:
            lec+=1
            previouslec = leftinput

        lock2.release()

def PIController():
    global speed, motor1f, motor2f, logger, speed


    # PID constants
    pK = 0.3
    iK = 0
    i_sum = 0
    dK = 0
    delta_error = 0
    x_distance_error = 0
    y_distance_error = 200 # this is the error from distance wanted to reach
    rxes = 0 # this is the recurring x distance error sum

    while True:
        time.sleep(0.01)
        global rec, lec, speed

        
        error = rec - lec # if positive, lec overshoot & vice versa


        

        delta_error = error - delta_error
        i_sum += error

        theta = math.pi/40 * error
        
        x_distance_error = 6.5*(1 - math.cos(theta))
        rxes += x_distance_error

        theta = abs(theta)
        x = math.cos(theta)
        if x == 1:
            theta_t = 0
        else:
            theta_t = math.atan(math.sin(theta) / x) * 180 / math.pi

        p = pK * error

        i = iK * i_sum

        d = dK * delta_error

        logger.debug(f"""error: {error} r_speed: {int(speed+p)} l_speed: {int(speed-p)} p: {int(p)}""")

        

        

        motor1f.ChangeDutyCycle(int(speed-p+d))
        motor2f.ChangeDutyCycle(int(speed+p+d))

        

        



#starting threads
rightThreadForMotor = threading.Thread(target=rightEncoder)
leftThreadForMotor = threading.Thread(target=leftEncoder)
reclecThread = threading.Thread(target=PIController, daemon=True)

leftThreadForMotor.start()
rightThreadForMotor.start()
reclecThread.start()



time.sleep(0.5)
motor1f.start(speed)
motor2f.start(speed)


