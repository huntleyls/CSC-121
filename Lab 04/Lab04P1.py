fpg = float(input("Enter fasting plasma glucose level:  "))
if fpg <= 100:
    print ("This patient has healthy fpg level")
if fpg >= 101 and fpg <= 125:
    print("This patient has pre-diabetes")
if fpg >=126:
    print("This patient has diabetes")
again = input("Checking diabetes for another patient? [y/n]")
while again == 'y':
    fpg = float(input("Enter fasting plasma glucose level:  "))
    if fpg <= 100:
        print ("This patient has healthy fpg level")
    if fpg >= 101 and fpg <= 125:
        print("This patient has pre-diabetes")
    if fpg >=126:
        print("This patient has diabetes")
    again = input("Checking diabetes for another patient? [y/n]")
