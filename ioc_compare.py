import sqlite3, random, os.path, mysql.connector
dbconnection = sqlite3.connect('blackhawkDB.sql')
dbcursor = dbconnection.cursor()

### REMOTE DATABASE CONNECTION ###
REMOTEdbconnection = mysql.connector.connect(user='<USER>', password='<PASS>',
                              host='<IP-OR-DOMAIN>',
                              database='blackhawk_prod')
REMOTEdbcursor = REMOTEdbconnection.cursor()



REMOTEdbcursor.execute('SELECT * FROM ioctable')
helloWorld =  REMOTEdbcursor.fetchall()
#print helloWorld[1][2]

string123 = 'None'

for x in range(0, len(helloWorld)):
    for y in range(0,6):
        print helloWorld[x][y]
        if str(helloWorld[x][y]) == "None":
            #helloWorld[x][y] = "NONE"
            print "DAVE"


    print '--------------'






    # print helloWorld[x]

# print helloWorld[1][1]
# if helloWorld[1][1] == "None":
#     print "HELLOWORLD"




# REMOTEdbcursor.execute('SELECT COUNT(*) FROM processinfo;')
# numberOfRows = REMOTEdbcursor.fetchone()
# print numberOfRows[0]
#
# for x in range(0, numberOfRows[0]):
#     print "We're on time %d" % (x+1)
# # for networkInfo in c.Win32_NetworkAdapterConfiguration():
# #         if networkInfo.IPEnabled == 1:
# #                 REMOTEdbcursor.execute(
# #                     'INSERT INTO networkInfo (FKMachineID, DefaultIPGateway, Description, DHCPEnabled, DHCPLeaseExpires, DHCPLeaseObtained, DHCPServer, DNSDomain, IPAddress, IPSubnet, IPEnabled, MACAddress) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
# #                     (MachineID, (str(networkInfo.DefaultIPGateway[0])), networkInfo.Description, networkInfo.DHCPEnabled, networkInfo.DHCPLeaseExpires, networkInfo.DHCPLeaseObtained, networkInfo.DHCPServer, (str(networkInfo.DNSDomain)), (str(networkInfo.IPAddress[0])), (str(networkInfo.IPSubnet[0])), networkInfo.IPEnabled, networkInfo.MACAddress))
# # REMOTEdbconnection.commit()
# #
