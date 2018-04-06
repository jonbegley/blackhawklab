import mysql.connector


REMOTEdbconnection = mysql.connector.connect(user='<USER>', password='<PASS>',
                              host='<IP-OR-DOMAIN>',
                              database='blackhawk_prod')

REMOTEdbcursor = REMOTEdbconnection.cursor()

REMOTEdbcursor.execute('DELETE FROM processinfo')
REMOTEdbcursor.execute('DELETE FROM machineinfo')
REMOTEdbcursor.execute('DELETE FROM networkinfo')
REMOTEdbcursor.execute('DELETE FROM osinfo')
REMOTEdbcursor.execute('DELETE FROM useraccinfo')
#REMOTEdbcursor.execute('CREATE TABLE `networkInfo` (`ID`	INTEGER,`FKMachineID`	TEXT,`DefaultIPGateway`	TEXT,`Description`	TEXT,`DHCPEnabled`	TEXT,`DHCPLeaseExpires`	TEXT,`DHCPLeaseObtained`	TEXT,`DHCPServer`	TEXT,`DNSDomain`	TEXT,`IPAddress`	TEXT,`IPSubnet`	TEXT,`IPEnabled`	TEXT,`MACAddress`	TEXT,PRIMARY KEY(`ID`));')

REMOTEdbconnection.commit()