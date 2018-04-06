import mysql.connector

REMOTEdbconnection = mysql.connector.connect(user='<USER>', password='<PASS>',
                              host='<IP-OR-DOMAIN>',
                              database='blackhawk_prod')


dbcursor = dbconnection.cursor()

var1 = "helloworld"
var2 = "HelloWorld"
var3 = "HelloWorld"


# dbcursor.execute("CREATE TABLE `machineInfo` (`ID`	INTEGER,"
#                  "`ComputerUID`	TEXT,`DaylightinEffect`	TEXT,`DNSHostName`	TEXT,`Domain`	TEXT,`DomainRole`	TEXT,`DaylightSavingsEnabled`	TEXT,`HypervisorPresent`	TEXT,`Manufacturer`	TEXT,`Model`	TEXT,`ComputerName`	TEXT,`NumberOfLogicalProcessors`	TEXT,`NumberOfProcessors` TEXT,`TotalPhysicalMemory`	INTEGER,`PCSystemType`	TEXT,`SystemType`	TEXT,`UserName`	TEXT,`WorkGroup`	TEXT,`WakeUpType`	TEXT,`PartOfDomain`	TEXT,PRIMARY KEY(`ID`));")
# dbcursor.close()
# dbconnection.close()

# dbcursor.execute("CREATE TABLE `testTable2` (`ID`	INTEGER,"
#                  "`ComputerUID`	TEXT,`DaylightinEffect`	TEXT,`DNSHostName`	TEXT,`TotalPhysicalMemory`")
# dbcursor.close()
# dbconnection.close()


dbcursor.execute("INSERT INTO testtable1 (ComputerUID, DaylightinEffect, DNSHostName, TotalPhysicalMemory) VALUES ( %s, %s, %s, %s)", (var2, var3, var1, var1))
dbconnection.commit()

# bob = "Test1"
# dummyVar = "HelloWorld"
#
# loggit = """INSERT INTO testTable1 (logged_info, dummy) VALUES (%s, %s)"""
#
# dbcursor.execute(loggit, (bob, dummyVar))



# dbconnection = sqlite3.connect('blackhawkDB.sql')
#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
#                                                          #
# Simple script to connect to a remote mysql database      #
#                                                          #
#                                                          #
# Install MySQLdb package by running:                      #
#                                                          #
#                       pip install MySQL-python           #
#                                                          #
############################################################

#
# import MySQLdb as db
#
# HOST = "10.10.10.52"
# PORT = 3306
# USER = "jbegley"
# PASSWORD = "Passw0rd1!"
# DB = "blackhawk_test"
#
# try:
#     connection = db.Connection(host=HOST, port=PORT,
#                                user=USER, passwd=PASSWORD, db=DB)
#
#     dbhandler = connection.cursor()
#     dbhandler.execute("SELECT * from your_table")
#     result = dbhandler.fetchall()
#     for item in result:
#         print item
#
# except Exception as e:
#     print e
#
# finally:
#     connection.close()