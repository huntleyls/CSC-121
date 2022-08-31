course  = []
def findcourse (c):
    if len(course ) > 0:
        for x in course :
            if x == c:
                return True
        return False
    else:
        return False
def addcourse (c):
    if(findcourse (c)):
        print("You are already registered in that course")
    else:
        course .append(c)
        print("Course added")
        print("registered courses",sorted(course ))
def deletecourse (c):
    if (not findcourse (c)):
        print("You are not registered in that course")
    else:
        course .remove(c)
        print("Course deleted")
        print(sorted(course ))
def main():
    while(True):
        choice = input("Enter A to add course, D to drop course or E to exit: ")
        if(choice == 'A'):
            c = input("Enter the course to add: ")
            addcourse (c)
        elif(choice == 'D'):
            c = input("Enter the course to drop: ")
            deletecourse (c)
        else:
            break
main()
