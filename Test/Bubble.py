def Bubble(index,lis):

    if index < 0 :
        return
    
    Bubble(index-1,lis)
    if lis[index] > lis[index+1]:
        lis[index],lis[index+1] = lis[index+1],lis[index]

    Bubble(index-1,lis)
    if lis[index] > lis[index+1]:
        lis[index],lis[index+1] = lis[index+1],lis[index]

    return lis

def BubbleLoop(lis):

    for i in range(len(lis)):
        for j in range(len(lis)-1-i):
            if lis[j] > lis[j+1]:
                lis[j],lis[j+1] = lis[j+1],lis[j]

    return lis

inp = [3,2,1,5,6,7] or input("Enter : ").split()
inp = list(map(int,inp))
inp2 = inp.copy()
print(Bubble(len(inp)-2,inp))
print(BubbleLoop(inp2))