
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#pins - trigger is blue wire
s1t = 11 
s1e = 13

s2t = 16
s2e = 18

# setting pins
GPIO.setup(s1t, GPIO.OUT)
GPIO.setup(s2t, GPIO.OUT)
GPIO.setup(s1e, GPIO.IN)
GPIO.setup(s2e, GPIO.IN)
ps1 = 0
pe1 = 0
ps2 = 0
pe2 = 0

print("started things")

def distanceCal(ps,pe):
    pdur = pe - ps
    return round(pdur*17150, 1)

for x in range(50):
    GPIO.output(s1t, GPIO.LOW)
    

    #pulse for sensor 1
    print("sending out pulse to 1")
    GPIO.output(s1t, GPIO.HIGH)
    time.sleep(0.00001)
    print("stopped pulse")
    GPIO.output(s1t, GPIO.LOW)
    while GPIO.input(s1e) == 0:
        ps1 = time.time()
        
    while GPIO.input(s1e) == 1:
        pe1 = time.time()
    
    time.sleep(0.05)

    GPIO.output(s2t, GPIO.LOW)

    #pulse for sensor2
    print("sending out pulse to 2")
    GPIO.output(s2t, GPIO.HIGH)
    time.sleep(0.00001)
    print("stopped pulse")
    GPIO.output(s2t, GPIO.LOW)
    while GPIO.input(s2e) == 0:
        ps2 = time.time()
        
    while GPIO.input(s2e) == 1:
        pe2 = time.time()
    
    distance1 = distanceCal(ps1, pe1)
    distance2 = distanceCal(ps2, pe2)
    if distance1 > 500:
        distance1 = "out of range"
    if distance2 > 500:
        distance2 = "out of range"

    print("Sensor 1: ", distance1 ," cm Sensor 2: ", distance2 ," cm")
    time.sleep(0.1)