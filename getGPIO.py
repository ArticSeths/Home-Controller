#!/usr/bin/python
import sys
import RPi.GPIO as GPIO

pin = int(sys.argv[1])

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(pin, GPIO.OUT)
print GPIO.input(pin)
