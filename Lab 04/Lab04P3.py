height = float(input("Enter initial height:"))
BI = float(input("Enter bounciness index: "))
bounces = float(input("Enter number of times the ball is allowed to bounce:"))
iteration = 1
while iteration <= bounces:

    height = height * BI

    output_string = "number of bounces " + str(iteration) + " height: " + str(height)

    print(output_string)
    iteration = iteration + 1

