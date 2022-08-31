def main():
    l=input("How many labs :")
    Lab=list()
    for i in range(0,int(l)):
        a=input("Enter a lab score :")
        Lab.append(float(a))
    print(Lab)
    Test=list()
    t=input("How many tests :")
    for i in range(0,int(t)):
        a=input("Enter a lab score :")
        Test.append(float(a))
    print(Test)
    print("The default weights for course grade are 50% labs and 50% tests.")
    a=input("Enter C to change the weights or D to use default weights: ")
    if(a=="D"):
        grade_calculator1(Lab,Test)
    if(a=="C"):
        lp=input("Enter lab percentage (without the % sign) : ")
        tp=input("Enter test percentage (without the % sign) : ")
        lp=float(lp)
        tp=float(tp)
        grade_calculator2(Lab,Test,lp,tp)




def grade_calculator2(Lab,Test,lp,tp):
    lab_average=0
    for i in Lab:
        lab_average=lab_average+i
    lab_average=lab_average/len(Lab)
    test_average=0
    for i in Test:
        test_average=test_average+i
    test_average=test_average/len(Test)
    print("Lab average : ",(lab_average*lp)/100)
    print("Test average : ",(test_average*tp)/100)
    print("Course grade : ",(((lab_average*lp)/100)+((test_average*tp)/100)))



def grade_calculator1(Lab,Test):
    lab_average=0
    for i in Lab:
        lab_average=lab_average+i
    lab_average=lab_average/len(Lab)
    test_average=0
    for i in Test:
        test_average=test_average+i
    test_average=test_average/len(Test)
    print("Lab average : ",lab_average)
    print("Test average : ",test_average)
    print("Course grade : ",(lab_average+test_average)/2)
