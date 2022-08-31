def get_kWh_used():
    kWh = float(input("Enter kilowatt hours used:"))
    while (kWh < 0):
        print ("kWh cannot be negative")
        kWh = float(input("Enter kilowatt hours used:"))
    return kWh

def bill_calculator(kWh):
    if (kWh<500):
        return  kWh * 0.12
    else:
        return (500 * 0.12) + (kWh - 500) * 0.15
if __name__ == '__main__':
    kWh = get_kWh_used()
    print("please pay this amount:", bill_calculator(kWh),)
