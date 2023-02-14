def whowin(str1,str2):
    if(str1 == "rock"):
        if(str2 == "rock"):
            return 0
        elif(str2 == "scissors"):
            return 1
        elif(str2 == "paper"):
            return 2
    elif(str1 == "paper"):
        if(str2 == "rock"):
            return 1
        elif(str2 == "scissors"):
            return 2
        elif(str2 == "paper"):
            return 0
    elif(str1 == "scissors"):
        if(str2 == "rock"):
            return 2
        elif(str2 == "scissors"):
            return 0
        elif(str2 == "paper"):
            return 1
        
while(True):

    try:
        Quantity,Sessions = map(str,input().split())
    except:
        break

    Quantity = int(Quantity)
    Sessions = int(Sessions)
    if (Quantity == 0):
        break

    palyer = []

    for i in range(Quantity):
        palyer.append([0,0]) ## 0 是win 1 是lose
    '''
    print(palyer)
    palyer[1][1] += 1
    print(palyer)
    '''
#  k ∗ n ∗ (n − 1)/2 
    total = int((Sessions * Quantity * (Quantity -1) )/2)
    for i in range(total):
        playone,first,playtwo,second = map(str,input().split())
        playone = int(playone) -1
        playtwo = int(playtwo) -1
        ##print("playone : ",playone,"playtwo : ",playtwo)
        if (whowin(first,second) == 1):
            palyer[playone][0] += 1
            palyer[playtwo][1] += 1
        elif (whowin(first,second) == 2):
            palyer[playone][1] += 1
            palyer[playtwo][0] += 1
        '''
        elif (whowin(first,second) == 0):
            palyer[playone][1] += 1
            palyer[playtwo][1] += 1
        '''

    for i in range(Quantity):
        try:
            probability = palyer[i][0] / (palyer[i][0] + palyer[i][1])
            print("%.3f" % probability)
        except:
            print("-")

        
        
        #print("palyer 1 win ",palyer[i][0],"lose:",palyer[i][1])
        

    print()
''''
2 4 
1 rock 2 paper
1 scissors 2 paper
1 rock 2 rock
2 rock 1 scissors
'''