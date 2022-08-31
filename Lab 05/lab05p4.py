import random
my_randoms=[]
for i in range (5):
    my_randoms.append(random.randrange(1, 10,))
print (my_randoms)
import random
my_random=[]
for i in range (5):
    my_random.append(random.randrange(1, 10,))
print (my_random)
def function(my_randoms,my_random):
    list3 = [max(value) for value in zip(my_randoms, my_random)]
    return list3
print("Larger number in each comparison:")
print(function(my_randoms,my_random))

