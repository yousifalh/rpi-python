import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

in1 = 31
in2 = 33
in3 = 35
in4 = 37
GPIO.setup(in1, GPIO.OUT)
print("setting up pin ", in1)
GPIO.setup(in2, GPIO.OUT)
print("setting up pin ", in2)
GPIO.setup(in3, GPIO.OUT)
print("setting up pin ", in3)
GPIO.setup(in4, GPIO.OUT)
print("setting up pin ", in4)


def move_foward():
    print("moving foward")
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in3, GPIO.HIGH)
    time.sleep(2)
    print("stopping")
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)

def move_backward():
    print("moving backwards")
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in4, GPIO.HIGH)
    time.sleep(2)
    print("stopping")
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)

def move_fw_speed(inp):
    print("moving foward at ", inp, " duty cycle")
    GPIO.PWM(in1, inp)
    GPIO.PWM(in3, inp)
    time.sleep(2)
    

def move_bk_speed(inp):
    print("moving backward at ", inp, " duty cycle")
    GPIO.PWM(in2, inp)
    GPIO.PWM(in3, inp)
    time.sleep(2)
    
    



move_fw_speed(50)
time.sleep(1)
move_bk_speed(50)
