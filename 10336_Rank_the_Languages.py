'''
1
4 8
ttuuttdd
ttuuttdd
uuttuudd
uuttuudd
'''

'''
我的想法:

首先將出現的字母，存放進Letter裡面。
用意是可以將位置的數據存在同意維度。
例:
Letter = [t,u,d]
area = [
    [[0,1,4,5],[0,1,4,5],[2,3],[2,3],] ##t
    [[2,3],[2,3],[0,1,4,5],[0,1,4,5],] ##u
    [[6,7],[6,7],[6,7],[6,7]]         ##d
    ]
area = [
    [[0,1,4,5],[2,3],[6,7]],
    [[0,1,4,5],[2,3],[6,7]], 
    [[2,3],[0,1,4,5],[6,7]].
    [[2,3],[0,1,4,5],[6,7]].
    ]
然後再判斷第一次的數據:
    [0,1]連續所以t範圍+1，[2,3]連續所以u範圍+1，已次類推。
第二次:
    [0,1]連續但是前一個陣列已經出現過，所以pass。
    [2,3]連續但是前一個陣列已經出現過，所以pass。
第三次:
    [2,3]連續而且在這之前的u陣列沒出現過，所以+1。
    [0,1]連續而且在這之前的u陣列沒出現過，所以+1。
'''
Data_quantity = int(input())
Letter = []

area = [[[]]]

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
            
