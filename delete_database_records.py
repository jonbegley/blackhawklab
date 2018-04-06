import sqlite3, os
dbconnection = sqlite3.connect('blackhawkDB.sql')
dbcursor = dbconnection.cursor()

dbcursor.execute('DELETE FROM networkInfo')
dbcursor.execute('DELETE FROM machineInfo')
dbcursor.execute('DELETE FROM osInfo')
dbcursor.execute('DELETE FROM processInfo')
dbcursor.execute('DELETE FROM userAccInfo')
dbconnection.commit()

inRemoveConfig = raw_input("Do you wish to remove config file? [Yes]:")

if inRemoveConfig == "":
    os.remove("config")
    print "Config File Removed"
else:
    print("Config not removed.")

print("\n* * * * * * COMPLETED * * * * * * *")