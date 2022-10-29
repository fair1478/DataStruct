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
        

inp = input('Enter Input : ').split(',')
queue = Queue()
for i in inp:
    if i[0] == "E":
        queue.enQueue(i[2:])
        print("Add",i[2:],"index is",queue.size()-1)
    else:
        if queue.size()>0:
            print("Pop",queue.deQueue(),"size in queue is",queue.size())
        else:
            print("-1")
print("Number in Queue is : ",queue.item) if not queue.isEmpty() else print("Empty") 


