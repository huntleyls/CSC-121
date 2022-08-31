time = float(input("Input time in seconds: "))
if time >= 43200:
    ampm = "pm"
else:
    ampm = "am"
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
if hour > 12:
    hours = hour - 12
minutes = time // 60
time %= 60
seconds = time

print("The time is %d:%d:%d" % (hours, minutes, seconds,),ampm,)
