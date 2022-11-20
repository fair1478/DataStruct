def bi_search(arr, x):
    
    if len(arr)==1:
        print(arr)
        return False

    mid = len(arr)//2
    if x < arr[mid]:
        return bi_search(arr[0:mid],x)
    elif x > arr[mid]:
        return bi_search(arr[mid+1:len(arr)],x)
    else:
        return True

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(sorted(arr), k))