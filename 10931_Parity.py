<<<<<<< HEAD
##10931 Parity
while (True) :

    num = int(input())
    if (num == 0):
        break
    a = str(bin(num))
    cal = 0
    for i in  range(len(a)):
        if a[i] == '1':
            cal = cal +1

=======
##10931 Parity
while (True) :

    num = int(input())
    if (num == 0):
        break
    a = str(bin(num))
    cal = 0
    for i in  range(len(a)):
        if a[i] == '1':
            cal = cal +1

>>>>>>> c71bc47e055be75ff323e59e0d6cb65d94e985d2
    print("The parity of ",a[2:]," is ",cal," (mod 2)")