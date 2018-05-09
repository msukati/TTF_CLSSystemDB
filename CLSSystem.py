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
import ActiveBuzzer
import DB_Helper

time.sleep(15)              #This will let the script be prepared to run during startup

def init():
    LED.setup()
    ActiveBuzzer.setup()

def main():
    
    rfid_reader = SimpleMFRC522.SimpleMFRC522()
    temp_sensor = Adafruit_DHT.DHT11
    temp_pin = 4 # Physical pin is 7
    init()  #initialize the GPIO pins
    dbh = DB_Helper.DB_Helper()

    try:
	while True:
            print "Please place the tag to the RFID reader."

            # Turn ON LED to indicate that RFID is ready for reading        
            LED.ledON()  

            # Get the RFID
            id, text = rfid_reader.read()
            print "RFID: " + str(id)      
            LED.ledOFF()
            
            # Code for reading the DHT11 Humidity and Temperature Sensor
            humidity, temperature = Adafruit_DHT.read_retry(temp_sensor, temp_pin)
            print "Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity)

            #Fetch the TagId from db.tbl_Tag base on RFID
            tagId = dbh.getTagId(id)  
            #Insert the temperature, humidity and RFID to Data table
            inserted = dbh.addEntry(tagId, temperature, humidity)
        
            # Turn ON the buzzer to indicate that data is sent to Database
            if inserted is True:                
                ActiveBuzzer.beep()
    	
    except KeyboardInterrupt:
	dbh.destroy()
    	LED.ledOFF()
    	cleanGPIO()

def cleanGPIO():
	GPIO.cleanup()        

if __name__ == "__main__": main()		
