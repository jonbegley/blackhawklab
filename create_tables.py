import mysql.connector


REMOTEdbconnection = mysql.connector.connect(user='<USER>', password='<PASS>',
                              host='<IP-OR-DOMAIN>',
                              database='blackhawk_prod')

REMOTEdbcursor = REMOTEdbconnection.cursor()

REMOTEdbcursor.execute('CREATE TABLE `networkInfo` (`ID`	INTEGER,`FKMachineID`	TEXT,`DefaultIPGateway`	TEXT,`Description`	TEXT,`DHCPEnabled`	TEXT,`DHCPLeaseExpires`	TEXT,`DHCPLeaseObtained`	TEXT,`DHCPServer`	TEXT,`DNSDomain`	TEXT,`IPAddress`	TEXT,`IPSubnet`	TEXT,`IPEnabled`	TEXT,`MACAddress`	TEXT,PRIMARY KEY(`ID`));')

REMOTEdbcursor.execute('CREATE TABLE `osInfo` (`ID`	INTEGER,`FKmachineID`	INTEGER,`BootDevice`	TEXT,`BuildNumber`	TEXT,`Caption`	TEXT,`CodeSet`	TEXT,`CountryCode`	TEXT,`CSName`	TEXT,`CurrentTimeZone`	TEXT,`EncryptionLevel`	TEXT,`ForegroundApplicationBoost`	TEXT,`FreePhysicalMemory`	TEXT,`FreeSpaceInPagingFiles`	TEXT,`FreeVirtualMemory`	TEXT,`InstallDate`	TEXT,`LastBootUpTime`	TEXT,`LocalDateTime`	TEXT,`Locale`	TEXT,`Manufacturer`	TEXT,`MaxNumberOfProcesses`	TEXT,`MaxProcessMemorySize`	TEXT,`MUILanguages`	TEXT,`Name`	TEXT,`NumberOfProcesses`	TEXT,`NumberOfUsers`	TEXT,`OperatingSystemSKU`	TEXT,`Organization`	TEXT,`OSArchitecture`	TEXT,`OSLanguage`	TEXT,`OSProductSuite`	TEXT,`OSType`	TEXT,`PrimaryOS`	TEXT,`ProductType`	TEXT,`RegisteredUser`	TEXT,`SerialNumber`	TEXT,`ServicePackMajorVersion`	TEXT,`ServicePackMinorVersion`	TEXT,`SystemDevice`	TEXT,`SystemDirectory`	TEXT,`SystemDrive`	TEXT,`TotalVirtualMemorySize`	TEXT,`Version`	TEXT,`WindowsDirectory`	TEXT,PRIMARY KEY(`ID`));')

REMOTEdbcursor.execute('CREATE TABLE `processInfo` (`ID`	INTEGER,`FKMachineID`	INTEGER,`ProcessID`	INTEGER,`ProcessName`	TEXT,`ParentProcessID`	INTEGER,`ParentProcessName`	TEXT,`CreationDate`	TEXT,`ComandLineArg`	TEXT,`ExecutablePath`	TEXT,`InstallDate`	TEXT,`Handle`	TEXT,`HandleCount`	INTEGER,`Status`	TEXT,PRIMARY KEY(`ID`));')

REMOTEdbcursor.execute('CREATE TABLE `userAccInfo` (`ID`	INTEGER,`AccountType`	TEXT,`Caption`	TEXT,`Description`	TEXT,`Disabled`	TEXT,`DomainName`	TEXT,`FullName`	TEXT,`LocalAccount`	TEXT,`Lockout`	TEXT,`Name`	TEXT,`PasswordChangeable`	TEXT,`PasswordExpires`	TEXT,`PasswordRequired`	TEXT,`SID`	TEXT,`SIDType`	TEXT,`Status`	TEXT);')

REMOTEdbcursor.execute('CREATE TABLE `machineInfo` (`ID`	INTEGER,`ComputerUID`	TEXT,`DaylightinEffect`	TEXT,`DNSHostName`	TEXT,`Domain`	TEXT,`DomainRole`	TEXT,`DaylightSavingsEnabled`	TEXT,`HypervisorPresent`	TEXT,`Manufacturer`	TEXT,`Model`	TEXT,`ComputerName`	TEXT,`NumberOfLogicalProcessors`	TEXT,`NumberOfProcessors`	TEXT,`TotalPhysicalMemory`	INTEGER,`PCSystemType`	TEXT,`SystemType`	TEXT,`UserName`	TEXT,`WorkGroup`	TEXT,`WakeUpType`	TEXT,`PartOfDomain`	TEXT,PRIMARY KEY(`ID`));')

REMOTEdbcursor.execute('CREATE TABLE `iocTable` (`ID`	INTEGER,`FKMachineID`	INTEGER,`ProcessName`	INTEGER,`ParentProcessName`	TEXT,`ComandLineArg`	TEXT,`ExecutablePath` TEXT,PRIMARY KEY(`ID`));')


REMOTEdbconnection.commit()