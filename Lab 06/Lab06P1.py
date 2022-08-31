marks = []
for i in range(5):
    marks.append(float(input("Enter a test score: ")))
print("All scores:", marks)

newMarks = []
for i in range(len(marks)):
    if marks[i] < 60:
        newMarks.append(marks[i] + 10)
    else:
        newMarks.append(marks[i])
print("Students who scored below 60 get 10 extra points.")
print("All scores:", newMarks)
print("Students whose scores have changed:")
for i in range(len(marks)):
    if marks[i] !=newMarks[i]:
        print("Old score:",marks[i], "New score:", newMarks[i])


