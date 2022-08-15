import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

in2 = 31
in1 = 33
in4 = 37
in3 = 35




# in1 is the brown wire, it is connect to GPIO6 which is pin 31
GPIO.setup(in1, GPIO.OUT)

# in2 is the red wire, it is connected to GPIO13 which is pin 33
GPIO.setup(in2, GPIO.OUT)

# in3 is the yellow wire, it is connected to GPIO19 which is pin 35
GPIO.setup(in3, GPIO.OUT)

# in4 is the orange wire, it is connected to GPIO26 which is pin 37
GPIO.setup(in4, GPIO.OUT)

# turning in1 on 
GPIO.output(in1, GPIO.HIGH)
time.sleep(2)
GPIO.output(in1, GPIO.LOW)
time.sleep(2)

# turning in2 on
GPIO.output(in2, GPIO.HIGH)
time.sleep(2)
GPIO.output(in2, GPIO.LOW)
time.sleep(2)

# turning in3 on
GPIO.output(in3, GPIO.HIGH)
time.sleep(2)
GPIO.output(in3, GPIO.LOW)
time.sleep(2)

# turning in4 on
GPIO.output(in4, GPIO.HIGH)
time.sleep(2)
GPIO.output(in4, GPIO.LOW)
time.sleep(2)

