class Queue:

    def __init__(self, list = None):
        self.queue = list if list != None else []

    def __str__(self):
        return  ', '.join(str(data) for data in self.queue) if self.size() != 0 else 'Empty'
    
    def enQueue(self, item):
        self.queue.append(item)
    
    def deQueue(self):
        return self.queue.pop(0) if self.size() != 0 else 'Empty'

    def size(self):
        return len(self.queue)

    def insert(self,index,item):
        self.queue.insert(index,item)

inp = input("Enter Input : ").split(",")
myQ = Queue()
yourQ = Queue()
kanan = 0
dict_acti = {0:"Eat",1:"Game",2:"Learn",3:"Movie"}
dict_Po = {0:"Res.",1:"ClassR.",2:"SuperM.",3:"Home"}

for x in inp:
    myQ.enQueue(x.split()[0])
    yourQ.enQueue(x.split()[1])


for x in range(myQ.size()):
    if myQ.queue[x] == yourQ.queue[x]:
        kanan += 4
    elif myQ.queue[x][2] == yourQ.queue[x][2]:
        kanan += 2
    elif myQ.queue[x][0] == yourQ.queue[x][0]:
        kanan += 1
    else:
        kanan -= 5

print("My   Queue = ",myQ,sep="")
print("Your Queue = ",yourQ,sep="")


print("My   Activity:Location = ",end="")
for x in range(myQ.size()):
    if x < myQ.size()-1:
        print(f"{dict_acti[int(myQ.queue[x][0])]}:{dict_Po[int(myQ.queue[x][2])]}, ",end="")
    else:
        print(f"{dict_acti[int(myQ.queue[myQ.size()-1][0])]}:{dict_Po[int(myQ.queue[myQ.size()-1][2])]}")

print("Your Activity:Location = ",end="")
for x in range(yourQ.size()):
    if x < yourQ.size()-1:
        print(f"{dict_acti[int(yourQ.queue[x][0])]}:{dict_Po[int(yourQ.queue[x][2])]}, ",end="")
    else:
        print(f"{dict_acti[int(yourQ.queue[myQ.size()-1][0])]}:{dict_Po[int(yourQ.queue[myQ.size()-1][2])]}")
    
if kanan >= 7:
    print(f"Yes! You're my love! : Score is {kanan}.")
elif kanan >=0:
    print(f"Umm.. It's complicated relationship! : Score is {kanan}.")
else:
    print(f"No! We're just friends. : Score is {kanan}.")





