def findSumPower(data,index,size):
    if index >= size:
        return 0

    sum = findSumPower(data,2*index+1,size)
    sum += findSumPower(data,2*index+2,size) + data[index]
    return sum

inp_ = input("Enter Input : ").split('/')
lst = list(map(int, inp_[0].split()))
print(sum(lst))
for i in inp_[1].split(","):
    i = i.split()
    temp1 = findSumPower(lst,int(i[0]),len(lst))
    temp2 = findSumPower(lst,int(i[1]),len(lst))
    print(i[0],end='')
    if temp1 == temp2:
        print("=", end='')
    elif temp1<temp2:
        print("<", end='')
    else:
        print(">", end='')
    print(i[1])