score = []
i = 0
x = 0
myscore = 0

new_score = int(input("Enter an integer from 1 to 10 "))
score.append(new_score)
again = input("Enter another integer?  [y/n]")
while again == 'y':
    new_score = int(input("Enter an integer from 1 to 10 "))
    score.append(new_score)
    again = input("Enter another integer?  [y/n]")
if again == "n":
    print ("The list:", score)
    sc = sum(score)
    sco = sc / len(score)
    print("the averages is", sco)
if sco > 7:

    while i < len(score):
        myscore = score[i]
        x = myscore - 1
        i += 1
        print(x)
