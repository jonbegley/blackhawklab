import wmi, sqlite3, random, os.path, mysql.connector, time
dbconnection = sqlite3.connect('blackhawkDB.sql')
dbcursor = dbconnection.cursor()
c = wmi.WMI()
a = 0
b = 0
loop = 0
CONFIGcomputerUID = "NO_UID_FOUND"
MachineID = 0
idFromDatabaseInt = 0

### Server Config Variables ###
CONFIGupdate = 0
CONFIGserverIP = "NO IP FOUND"
CONFIGserverUsername = "NO DATABASE USERNAME FOUND"
CONFIGserverDBName = "NO DATABASE NAME FOUND"
CONFIGserverPassword = "NO DATABASE PASSWORD FOUND"
#################################


serverConfigFile = "serverconfig"
if os.path.isfile(serverConfigFile) == 1:
    print"****************************************************"
    print"*************** LOCAL SERVER EXSISTS ***************"
    print"****************************************************"
    with open("serverconfig") as serverConfigF:
        for line in serverConfigF:
            if "Server IP/DNS" in line:
                CONFIGserverIP = line
                CONFIGserverIP = CONFIGserverIP.replace("Server IP/DNS:", "")
                CONFIGserverIP = CONFIGserverIP.replace(" ", "")
                CONFIGserverIP = CONFIGserverIP.strip()
                print '\n \tServer IP Address -', CONFIGserverIP
    serverConfigF.close()

    with open("serverconfig") as serverConfigF:
        for line in serverConfigF:
            if "BHDB Database" in line:
                CONFIGserverDBName = line
                CONFIGserverDBName = CONFIGserverDBName.replace("BHDB Database:", "")
                CONFIGserverDBName = CONFIGserverDBName.replace(" ", "")
                CONFIGserverDBName = CONFIGserverDBName.strip()
                print ' \tServer DB Connection Name -', CONFIGserverDBName
    serverConfigF.close()

    with open("serverconfig") as serverConfigF:
        for line in serverConfigF:
            if "Username" in line:
                CONFIGserverUsername = line
                CONFIGserverUsername = CONFIGserverUsername.replace("BHDB Username:", "")
                CONFIGserverUsername = CONFIGserverUsername.replace(" ", "")
                CONFIGserverUsername = CONFIGserverUsername.strip()
                print ' \tServer Username -', CONFIGserverUsername
    serverConfigF.close()

    with open("serverconfig") as serverConfigF:
        for line in serverConfigF:
            if "BHDB Password" in line:
                CONFIGserverPassword = line
                CONFIGserverPassword = CONFIGserverPassword.replace("BHDB Password:", "")
                CONFIGserverPassword = CONFIGserverPassword.replace(" ", "")
                CONFIGserverPassword = CONFIGserverPassword.strip()
                print ' \tServer Password - **************'
    serverConfigF.close()

    print'\n****************************************************\n'


if CONFIGserverIP == "NO IP FOUND":
    CONFIGupdate = CONFIGupdate + 1
    CONFIGserverIP = raw_input('\nServer Domain Name/IP Address: ')
    while b == 0:
        if ((raw_input("Server Domain/IP Address = \"" + CONFIGserverIP + "\" is this correct? (YES/NO)")).lower()) == "no":
            CONFIGserverIP = raw_input('\nRe-Enter - Server Domain Name/IP Address: ')
        else:
            b = b+1
b = 0
if CONFIGserverDBName == "NO DATABASE NAME FOUND":
    CONFIGupdate = CONFIGupdate + 1
    CONFIGserverDBName = raw_input('\nServer DB Name: ')
    while b == 0:
        if ((raw_input("Server Database Name = \"" + CONFIGserverDBName + "\" is this correct? (YES/NO)")).lower()) == "no":
            CONFIGserverIP = raw_input('\nRe-Enter - Server Database Name: ')
        else:
            b = b+1
