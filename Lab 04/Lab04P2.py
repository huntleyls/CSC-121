hour = float(input("Enter Hour: "))
while hour < 1 or hour > 12:
    print('Hour must be from 1 to 12.')
    hour = float(input("enter hour: "))
minute = float(input("Enter Minute: "))
while  0 > minute or 59 < minute:
    print('Minute must be from 0 to 59 .')
    minute = float(input("Enter Minute: "))
second = float(input("Enter Second: "))
while  second < 0 or second > 59:
    print('Second must be from 0 to 59 .')
    second = float(input("Enter Second: "))
am_pm = input("AM or PM: ")
while  am_pm != "AM" and am_pm != "PM":
    print('please enter am or pm.')
    am_pm = (input("AM or PM: "))

hours = 0

if am_pm == "AM" and hour == 12:
    hours =  0

if am_pm == "PM" and hour == 12:
    hours = 12

if am_pm == "PM" and hour != 12:
    hours = hour + 12

seconds_since_midnight = ((3600 * hours) +(minute *60) + second)
print("Seconds since midnight:", seconds_since_midnight)
