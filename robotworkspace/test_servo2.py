import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

import atexit
atexit.register(GPIO.cleanup)



GPIO.setup(15, GPIO.OUT)


upperS = GPIO.PWM(15, 50)


upperS.start(2)

print("waiting for 2 seconds")
time.sleep(2)
print("start")

upperS.ChangeDutyCycle(7)


time.sleep(3)
