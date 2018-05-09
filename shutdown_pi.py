#!/bin/python
# Simple script for shutting down the raspberry Pi at the press of a button.
# by Inderpreet Singh
# https://www.hackster.io/glowascii/raspberry-pi-shutdown-restart-button-d5fd07

import RPi.GPIO as GPIO
import time
import os


BtnPin = 20    # Physical pin is 38

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
	
def Shutdown(channel):
    os.system("sudo shutdown -h now")
    
GPIO.add_event_detect(20, GPIO.FALLING, callback = Shutdown, bouncetime = 2000)

while 1:
    time.sleep(1)
        