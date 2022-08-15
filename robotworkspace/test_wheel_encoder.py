import RPi.GPIO as GPIO
import atexit
import time
import logging
import math
import threading
import socket
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

lockForAverage = threading.Lock()
lockForSending = threading.Lock()

#----------#
# time between full rotation
tbfr = []
average = 0


def rightEncoder():
    global re, rec, tbfr
    previousrec = GPIO.input(re)
    delta_t = time.time

    while True:
        time.sleep(0.001)
        rightinput = GPIO.input(re)
        
        # if the encoder changed, increment lec
        if rightinput != previousrec:
            rec+=1
            previousrec = rightinput

        if rec % 40 == 0:
            c = time.time - delta_t
            tbfr.append(int(c))
            delta_t = time.time

        for x in range(len(tbfr)):
            










    




rightThreadForMotor = threading.Thread(target=rightEncoder)

rightThreadForMotor.start()
