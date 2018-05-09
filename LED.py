#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LEDPin = 26		#Physical pin 37

def setup():
	GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
	GPIO.setup(LEDPin, GPIO.OUT)
	GPIO.output(LEDPin, GPIO.HIGH)

def ledON():
	GPIO.output(LEDPin, GPIO.LOW)
	time.sleep(0.5)
	
def ledOFF():
	GPIO.output(LEDPin, GPIO.HIGH)
	time.sleep(0.5)

def destroy():
	GPIO.output(LEDPin, GPIO.HIGH)
	GPIO.cleanup()

def test():
	for n in range(0, 10):
		led()

if __name__ == '__main__':
	setup()
	try:
		test()
	except KeyboardInterrupt:
		destroy()

