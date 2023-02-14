'''
1
4 8
ttuuttdd
ttuuttdd
uuttuudd
uuttuudd
'''
'''
先擱著
'''
Data_quantity = int(input())
Letter = []
area = [[[]]]
mapp = []
#str = []

for i in range(Data_quantity):
    Rows,Size = map(int,input().split())
    
    mapplist = []
    for j in range(Rows):
        mapp.append([])
        mapp[j] = input()
        mapplist.append([])
        mapplist[y] = list(mapp[y])
    

    for y in range(Rows):
        for x in range(Size):
            if(mapp[y][x] not in Letter):
                Letter.append(mapp[y][x])
                mapplist[y][x] = Letter.index(mapp[y][x])
            elif(mapp[y][x] in Letter):
                mapplist[y][x] = Letter.index(mapp[y][x])
            #print(Letter.index(mapp[y][x]))
    

    print(mapplist)
                





'''

for i in range(Data_quantity):
    Rows,Size = map(int,input().split())

    for j in range(Rows):
        str = input()
        #print("A",area)
        #print("B",Letter)
        #area[j].append([])
        for k in range(len(Letter)):
            area[j].append([])

        for k in range(Size):
            
            #print(str[k] not in Letter)
            if(str[k] not in Letter):
                Letter.append(str[k])
                ##print(Letter.index(str[k]))
                area[j].append([])
                area[j][Letter.index(str[k])].append(k) 
            elif(str[k] in Letter):
                try:
                    area[j][Letter.index(str[k])].append(k)
                except IndexError:
                    area[j].append([])
                    area[j][Letter.index(str[k])].append(k)
        area.append([])

        


print(area)
'''
            