b = 0
if CONFIGserverUsername == "NO DATABASE USERNAME FOUND":
    CONFIGupdate = CONFIGupdate + 1
    CONFIGserverUsername = raw_input('\nUsername: ')
    while b == 0:
        if ((raw_input("Username = \"" + CONFIGserverUsername + "\" is this correct? (YES/NO)")).lower()) == "no":
            CONFIGserverIP = raw_input('\nRe-Enter - Username: ')
        else:
            b = b+1
b = 0
if CONFIGserverPassword == "NO DATABASE PASSWORD FOUND":
    CONFIGupdate = CONFIGupdate + 1
    CONFIGserverPassword = raw_input('\nPassword: ')
    while b == 0:
        if ((raw_input("Password = \"" + CONFIGserverPassword + "\" is this correct? (YES/NO)")).lower()) == "no":
            CONFIGserverIP = raw_input('\nRe-Enter - Password: ')
        else:
            b = b+1

if CONFIGupdate > 0:
    print"****************************************************"
    print"*************** CONNECTION INFORMATION *************"
    print"****************************************************"
    print '\n \tServer IP Address -', CONFIGserverIP
    print ' \tServer DB Connection Name -', CONFIGserverDBName
    print ' \tServer Username -', CONFIGserverUsername
    print ' \tServer Password - **************'


### REMOTE DATABASE CONNECTION ###
REMOTEdbconnection = mysql.connector.connect(user=str(CONFIGserverUsername),
                                             password=str(CONFIGserverPassword),
                                             host=str(CONFIGserverIP),
                                             database=str(CONFIGserverDBName))
REMOTEdbcursor = REMOTEdbconnection.cursor()

### INITIALISE CONFIG FILE ###

configFileName = "config"
if os.path.isfile(configFileName) == 1:
    print"*************** CONFIG FILE EXSISTS ***************"
    with open("config") as f:
        for line in f:
            if "Computer UID:" in line:
                CONFIGcomputerUID = line

    print CONFIGcomputerUID
    CONFIGcomputerUID = CONFIGcomputerUID.replace("Computer UID:", "")
    CONFIGcomputerUID = CONFIGcomputerUID.replace(" ", "")
    CONFIGcomputerUID = CONFIGcomputerUID.strip()
    CONFIGcomputerUID = CONFIGcomputerUID.upper()

    CONFIGcomputerName = "HelloWorld"
    with open("config") as f:
        for line in f:
            if "Machine Name:" in line:
                CONFIGcomputerName = line

    print CONFIGcomputerName.strip()
    CONFIGcomputerName = CONFIGcomputerName.replace("Machine Name:", "")
    CONFIGcomputerName = CONFIGcomputerName.replace(" ", "")
    CONFIGcomputerName = CONFIGcomputerName.strip()
    CONFIGcomputerName = CONFIGcomputerName.upper()
    print"***************************************************"

    query = 'SELECT ID FROM machineInfo WHERE ComputerUID=\"%s\";' %CONFIGcomputerUID

    REMOTEdbcursor.execute(query)
    idFromDatabase = REMOTEdbcursor.fetchone()
    print idFromDatabase[0]
    idFromDatabaseInt = idFromDatabase[0]
    MachineID = idFromDatabaseInt

    #dbcursor.execute('SELECT * FROM machineInfo WHERE ComputerUID="'"(%s)"'";' %CONFIGcomputerUID)
    #dbcursor.execute('SELECT * FROM machineInfo WHERE ComputerUID="5CB13F0A3A27BFFDDE6F9498924FE50F";')
    #idFromDatabase = dbcursor.fetchone()
    #print idFromDatabase

    # if idFromDatabase == CONFIGcomputerName:
    #     print"****MATCH****"
    # else:
    #     print"FAIL"

