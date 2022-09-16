from statistics import mode

def check(RecieveList):
    global pa
    tempList =[]
    pa = False
    for x in RecieveList:
        if 0<x<21:
            pa = True
            tempList.append(x)
        else:
            pass
    RecieveList.clear()
    RecieveList = tempList.copy()
    return RecieveList

print("*** Election ***")
num = int(input("Enter a number of voter(s) : "))
ls=[]
ls = list(map(int,input().strip().split()))[:num]
ls = check(ls)
if pa:
   print(mode(ls)) 
else:
    print("*** No Candidate Wins ***")
