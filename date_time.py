import datetime
x = datetime.datetime.now()

# Formatting Date and Time
date = x.strftime("Todays Date: %Y-%m-%d")
time = x.strftime("Current Time: %H:%M:%S")

print(date)
print(time)