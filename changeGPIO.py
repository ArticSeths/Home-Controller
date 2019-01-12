#!/usr/bin/python
import sys
import RPi.GPIO as GPIO
from time import sleep

pin = int(sys.argv[1])
# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Set relay pins as output
GPIO.setup(pin, GPIO.OUT)

if GPIO.input(pin):
    GPIO.output(pin, GPIO.LOW)
    print 'low'
else:
    GPIO.output(pin, GPIO.HIGH)
    print 'high'

#GPIO.output(21, GPIO.HIGH)
# Sleep for 5 seconds
#sleep(5)
# Turn all relays OFF
#GPIO.output(21, GPIO.LOW)
#GPIO.cleanup()
