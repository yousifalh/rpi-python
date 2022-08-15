import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

in1,in2,in3,in4 = 31,33,35,37

#GPIO setups
GPIO.setup(in1, GPIO.OUT)
print("setting up pin ", in1)
GPIO.setup(in2, GPIO.OUT)
print("setting up pin ", in2)
GPIO.setup(in3, GPIO.OUT)
print("setting up pin ", in3)
GPIO.setup(in4, GPIO.OUT)
print("setting up pin ", in4)

#Defining movement functions
def moveFoward():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in4, GPIO.HIGH)

def moveBackward():
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in3, GPIO.HIGH)

def stop():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    

#Defining sensors
s1t = 11
s1e = 13

s2t = 16
s2e = 18

GPIO.setup(s1t, GPIO.OUT)
GPIO.setup(s2t, GPIO.OUT)
GPIO.setup(s1e, GPIO.IN)
GPIO.setup(s2e, GPIO.IN)
ps1 = 0
pe1 = 0
ps2 = 0
pe2 = 0

def distanceCal(ps,pe):
    pdur = pe - ps
    return round(pdur*17150, 1)

while True:
    GPIO.output(s1t, GPIO.LOW)
    

    #pulse for sensor 1
    GPIO.output(s1t, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(s1t, GPIO.LOW)
    while GPIO.input(s1e) == 0:
        ps1 = time.time()
    while GPIO.input(s1e) == 1:
        pe1 = time.time()
    
    time.sleep(0.05)

    GPIO.output(s2t, GPIO.LOW)

    #pulse for sensor2
    GPIO.output(s2t, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(s2t, GPIO.LOW)
    while GPIO.input(s2e) == 0:
        ps2 = time.time()
    while GPIO.input(s2e) == 1:
        pe2 = time.time()
    
    distance1 = distanceCal(ps1, pe1)
    distance2 = distanceCal(ps2, pe2)

    if (distance1 <= 10) and (distance1 >= 0):
        moveBackward()
    elif (distance1 < 500) and (distance1 > 10):
        moveFoward()
    if (distance2 <= 10) and (distance2 >= 0):
        moveBackward()
    elif (distance2 < 500) and (distance2 > 10):
        moveFoward()
    time.sleep(0.1)