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

    def Dup(self):
        if len(self.queue) == len(set(self.queue)):
            return 'NO Duplicate'
        else:
            return 'Duplicate'


lst = input('Enter Input : ').split('/')
lstL = lst[0].split()
lstR = lst[1].split(',')

q = Queue(lstL)
for i in lstR:
    i = i.split()
    if i[0] == 'E':
        q.enQueue(i[1])
    elif i[0] == 'D':
        q.deQueue()
print(q.Dup())