##10789 Prime Frequency



## 函式解說
def Isprime(N):
    if (N > 2):
        if (N % 2 == 0): ##質數絕對不可能被2給整除
            return False
        for i in range(3,int((N ** (0.5)))+1,2): ##根據埃拉托斯特尼篩法，迴圈不用計算到N-1，只需要到平方根N就好
            if (N % i == 0) :
                return False
        return True
    elif (N == 2):
        return True
    else:
        return False
    

T = int(input())
empty = 0
out = ""
for i in range(T) :
    str = input()
    out = ""
    for j in range(26):
        capital = str.count(chr(65+j))
        if (Isprime(capital)):
            ##print("case ",i+1,":",chr(65+j))
            out += chr(65+j)
    for j in range(26):
        lower = str.count(chr(97+j))
        if (Isprime(lower)):
            #print("case ",i+1,":",chr(97+j))
            out += chr(97+j)
    for j in range(9):
        num = str.count(chr(48+j))
        if (Isprime(num)):
            #print("case ",i+1,":",chr(48+j))
            out += chr(48+j)
    if len(out) == 0 :
        print("case ",i+1,":","empty")
    else:
        print("case ",i+1,":",out)
    






