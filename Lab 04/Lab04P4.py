total = float(input("Enter initial deposit: "))
retirementFund = 0
year = 1
while year <= 10:
    if year == 1:
        total = total
        retirementFund = total*.05
    else:
        total = total + total * .02
        retirementFund = retirementFund + (total * .05)

    output_string = "Year " + str(year) + " total: $" + format(total,".2f")
    output_string = output_string +  "   Retirement Found Total So Far: " +  format(retirementFund, ".2f")
    print(output_string)
    year = year + 1

