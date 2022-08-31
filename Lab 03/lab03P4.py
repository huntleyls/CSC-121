def get_charge(weight,delivery):
    if delivery == 'S':
        if weight<=4:
            return 1.05
        elif weight>4 and weight<=8:
            return 0.95
        elif weight>8 and weight<=15:
            return 0.85
        else:
            return 0.80
    else:
        if weight<=2:
            return 3.25
        elif weight>2 and weight<=5:
            return 2.95
        elif weight>5 and weight<=10:
            return 2.75
        else:
            return 2.55

try:
    delivery = input("Enter S for standard shipping,E for express:")
    weight = float(input("Enter Weight (lbs):"))
    rate = get_charge(weight,delivery)
    charge = rate*weight
    print("Shipping charge:",charge)
except:
    print("Enter proper input ")
