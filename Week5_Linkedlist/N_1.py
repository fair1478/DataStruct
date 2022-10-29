class Node:
    def __init__(self, data, next= None):
        self.data= data 
        if next == None:
            self.next= None 
        else:
            self.next= next
        
        def __str__(self):
            return self.data

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def __str__(self):
        s=""
        t=self.head
        while t!=None:
            s+=str(t.data)
            t=t.next
            if t!=None:
                s+="->"
        return s

    def append(self,data):
        p = Node(data)
        if self.isEmpty():
            self.head = p
        else:
            t=self.head
            while t.next!=None:
                t=t.next
            t.next = p
        self.size+=1

    def insert(self, index, data):
            p=Node(data)
            if self.isEmpty():
                self.head = p
            elif index==0:
                p.next = self.head
                self.head = p
            else:
                t=self.head
                i = 0
                while i<index-1:
                    i+=1
                    t=t.next
                p.next = t.next
                t.next = p
            self.size +=1
        


inp = [i.strip() for i in input("Enter Input : ").split(",")]
l = inp[0].split()
lnk = LinkedList()
for i in l:lnk.append(int(i))
if lnk.isEmpty():
    print("List is empty")
else:
    print("link list : "+lnk.__str__())
for i in inp[1:]:
    index,data = [int(j)for j in i.split(":")]
    if index<0 or index>lnk.size:
        print("Data cannot be added")
    else:
        lnk.insert(index,data)
        print("index = "+str(index)+" and data = "+str(data))
    if lnk.isEmpty():print("List is empty")
    else:print("link list : "+lnk.__str__())