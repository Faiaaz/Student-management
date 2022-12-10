# student function
def students():
    student_names = []
    n = int(input("how many students do you wish to register? "))

    print("enter student name(s): ")
    for i in range(0,n):
        name = input()
        student_names.append(name)

    print("the students are: ", student_names)

