class node:
    def __init__(self,data:int,next = None ):
        self.data = data
        self.next = next
    def __str__(self):
        if self.data == None:
            return "Empty"
        else:
            return str(self.data)

def createList(l=[]):
    temp =[]
    for x in l:
        temp.append(x)
    head = node(l[0])
    cur = head
    for x in temp[1:]:
        cur.next = node(x)
        cur = cur.next
    return head

def printList(H:node):
    cur = H
    s = ""
    while cur != None:
        s += str(cur.data) + " "
        cur = cur.next
    print(s)

def mergeOrderesList(p:node,q:node):
    head = p
    cur = p
    while cur.next != None:
        cur = cur.next
    cur.next = q
    while cur != None:
        cur = cur.next
    
    cur = head
    tempList = []
    while cur != None:
        tempList.append(int(cur.data))
        cur = cur.next
    tempList.sort()
    head = createList(tempList)
    return head

#################### FIX comand ####################   
# input only a number save in L1,L2
L1,L2 = input("Enter 2 Lists : ").split()
LL1 = createList(L1.split(","))
LL2 = createList(L2.split(","))
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)