import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
import atexit
atexit.register(GPIO.cleanup)

# pin for lower servo is 38, pin for upper servo is 40
up = 40
down = 38

GPIO.setup(up, GPIO.OUT)
GPIO.setup(down, GPIO.OUT)

# 2-12 % duty cycle can be read by a servo motor

def servo_soft_pwm(pin, angle, t):
    print(pin, angle, t)
    duty = ((angle/180) * 10) + 2
    for x in range(int(t/0.02)):
        #This whole process takes 0.1 seconds to complete
        #0.02s is the time period for one wavelength (ignoring rubbish soft inaccuracies)
        #servo is adjusted/checked once every 5 wavelengths (0.1 seconds)
        #on duty
        for y in pin:
            GPIO.output(y, GPIO.OUT)
        time.sleep(duty*0.02)
        
        
servo_soft_pwm([up, down], 180, 3)
servo_soft_pwm([up, down], 0, 3)
servo_soft_pwm([up, down], 90, 3)







