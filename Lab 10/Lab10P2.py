f = open("water.txt", "r")
for line in f:
    words = line.strip().split()
    number = words[0]
    customer_type = words[1]
    gallons = int(words[2])
    charge = 0
    if customer_type == "R":
        if gallons <= 6000:
            charge = gallons * 0.005
        else:
            charge = (6000 * 0.005) + ((gallons-6000) * 0.007)
    else:
        if gallons <= 8000:
            charge = gallons * 0.006
        else:
            charge = (8000 * 0.006) + ((gallons-8000) * 0.008)
    print("Account number: %s Water charge: $%.2f" % (number, charge))
f.close()
