userType = input("What type of customer are you? R: residential B: business\n")
userGallons = int(input("Please enter the ammount of water you have used in Gallons\n"))

if userType == 'R' and userGallons <= 6000:
    userTotal = userGallons * 0.005
else:
    userTotal = (6000 * 0.005) + (userGallons - 6000) * 0.007

if userType == 'B' or userGallons <= 8000:
    userTotal = userGallons * 0.006
else:
    userTotal = (8000 * 0.006) + (userGallons - 8000) * 0.008

userTotal = str(round(userTotal, 2))
print("Your Total is: " + "$" + userTotal)
