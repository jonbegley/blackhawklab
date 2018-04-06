import wmi, sqlite3, random, os.path, mysql.connector, getpass, base64, logging


dbconnection = sqlite3.connect('blackhawkDB.sql')
dbcursor = dbconnection.cursor()
c = wmi.WMI()
a = 0
b = 0
loop = 0

##########################################################

CONFIGupdate = 0
CONFIGserverIP = "NO IP FOUND"
CONFIGserverUsername = "NO DATABASE USERNAME FOUND"
CONFIGserverDBName = "NO DATABASE NAME FOUND"
CONFIGserverPassword = "NO DATABASE PASSWORD FOUND"




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
