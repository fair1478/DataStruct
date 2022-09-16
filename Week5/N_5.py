class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return ""
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        p = Node(item)
        if self.isEmpty():
            self.head = p
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = Node(item)

    def addHead(self, item):
        p = Node(item)
        if self.isEmpty():
            self.head = p
        else:
            p.next = self.head
            self.head = p

    def insert(self, pos, item):
        p = Node(item) 
        if self.isEmpty():
            self.head = p
        elif pos == 0 or -1*pos>self.size():
                p.next = self.head
                self.head = p
        elif pos >= self.size()-1:
            self.append(item)
        elif pos > 0:
            cur = self.head
            i = 0
            while i < pos-1:
                i += 1
                cur = cur.next
            p.next = cur.next
            cur.next = p

                 
    def search(self, item):
        q = self.head
        while q != None:
            if q.value == item:
                return "Found"
            q = q.next
        return "Not Found"

    def index(self, item):
        i = 0
        q = self.head
        while q!=None:
            if q.value==item:
                return i
            q=q.next
            i+=1
        return -1

    def size(self):
        if self.isEmpty():
            return 0
        else:
            i = 1
            q = self.head
            while q.next != None:
                i += 1
                q = q.next
            return i

    def pop(self, pos):
        if pos<0 or pos>=self.size():
            return "Out of Range"
        else:
            i=0
            cur=self.head
            while i<pos:
                cur=cur.next
                i+=1
            if self.size()==1:
                self.head=None
            elif i==0:
                self.head = cur.next
                return cur
            else:
                previous = cur
                cur = cur.next
                previous.next = cur.next
            return cur

    def appendWithSortMax(self,item):
        cur = self.head
        previous = None
        while cur != None and cur.value > item:
            previous = cur
            cur = cur.next
        if previous != None:
            previous.next = Node(item,cur)
        else:
            self.head = Node(item,cur)

def maxDigit(item:int):
    if item < 0:
        item *= -1

    i = 0 
    while item > 0:
        item //= 10
        i += 1
    return i

def getDigitValue(item:int,d:int):
    if item < 0:
        item *= -1

    for i in range(d-1):
        item = item // 10
    return item%10
    
def RadixSort(input_list):
    beforLinkedList = LinkedList()
    mainLinkedList = LinkedList()

    for item in input_list:
            beforLinkedList.append(item)
            mainLinkedList.append(item)
    
    maxBits = maxDigit(max(input_list))
    nestLinkedList = [LinkedList(),LinkedList(),LinkedList(),LinkedList(),LinkedList(),LinkedList(),LinkedList(),LinkedList(),LinkedList(),LinkedList()]
    
    count = 0
    for i in range(1,maxBits+2):
        count += 1
        while not mainLinkedList.isEmpty():
            item = mainLinkedList.pop(0).value
            valueDigit = getDigitValue(item,i)
            nestLinkedList[valueDigit].appendWithSortMax(item)
        print("------------------------------------------------------------")

        print(f"Round : {i}")
        for j in range(10):
            print(f"{j} : {nestLinkedList[j]}")

        
        sumStatus = 0
        for i in range(1,10):
            sumStatus += not nestLinkedList[i].isEmpty()
        if sumStatus == 0:
            for i in range(10):
                while not nestLinkedList[i].isEmpty():
                    mainLinkedList.append(nestLinkedList[i].pop(0).value)
            break
        
        for i in range(10):
            while not nestLinkedList[i].isEmpty():
                mainLinkedList.append(nestLinkedList[i].pop(0).value)


    print("------------------------------------------------------------")
    print(f"{count-1} Time(s)")
    print("Before Radix Sort :"," -> ".join(str(beforLinkedList).split()))
    print("After  Radix Sort :"," -> ".join(str(mainLinkedList).split()))

inp = list(map(int,input("Enter Input : ").split()))
RadixSort(inp)