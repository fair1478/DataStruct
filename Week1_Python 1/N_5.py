
from ast import Num


print("*** Fun with countdown ***")
ls = [int(x) for x in input("Enter List : ").split()]
newLs = []
realLs = []
n=0
for i in range(len(ls)):
    if ls[i] == 1:
        n +=1
        temp = [1]
        j = i
        while ls[j-1] == ls[j]+1:
            temp.append(ls[j-1])
            j-=1
        temp.reverse()
        newLs.append(temp)
realLs.append(newLs)
realLs.insert(0,n)
print(realLs)