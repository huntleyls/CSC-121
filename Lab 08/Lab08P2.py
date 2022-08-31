def get_user_input():
    inputs = []
    while True:
        kwh = int(input("Enter kilowatt hours used: \n"))
        if kwh > 0:
            inputs.append(kwh)
            break
        else:
            print("kWh cannot be negative.")
    while True:
        letter = input("Enter R for residential customer, B for business customer: \n")
        letter = letter.upper()
        if letter == 'R' or letter == 'B':
            inputs.append(letter)
            break
        else:
            print("Invalid customer type.")
    return inputs

def bill_calculator(kwh, letter):
    bill = 0

    if letter == 'R':
        if kwh <= 500:
            bill = 0.12 * kwh
        else:
            bill = 60 + (0.15 * (kwh - 500))
        return bill
    else:
        if kwh <= 800:
            bill = 0.16 * kwh
        else:
            bill = 148 + (0.20 * (kwh - 800))
        return bill

input2 = get_user_input()
bill2 = bill_calculator(input2[0], input2[1])
print("Please pay this amount: $", bill2)
