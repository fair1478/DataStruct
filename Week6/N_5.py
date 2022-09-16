def staircase(y,lenStair):
    if y == 0:
        return ''
    if lenStair < 0:
        return staircase(y+1,lenStair) + ("_"*abs(y+1) + "#"*abs(lenStair-y-1) +'\n')
    return staircase(y-1,lenStair) + ("_"*abs(lenStair-y) + "#"*abs(y) +'\n')
    
lenStair = int(input("Enter Input : "))
if lenStair == 0:
    print("Not Draw!")
else:
    print(staircase(lenStair,lenStair), end='')