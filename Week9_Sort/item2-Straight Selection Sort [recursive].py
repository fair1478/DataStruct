haveNotCur = True
cur = None
def StraightSelectionSort(i,lis):
    global haveNotCur
    global cur
    if i < 0 :
        return
    
    if lis[i] < lis[i+1] and haveNotCur:
        StraightSelectionSort(i-1,lis)
        cur = i
        haveNotCur = False

    if lis[cur] < lis[cur+1] and not haveNotCur:
        StraightSelectionSort(i-1,lis)

    lis[i] ,lis[cur]  = lis[cur] ,lis[i]
    
    print(lis)

lis= [5,4,3,1,2]

StraightSelectionSort(len(lis)-2,lis)