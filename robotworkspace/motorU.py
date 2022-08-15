import RPi.GPIO as GPIO

# Analysis of code from coming back to this a year later:
# This was a dumb idea...

def setMotorPins(array_of_pins):
    for item in array_of_pins:
        GPIO.setup(array_of_pins[item], GPIO.OUT)

def setInputPins(array_of_pins):
    for item in array_of_pins:
        GPIO.setup(array_of_pins[item], GPIO.IN)




