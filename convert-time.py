import wmi, sqlite3

dbconnection = sqlite3.connect('blackhawkDB.sql')
dbcursor = dbconnection.cursor()

print wmi.to_time("20170202111721.000000+000")

sec = wmi.to_time("20170202111721.000000+000")[5]
mins = wmi.to_time("20170202111721.000000+000")[4]
hour = wmi.to_time("20170202111721.000000+000")[3]
day = wmi.to_time("20170202111721.000000+000")[2]
month = wmi.to_time("20170202111721.000000+000")[1]
year = wmi.to_time("20170202111721.000000+000")[0]

print("Time:")
print ("%d:%d"% (hour, mins))

print("Date:")
print("%d/%d/%d"% (day, month, year))

print("Time and Date:")
#print("%d:%d %d/%d/%d"% (hour, mins, day, month, year))

print("%d-%d-%d %d:%d:%d"% (year, month, day, hour, mins, sec))

print ("* * * * * * * * * * * * * * * * * * *")
print ("* * * * * * * * * * * * * * * * * * *")
print("Development Process:")
print("")
#printProcessInfo = dbcursor.execute('SELECT * FROM processInfo')
#print (printProcessInfo)

print("* * * * * * * * * * * * * * * * * * *")
print("* * * * * * * * * * * * * * * * * * *")


