class Queue:

    def __init__(self):
        self.item = []

    def enQueue(self,i):
        self.item.append(i)
    
    def deQueue(self):
        return self.item.pop(0) if self.size() != 0 else 'Empty'

    def isEmpty(self):
        return True if self.item == [] else False
    
    def size(self):
        return len(self.item)

class Stack:
    def __init__(self):
        self.item = []
        
    def isEmpty(self):
        return len(self.item) == 0
    
    def size(self):
        return len(self.item)
    
    def peek(self):
        return self.item[-1] if self.size()>0 else -1

    def push(self,tmp):
        self.item.append(tmp)
    
    def pop(self):
        return self.item.pop()
            
inp1 = input("Enter people and time : ").split(" ")
main = list(inp1[0])
cashier1 = Queue()
cashier2 = Queue()
stack1 = Stack()
stack2 = Stack()


for i in range(int(inp1[1])):
    if stack1.size()>=3:
        if stack1.item[0] == stack1.item[1] == stack1.item[2]:
            while not stack1.isEmpty(): stack1.pop()
            cashier1.deQueue()

    if stack2.size()>=2:
        if stack2.item[0] == stack2.item[1]:
            while not stack2.isEmpty(): stack2.pop()
            cashier2.deQueue()

    if cashier1.size()<5 and main:
        cashier1.enQueue(main[0])
        main.pop(0)
    elif cashier2.size()<5 and main:
        cashier2.enQueue(main[0])
        main.pop(0)

    if not cashier1.isEmpty() and cashier1.item[0] != None:      
        stack1.push(cashier1.item[0])
    if not cashier2.isEmpty() and cashier2.item[0] != None:
        stack2.push(cashier2.item[0])
    
    print(i+1,main,cashier1.item,cashier2.item,sep=" ")
    
