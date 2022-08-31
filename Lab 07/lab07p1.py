def bill_calculator(power):
    if power <= 500:
        return power * 0.12
    else:
        return (500 * 0.12) + ((power - 500) * 0.15)


def main():
    power = float(input('Enter kilowatt hours used: '))
    print('Please pay this amount: ' + str(bill_calculator(power)))

main()
