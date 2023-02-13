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

    print("The parity of ",a[2:]," is ",cal," (mod 2)")