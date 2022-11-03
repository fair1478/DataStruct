def printTree(data, index, size, level):
    if  index < size:
        printTree(data, 2 * index + 2, size, level + 1)
        print('        ' * level, data[index])
        printTree(data, 2 * index + 1, size, level + 1)


inp = input('Enter Input : ').split('/')
data = []
van = {}
for i in range(int(inp[0])):
    van[i+1] = van.get(i+1,0)
    data.append(int(i)+1)

for cus, key in enumerate(inp[1].split()):
    print(f'Customer {cus + 1} Booking Van {data[0]} | {key} day(s)')
    temp = data.pop(0)
    van[temp] = van.get(temp, 0) + int(key)
    for index, key in enumerate(data):
        if  van[temp] < van[key] or (van[temp] == van[key] and temp < key):
            data.insert(index, temp)
            temp = None
            break
    if temp:
        data.append(temp)