else:
    configFile = open('config', 'w')
    configFile.write("*** PLEASE DO NOT MODIFY THIS FILE ***\n"
                     "\t  BlackhawkLAB Config File "
                     "\n\t   Developed by Jon Begley "
                     "\n\tStaffordshire Univeristy 2017\n"
                     "**************************************"
                     "\n\nMachine Name: \t\t")
    print "***************************************************"
    print "*************** CONFIG FILE CREATED ***************"
    print "***************************************************"

    ### GENERTATE COMPUTER HASH (COMPUTERUID) ###
    computerHashRAW = random.getrandbits(128)
    print(computerHashRAW)
    computerHash = ("%032x" % computerHashRAW)
    computerHash = computerHash.upper()
    print computerHash

    # -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+#

    # Populating Machine Infomation into BlackhawkDB #
    for machineInfo in c.Win32_ComputerSystem():
        REMOTEdbcursor.execute('INSERT INTO machineInfo (ComputerUID, DaylightinEffect, DNSHostName, '
                         'Domain, DomainRole, DaylightSavingsEnabled, Manufacturer,'
                         ' Model, ComputerName, NumberOfLogicalProcessors, NumberOfProcessors,'
                         ' PCSystemType, SystemType, UserName, WorkGroup, WakeUpType, PartOfDomain, LastUpdatedDate, LastUpdatedTime) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                         (computerHash, machineInfo.DaylightinEffect, machineInfo.DNSHostName, machineInfo.Domain, machineInfo.DomainRole, machineInfo.EnableDaylightSavingsTime,
                          machineInfo.Manufacturer, machineInfo.Model, machineInfo.Name, machineInfo.NumberOfLogicalProcessors,
                          machineInfo.NumberOfProcessors, machineInfo.PCSystemType, machineInfo.SystemType, machineInfo.UserName,
                          machineInfo.WorkGroup, machineInfo.WakeUpType, machineInfo.PartOfDomain, (str(time.strftime("%d/%m/%Y"))) , (str(time.strftime("%H:%M:%S")))))

    MachineID = REMOTEdbcursor.lastrowid
    print ('MachineID from DB', MachineID)

    configFile.write(machineInfo.Name)
    configFile.write("\nDomain: \t\t\t")
    configFile.write(machineInfo.Domain)
    configFile.write("\nManufacturer: \t\t")
    configFile.write(machineInfo.Manufacturer)
    configFile.write("\nModel: \t\t\t\t")
    configFile.write(machineInfo.Model)
    configFile.write("\nComputer UID: \t\t")
    configFile.write(computerHash)
    configFile.write("\nComputer DBID: \t\t")
    configFile.write(str(MachineID))
    configFile.close()

    REMOTEdbconnection.commit()

    print "Populate Machine Info - Complete"

    #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+#

#print MachineID

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+#



# Populate User Infomation into BlackhawkDB #
for userAccInfo in c.Win32_UserAccount():
    REMOTEdbcursor.execute('INSERT INTO userAccInfo (AccountType, Caption, Description, Disabled, DomainName, FullName, LocalAccount, Lockout, Name,'
                     ' PasswordChangeable, PasswordExpires, PasswordRequired, SID, SIDType, Status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                     (userAccInfo.AccountType, userAccInfo.Caption, userAccInfo.Description, userAccInfo.Disabled, userAccInfo.Domain, userAccInfo.FullName,
                      userAccInfo.LocalAccount, userAccInfo.Lockout, userAccInfo.Name, userAccInfo.PasswordChangeable, userAccInfo.PasswordExpires, userAccInfo.
                      PasswordRequired, userAccInfo.SID, userAccInfo.SIDType, userAccInfo.Status))
REMOTEdbconnection.commit()

print "Populate User Info - Complete"

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+#


