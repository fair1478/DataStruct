class Stack :

    def __init__(self):
        self.items = []

    def push(self,i):
        self.items.append(int(i))
    
    def pop(self):
        if(self.isEmpty() == True):
            return -1
        else:
            return self.items.pop()

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        elif len(self.items) >0:
            return False

    def size(self):
        return str(len(self.items))

    def ManageStack(self,i):
        temp = []
        T = [str(y) for y in i.split(" ")]
        if T[0] == "A":
            self.push(T[1])
            print("Add = ",T[1],sep="")
        elif T[0] == "P":
            if self.isEmpty():
                print("-1")
                return -1
            print("Pop = ",self.pop(),sep="")
        elif T[0] == "D":
            if self.isEmpty():
                print("-1")
                return -1
            for x in self.items:
                if x != int(T[1]):
                    temp.append(x)
                else:
                    print("Delete = ",T[1],sep="")
            if self.items != temp.copy():
                self.items = temp.copy()
                temp.clear()
            else:
                return -1
        elif T[0] == "LD":
            tempp = []
            if self.isEmpty():
                print("-1")
                return -1
            for x in self.items:
                if x >= int(T[1]):
                    temp.append(x)
                # elif x == int(T[1]):
                #     print("Delete = ",x,sep="")
                #     self.items.remove(x)
                #     temp = self.items.copy()
                #     break
                else:
                    tempp.append(x)
            tempp.reverse()
            for i in tempp:
                print("Delete = ",i," Because ",i," is less than ",T[1],sep="")
            tempp.clear()
            if self.items != temp.copy():
                self.items = temp.copy()
                temp.clear()
            else:
                return -1
        elif T[0] == "MD":
            tempp = []
            if self.isEmpty():
                print("-1")
                return -1
            for x in self.items:
                if x <= int(T[1]):
                    temp.append(x)
                # elif x == int(T[1]):
                #     print("Delete = ",x,sep="")
                #     self.items.remove(x)
                #     temp = self.items.copy()
                #     break
                else:
                    tempp.append(x)
            tempp.reverse()
            for i in tempp:
                print("Delete = ",i," Because ",i," is more than ",T[1],sep="")
            tempp.clear()
            if self.items != temp.copy():
                self.items = temp.copy()
                temp.clear()
            else:
                return -1    

            
S = input("Enter Input : ").split(',')

stack = Stack()

for x in S:
    stack.ManageStack(x)
    
print("Value in Stack = ",stack.items,sep="")