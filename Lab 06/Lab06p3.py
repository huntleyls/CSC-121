def main():
    print("Please enter Jean's scores one by one.")
Jean = []
for i in range(0,4):
    Jean.append(float(input("Enter a Score:")))
print("Jean's scores:" , end =" ")
print(Jean)

print("Please enter Kayla's scores one by one.")
Kayla = []
for i in range(0,4):
    Kayla.append(float(input("Enter a Score:")))
print("Kayla's scores:" , end =" ")
print(Kayla)

print("Please enter Connie's scores one by one.")
Connie = []
for i in range(0,4):
    Connie.append(float(input("Enter a Score:")))
print("Connie's scores:" , end =" ")
print(Connie)


all=[]
all.append(Jean)
all.append(Kayla)
all.append(Connie)
print("All scores:" , end =" ")
print(all)


for i in range(0,4):
    Jean[i]=Jean[i]+1
    Kayla[i]=Kayla[i]+1
    Connie[i]=Connie[i]+1


allextra=[]
allextra.append(Jean)
allextra.append(Kayla)
allextra.append(Connie)
print("All scores after extra point:" , end =" ")
print(allextra)

allextrasort=[]
allextrasort.append(sorted(Jean))
allextrasort.append(sorted(Kayla))
allextrasort.append(sorted(Connie))

print("All scores after sorting:" , end =" ")
print(allextrasort)
if __name__ == '__main__':
    main()

