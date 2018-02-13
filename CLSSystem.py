#!/usr/bin/env python

#-----------------------------------------------------------
# File name   : CLSystem.py
# Description : The script will get the UID from the RFID reader and temperature from DHT11 then save to the cls_system db
# Author      : Maria Mercid L. Sukati	
# E-mail      : mariamercidlangbid@gmail.com
# Date        : 1 Feb 2018
#-----------------------------------------------------------
import datetime
import time
import RPi.GPIO as GPIO
import Adafruit_DHT
import SimpleMFRC522

import LED
import DB_Helper

def main():
    
    rfid_reader = SimpleMFRC522.SimpleMFRC522()
    temp_sensor = Adafruit_DHT.DHT11
    temp_pin = 4 # Physical pin is 7
    dbh = DB_Helper.DB_Helper()

    try:
        print "Please place the tag to the RFID reader."
    	# Get the RFID
    	id, text = rfid_reader.read()
    	print "RFID: " + str(id)

    	# Turn ON LED to indicate that reading is successful
        LED.setup()
        LED.led()            
        
    	# Code for reading the DHT11 Humidity and Temperature Sensor
    	humidity, temperature = Adafruit_DHT.read_retry(temp_sensor, temp_pin)
    	print "Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity)

    	#Fetch the TagId from db.tbl_Tag base on RFID
        tagId = dbh.getTagId(id)  
    	#Insert the temperature and RFID to Data table
    	dbh.addEntry(tagId, temperature)
    	
    finally:
    	dbh.destroy()
    	cleanGPIO()

def cleanGPIO():
	GPIO.cleanup()        

if __name__ == "__main__": main()		