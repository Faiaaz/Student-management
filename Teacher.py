#Teacher function
def teachers():
    teacher_names = []
    n = int(input("how many teachers do you wish to register? "))

    print("enter teacher name(s): ")
    for i in range(0,n):
        name = input()
        teacher_names.append(name)

    print("the teachers are: ", teacher_names)