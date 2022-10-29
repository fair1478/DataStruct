class Stack:
    def __init__(self):
        self.stk = []
        
    def isEmpty(self):
        return len(self.stk) == 0
    
    def size(self):
        return len(self.stk)
    
    def peek(self):
        return self.stk[-1] if self.size()>0 else -1

    def push(self,tmp):
        self.stk.append(tmp)
    
    def pop(self):
        return self.stk.pop()

s = Stack()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[0]=='A':
        while int(i[2:])>=s.peek() and s.size()>0:
            s.pop()
        s.push(int(i[2:]))
    else:
        print(s.size())