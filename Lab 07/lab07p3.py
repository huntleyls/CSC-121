def bill_calculator(kWh,ctype):
    if ctype == 'R' or 'r':
        if kWh>500:
            return 500*.12 +(kWh-500)*.15
        else:
            return kWh*.12
    else:
        if kWh>800:
            return 800*.16 +(kWh-800)*.2
        else:
            return kWh*.16

def main():
    kw=float(input('Enter kilowatt hours used: '))
    cust=input('Enter R for residential customer, B for business customer: ')
    amount=bill_calculator(kWh=kw, ctype=cust)#passing keyword arguments
    print('Please pay this amount:',amount)

if __name__ == '__main__':
    main()
