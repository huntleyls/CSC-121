

strng = input('Enter a string : ')

count = [0] * 26


for ch in strng.upper():

    ascii = ord(ch)

    if ascii >= 65 and ascii <= 90:

        index = ascii - 65

        count[index] += 1

for i in range(0, len(count)):

    if count[i] > 0:

        print('%10s %10d' %(chr(i + 65), count[i]))
