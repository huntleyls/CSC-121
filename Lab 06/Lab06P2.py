import random
tuple=[]
for i in range (10):
    tuple.append(random.randrange(1, 16,))
print ("Tuple of 10 random numbers:", tuple)
tup=tuple[:3]
print("Tuple of first 3 numbers:", tup)
tup2=tuple[-3:]
print("Tuple of last 3 numbers:", tup2)
tup3=tup+tup2
print("Two tuples concatenated:", tup3)
tup4=sorted(tup3)
print("Two tuples concatenated and sorted: ",tup4)
