even_list = list( range(5,22,4))
print("First list: ", even_list)
print("Elements in the first list:")
for elem in even_list:
        print (elem,)
reversed_range = list(reversed(range(5,27,7)))
print("Second list:",reversed_range)
s = sum (reversed_range)
print ("Total of the elements in the second list",s)
