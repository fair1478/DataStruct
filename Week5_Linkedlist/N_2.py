class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        p = Node(item)
        if self.isEmpty():
            self.head = p
            self.tail = p
        else:
            p.previous = self.tail
            self.tail.next = p
            self.tail = p

    def addHead(self, item):
        p = Node(item)
        if self.isEmpty():
            self.head = p
            self.tail = p
        else:
            p.next = self.head
            self.head.previous = p
            self.head = p

    def insert(self, pos, item):
        p = Node(item) 
        if self.isEmpty():
            self.head = p
            self.tail = p
        elif pos == 0 or -1*pos>self.size():
            self.head.previous = p
            p.next = self.head
            self.head = p
        elif pos >= self.size()-1:
            self.tail.next = p
            p.previous = self.tail
            self.tail = p
        elif pos > 0:
            cur = self.head
            i = 0
            while i < pos-1:
                i += 1
                cur = cur.next
            p.next = cur.next
            cur.next.previous = p
            cur.next = p
            p.previous = cur
        else:
            cur = self.tail
            i = 1
            while i < -1*pos:
                i+=1
                cur = cur.previous
            p.previous = cur.previous
            cur.previous.next = p
            cur.previous = p
            p.next = cur

                 
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
                self.previous=None
            elif i==0:
                self.head = cur.next
                self.head.previous = None
            elif i==self.size()-1:
                self.tail = cur.previous
                self.tail.next = None
            else:
                cur.next.previous = cur.previous
                cur.previous.next = cur.next
            return "Success"


L = DoublyLinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())