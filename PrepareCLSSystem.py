#!/usr/bin/env python

#-----------------------------------------------------------
# File name   : PrepareCLSystem.py
# Description : The script will provide options to the user to add entries to cls_system db
# Author      : Maria Mercid L. Sukati	
# E-mail      : mariamercidlangbid@gmail.com
# Date        : 8 Feb 2018
#-----------------------------------------------------------
import RPi.GPIO as GPIO
import SimpleMFRC522

import DB_Helper

def main():
	rfid_reader = SimpleMFRC522.SimpleMFRC522()
	dbh = DB_Helper.DB_Helper()

	try:
            
		while True:
                
			print "Select from the following: \n"
			o = int(raw_input("[1] Register Tag  \n[2] Write To RFID  \n[3] Register Respondent  \n[4] Register Suburb  \n[5] Register State \nPress Any Number to stop... \n\nEnter Option: "))
			
			if o==1:						
				print "Tap the Tag to the RFID Reader to register the ID"
				id, text = rfid_reader.read()
				resp = int(raw_input("Enter RespondentId: "))
				subid = int(raw_input("Enter SuburbId: "))
				stateid = int(raw_input("Enter StateId: "))
				# Register the id to tbl_Tag		
				dbh.registerRFID(id, resp, subid, stateid)

			elif o==2:
				print "Tap the Tag to the RFID Reader to write the ID"
				id = raw_input("Enter the id in hex [Ex. FF FF FF FF FF]: ")
				rfid_reader.write(id)
				
			elif o==3:			
				fname = str(raw_input("Enter First Name: "))
				lname = str(raw_input("Enter Last Name: "))
				bdate = str(raw_input("Birthdate [yyyy-mm-dd]: "))
				# Register respondent details to tbl_Respondent
				dbh.registerName(fname, lname, bdate)
				
			elif o==4:			
				name = str(raw_input("Enter Suburb Name: "))
				# Add suburb name to tbl_Suburb
				dbh.addSuburb(name)
				
			elif o==5:			
				name = str(raw_input("Enter State Name: "))
				# Add state name to tbl_State
				dbh.addState(name)
				
			else:
				break
                    
	finally:
		dbh.destroy()
		GPIO.cleanup()

if __name__ == "__main__": main()		