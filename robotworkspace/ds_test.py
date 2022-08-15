import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# on robot, trigger is blue wire
s1t = 11
s1e = 13

s2t = 16
s2e = 18

# trigger pins must be output
# echo pins must be input 
GPIO.setup(s1t, GPIO.OUT)
GPIO.setup(s1e, GPIO.IN)

GPIO.setup(s2t, GPIO.OUT)
GPIO.setup(s2e, GPIO.IN)

for x in range(5):
    GPIO.output(s1t, GPIO.LOW)
    GPIO.output(s2t, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(s1t, GPIO.HIGH)
    GPIO.output(s2t, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(s1t, GPIO.LOW)
    GPIO.output(s2t, GPIO.LOW)
    pulse_start1=0
    pulse_start2=0
    pulse_end1=0
    pulse_end2=0
    while GPIO.input(s1e) == 0:
        pulse_start1 = time.time()
    while (GPIO.input(s2e)) == 0:
        pulse_start2 = time.time()
    while GPIO.input(s1e) == 1:
        pulse_end1 = time.time()
    while GPIO.input(s2e) == 1:
        pulse_end2 = time.time()

    pulse1_duration = pulse_end1 - pulse_start1
    pulse2_duration = pulse_end2 - pulse_start2

    distance1 = pulse1_duration * 17150
    distance2 = pulse2_duration * 17150
    distance1 = round(distance1, 1)
    distance2 = round(distance2, 1)
    print("Sensor 1: ", distance1 ," cm Sensor 2: ", distance2 ," cm")
    time.sleep(3)



