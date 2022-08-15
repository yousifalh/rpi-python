import RPi.GPIO as GPIO
from atexit import register
from time import sleep, time
from math import pi
from threading import Lock, Thread

class robot():
    """This is the robot object"""
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        self.in1 = 31
        self.in2 = 33
        self.in3 = 37
        self.in4 = 35
        self.re = 38
        self.le = 40
        self.hz = 100
        self.motor1f = None
        self.motor1b = None
        self.motor2f = None
        self.motor2b = None
        self.rec = 0
        self.lec = 0
        self.lockR = Lock()
        self.lockL = Lock()
        self.printOnExit = True
        register(self.stop)
        if self.printOnExit == True:
            register(self.printing)
        

    def setMotors(self):
        """This sets the pins for motors and pwm"""
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        GPIO.setup(self.in3, GPIO.OUT)
        GPIO.setup(self.in4, GPIO.OUT)
        self.motor1f = GPIO.PWM(self.in1, self.hz)
        self.motor1b = GPIO.PWM(self.in2, self.hz)
        self.motor2f = GPIO.PWM(self.in3, self.hz)
        self.motor2b = GPIO.PWM(self.in4, self.hz)
    
    def setEncoders(self):
        """This sets the pins for encoders"""
        GPIO.setup(self.re, GPIO.IN)
        GPIO.setup(self.le, GPIO.IN)
    
    def changeMotorSpeed(motor, dutyCycle):
        """This sets the duty cycle of a specific motor"""
        motor.ChangeDutyCycle(dutyCycle)

    def moveFoward(self, dc):
        self.motor1f.GPIO.ChangeDutyCycle(dc)
        self.motor2f.GPIO.ChangeDutyCycle(dc)
    
    def stop(self):
        """This stops all the motors, used in atexit to stop motors running after hault"""
        self.motor1f.ChangeDutyCycle(0)
        self.motor1b.ChangeDutyCycle(0)
        self.motor2f.ChangeDutyCycle(0)
        self.motor2b.ChangeDutyCycle(0)

    
    def printing(self):
        """This prints all """
        print("final rec:", self.rec)
        print("final lec:", self.lec)
        right_distance = pi / 40 * self.rec * 6.5 # 6.5 cm wheel diameter (assume for both idc)
        left_distance = pi / 40 * self.lec * 6.5
        print("right motor distance travelled = ", right_distance," cm")
        print("left motor distance travelled = ", left_distance," cm")

    def rightEncoderThread(self):
        """This is the function for the thread to read input from encoder for the right encoder"""
        previousrec = GPIO.input(self.re)

        while True:
            sleep(0.001)
            self.lockR.acquire()
            rightinput = GPIO.input(self.re)
        
            # if the encoder changed, increment rec
            if rightinput != previousrec:
                self.rec+=1
                previousrec = rightinput
            
            self.lockR.release()

    def leftEncoderThread(self):
        """This is the function for the thread to read input from encoder for the left encoder"""
        previouslec = GPIO.input(self.le)
    
        while True:
            sleep(0.001)
            self.lockL.acquire()
            leftinput = GPIO.input(self.le)

            # if the encoder changed, increment lec
            if leftinput != previouslec:
                self.lec+=1
                previouslec = leftinput

            self.lockL.release()

    

    def startThreads(self):
        """This starts all the threads"""
        rightEncoderThread = Thread(target=self.rightEncoderThread)
        leftEncoderThread = Thread(target=self.leftEncoderThread)
        rightEncoderThread.start()
        leftEncoderThread.start()

