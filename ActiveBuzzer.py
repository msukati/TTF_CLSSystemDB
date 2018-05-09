#!/usr/bin/env python

#-----------------------------------------------------------
# File name   : 02_activeBuzzer.py
# Description : make an active buzzer beep.
# Author      : Jason
# E-mail      : jason@adeept.com
# Website     : www.adeept.com
# Date        : 2015/06/12
#-----------------------------------------------------------

import RPi.GPIO as GPIO
import time

BeepPin = 18    # Physical pin is 12

def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)        
	GPIO.setup(BeepPin, GPIO.OUT)   # Set pin mode as output
	GPIO.output(BeepPin, GPIO.LOW) # Set pin to high(+3.3V) to off the beep

def beep():
    GPIO.output(BeepPin, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(BeepPin, GPIO.LOW)
	time.sleep(0.1)	    

def test():
	while True:
		GPIO.output(BeepPin, GPIO.LOW)
		time.sleep(0.5)
		GPIO.output(BeepPin, GPIO.HIGH)
		time.sleep(0.5)
		
def destroy():
	GPIO.output(BeepPin, GPIO.HIGH)    # beep off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	print 'Press Ctrl+C to end the program...'
	setup()
	try:
		test()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()