#Insert Operating System Infomation Info #
for osInfo in c.Win32_OperatingSystem():
    REMOTEdbcursor.execute('INSERT INTO osInfo (BootDevice, BuildNumber, Caption, CodeSet, CountryCode, CSName, CurrentTimeZone, EncryptionLevel, '
                     'ForegroundApplicationBoost, FreePhysicalMemory, FreeSpaceInPagingFiles, FreeVirtualMemory, InstallDate, LastBootUpTime, '
                     'LocalDateTime, Locale, Manufacturer, MaxNumberOfProcesses, MaxProcessMemorySize, Name, NumberOfProcesses, NumberOfUsers, '
                     'OperatingSystemSKU, Organization, OSArchitecture, OSLanguage, OSProductSuite, OSType, PrimaryOS, ProductType, RegisteredUser, '
                     'SerialNumber, ServicePackMajorVersion, ServicePackMinorVersion, SystemDevice, SystemDirectory, SystemDrive, TotalVirtualMemorySize, '
                     'Version, WindowsDirectory) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                     (osInfo.BootDevice, osInfo.BuildNumber, osInfo.Caption, osInfo.CodeSet, osInfo.CountryCode, osInfo.CSName, osInfo.CurrentTimeZone,
                      osInfo.EncryptionLevel, osInfo.ForegroundApplicationBoost, osInfo.FreePhysicalMemory, osInfo.FreeSpaceInPagingFiles,
                      osInfo.FreeVirtualMemory, osInfo.InstallDate, osInfo.LastBootUpTime, osInfo.LocalDateTime, osInfo.Locale, osInfo.Manufacturer,
                      osInfo.MaxNumberOfProcesses, osInfo.MaxProcessMemorySize, osInfo.Name, osInfo.NumberOfProcesses, osInfo.NumberOfUsers, osInfo.OperatingSystemSKU,
                      osInfo.Organization, osInfo.OSArchitecture, osInfo.OSLanguage, osInfo.OSProductSuite, osInfo.OSType, osInfo.Primary, osInfo.ProductType,
                     osInfo.RegisteredUser, osInfo.SerialNumber, osInfo.ServicePackMajorVersion, osInfo.ServicePackMinorVersion, osInfo.SystemDevice, osInfo.SystemDirectory,
                     osInfo.SystemDrive, osInfo.TotalVirtualMemorySize, osInfo.Version, osInfo.WindowsDirectory))

    #print MachineID

REMOTEdbconnection.commit()

print "Populate OS Info - Complete"

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+#




    #Load Running Process Infomation into BlackHawkDB #
for processInfo in c.Win32_process():
        REMOTEdbcursor.execute('INSERT INTO processInfo (FKMachineID, ProcessID, ProcessName, ParentProcessID, CreationDate, ComandlineArg, ExecutablePath, InstallDate, Handle, HandleCount, Status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                         (MachineID, processInfo.processID, processInfo.Name, processInfo.ParentProcessID, processInfo.CreationDate, processInfo.CommandLine, processInfo.ExecutablePath, processInfo.InstallDate,
                          processInfo.Handle, processInfo.HandleCount, processInfo.Status))
        a = (a+1)
REMOTEdbconnection.commit()

print "Populate Process Info - Complete"


#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+#

# Populate Parent Process Name #
for process in c.Win32_process():
    REMOTEdbcursor.execute("""
       UPDATE processinfo
       SET ParentProcessName=%s
       WHERE ParentProcessID=%s
    """, (process.name, process.processID))
REMOTEdbconnection.commit()

print "Populate PPID Info - Complete"

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+#


# Populate Network Info #

for networkInfo in c.Win32_NetworkAdapterConfiguration():
        if networkInfo.IPEnabled == 1:
                REMOTEdbcursor.execute('INSERT INTO networkInfo (FKMachineID, DefaultIPGateway, Description, DHCPEnabled, DHCPLeaseExpires, DHCPLeaseObtained, DHCPServer, DNSDomain, IPAddress, IPSubnet, IPEnabled, MACAddress) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                    (MachineID, (str(networkInfo.DefaultIPGateway)), networkInfo.Description, networkInfo.DHCPEnabled, networkInfo.DHCPLeaseExpires, networkInfo.DHCPLeaseObtained, networkInfo.DHCPServer, (str(networkInfo.DNSDomain)), (str(networkInfo.IPAddress)), (str(networkInfo.IPSubnet)), networkInfo.IPEnabled, networkInfo.MACAddress))
REMOTEdbconnection.commit()

print "Populate Network Info - Complete"

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+#

print "*** COMPLETE ***"
#print MachineID

