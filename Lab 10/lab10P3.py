time = input('enter time [hh:mm:ss]:')
colons = time.count(':')
if colons == 2:
    hours,minutes,seconds = time.split(":")
    intHours = int(hours)
    intMins = int(minutes)
    intSecs = int(seconds)
    if len(hours) < 2 :
        print("hours must be a 2 digit number")
    elif len(minutes) < 2 :
         print("minutes must be a 2 digit number")
    elif len(seconds) < 2 :
        print("seconds must be a 2 digit number")
    elif intHours < 0 or intHours >23:
        print("Hour must be a 2-digit number between 0 and 23.")
    elif intMins < 0 or intMins >59:
        print("minutes must be a 2-digit number between 0 and 23.")
    elif intSecs < 0 or intSecs >59:
        print("seconds must be a 2-digit number between 0 and 23.")
    else:
        print("time with colons removed:",hours,minutes,seconds)

else:
    print("Must separate hour, minute and second with colons.")

