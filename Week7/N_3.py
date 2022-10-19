class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None
        self.hight = 0

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
            self.hight = 1
        else:
            current = self.root
            temp = 1
            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        if self.hight < temp:
                            self.hight = temp
                        self.level = temp
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        self.level = temp
                        break
                else:
                    break
                
def printTree90(node:Node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

def father(r:Node,data):
    if r is None:
        return "Not Found Data"
    if data == r.data:
        return f"None Because {data} is Root"
    if int(data) < int(r.data):
        if r.left is None:
            return "Not Found Data"
        if int(r.left.data) == int(data):
            return str(r.data)
        return father(r.left,data)
    elif int(data) > int(r.data):
        if r.right is None:
            return "Not Found Data"
        if int(r.right.data) == int(data):
           return str(r.data)
        return father(r.right,data)

tree = BinarySearchTree()
data = input("Enter Input : ").split("/")
for e in data[0].split():
    tree.create(e)
printTree90(tree.root)
print(father(tree.root,data[1]))