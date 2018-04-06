import wmi, sqlite3, random, os.path, mysql.connector
dbconnection = sqlite3.connect('blackhawkDB.sql')
dbcursor = dbconnection.cursor()
c = wmi.WMI()
a = 0
loop = 0
CONFIGcomputerUID = "NO_UID_FOUND"
MachineID = 0
idFromDatabaseInt = 0



#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+#


# Populate Network Info #

for networkInfo in c.Win32_NetworkAdapterConfiguration():
        if networkInfo.IPEnabled == 1:
            a = str((networkInfo.DefaultIPGateway[0]))
            print a





        # if networkInfo.IPEnabled == 1:
        #         print(
        #             'INSERT INTO networkInfo (FKMachineID, DefaultIPGateway, Description, DHCPEnabled, DHCPLeaseExpires, DHCPLeaseObtained, DHCPServer, DNSDomain, IPAddress, IPSubnet, IPEnabled, MACAddress) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
        #             (MachineID, (str(networkInfo.DefaultIPGateway[0])), networkInfo.Description, networkInfo.DHCPEnabled, networkInfo.DHCPLeaseExpires, networkInfo.DHCPLeaseObtained, networkInfo.DHCPServer, (str(networkInfo.DNSDomain)), (str(networkInfo.IPAddress[0])), (str(networkInfo.IPSubnet[0])), networkInfo.IPEnabled, networkInfo.MACAddress)))

print "Populate Network Info - Complete"

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+#