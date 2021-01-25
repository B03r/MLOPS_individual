# Print date
import datetime
now = datetime.datetime.now()
print ("Current date: ")
print (now.strftime("%Y-%m-%d"))

# Feature 1 - print date and time
print ("Current date and time: ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
