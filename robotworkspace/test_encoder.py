import RPi.GPIO as GPIO
import atexit
import time
import logging
import math
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
logger = logging.getLogger("test_encoders")

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

def mf():
    GPIO.output(in1, True)
    GPIO.output(in3, True)
    GPIO.output(in2, False)
    GPIO.output(in4, False)

def mb():
    GPIO.output(in1, False)
    GPIO.output(in3, False)
    GPIO.output(in2, True)
    GPIO.output(in4, True)

def mr():
    GPIO.output(in1, True)
    GPIO.output(in3, False)
    GPIO.output(in2, False)
    GPIO.output(in4, False)

def ml():
    GPIO.output(in1, False)
    GPIO.output(in3, True)
    GPIO.output(in2, False)
    GPIO.output(in4, False)

def stop():
    GPIO.output(in1, False)
    GPIO.output(in3, False)
    GPIO.output(in2, False)
    GPIO.output(in4, False)

def printing():
    print("final rec:", rec)
    print("final lec:", lec)
    right_distance = math.pi / 40 * rec * 6.5 # 6.5 cm wheel diameter (assume for both idc)
    left_distance = math.pi / 40 * lec * 6.5
    print("right motor distance travelled = ", right_distance," cm")
    print("left motor distance travelled = ", left_distance," cm")

atexit.register(stop)

logging.basicConfig(level=logging.INFO)
rec = 0
lec = 0
atexit.register(printing)

#initial previous values to get the code starting
previousrec = GPIO.input(re)
previouslec = GPIO.input(le)

mf()

while True:
    time.sleep(0.01)
    rightinput = GPIO.input(re)
    leftinput = GPIO.input(le)

    if rightinput != previousrec:
        rec+=1
        previousrec = rightinput

    if leftinput != previouslec:
        lec+=1
        previouslec = leftinput


    

