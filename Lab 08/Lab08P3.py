start_num = int(input("Enter starting number: "))
end_num = int(input("Enter ending number: "))

my_list = list(x for x in list(range(start_num, end_num+1)) if x%2 == 1)

print("odd numbers in the range:", my_list)
