#!/usr/bin/env python

#-----------------------------------------------------------
# File name   : DB_Helper.py
# Description : The script will provide functions for the CLSystem to manipulate the tables in cls_system db
# Author      : Maria Mercid L. Sukati	
# E-mail      : mariamercidlangbid@gmail.com
# Date        : 7 Feb 2018
#-----------------------------------------------------------
import MySQLdb

hostname = '35.201.4.193'
username = 'root'
password = 'clsP@$$0717'
database = 'cls_system'

class DB_Helper:

    def __init__(self):
        self.dbcon = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
        self.cursor = self.dbcon.cursor()

    def destroy(self):
        self.cursor.close();
        self.dbcon.close();
   
    # Get the TagId base on the RFID
    def getTagId(self, Rfid):
        print "Searching for the TagId..."
        query = "SELECT TagId FROM tbl_Tag WHERE Rfid=%s" % Rfid
        self.cursor.execute(query);
        data = self.cursor.fetchone()
        return data[0]

    # Add the RFID and temperature
    def addEntry(self, id, temp):
        print "Inserting the data..."
        query = "INSERT INTO tbl_Data (TagId, Temperature) VALUES (%s, %s)" % (id, temp)
        self.cursor.execute(query)
        self.dbcon.commit()

    # Add the TagId
    def registerRFID(self, id, resp, suburb, state):
        print "Inserting the Rfid..."
        query = "INSERT INTO tbl_Tag (Rfid, RespondentId, SuburbId, StateId) VALUES (%s, %s, %s, %s)" % (id, resp, suburb, state)
        self.cursor.execute(query)
        self.dbcon.commit()

    # Add the Register respondent details
    def registerName(self, fname, lname, bdate):
		print "Inserting respondent details..."        
		query = """INSERT INTO tbl_Respondent (FirstName, LastName, BirthDate) VALUES (%s, %s, %s)""" 
		self.cursor.execute(query,(fname, lname, bdate,))
		self.dbcon.commit()
        
    # Add a suburb name
    def addSuburb(self, name):
        print "Inserting suburb name..."
        query = """INSERT INTO tbl_Suburb (Name) VALUES (%s)"""
        self.cursor.execute(query, (name,))
        self.dbcon.commit()
        
    # Add a state name 
    def addState(self, name):
        print "Inserting state name..."
        query = """INSERT INTO tbl_State (Name) VALUES (%s)"""
        self.cursor.execute(query, (name,))
        self.dbcon.commit()        
        