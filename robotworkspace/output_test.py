
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)



GPIO.setup(7, GPIO.OUT)

sleep(30)