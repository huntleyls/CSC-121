hour = float(input("Enter hour:"))
minute = float(input("Enter minute:"))
second = float(input("Enter second:"))
am_pm = input ("Enter AM or PM:")

if am_pm == "AM" and hour == 12:
    hours = hour * 0

if am_pm == "PM":
    hours = hour +12

seconds_since_midnight = ((3600 * hours) +(minute *60) + second)
print("Seconds since midnight:", seconds_since_midnight)
