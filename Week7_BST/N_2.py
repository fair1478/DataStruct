class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
        self.hight = 0

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
            return self.root
        cur = self.root
        temp = 0
        while 1:
            temp += 1
            if cur.data > data:
                if cur.left != None:
                    cur = cur.left
                else:
                    cur.left = Node(data)
                    if self.hight < temp:
                        self.hight = temp
                    break
            else:
                if cur.right != None:
                    cur = cur.right
                else:
                    cur.right = Node(data)
                    if self.hight < temp:
                        self.hight = temp
                    break
        return self.root
                
    def SearchBelow(self,node,level,item):
        if node != None:
            self.SearchBelow(node.left, level + 1,int(item))
            if node.data < item:
                lis.append(node.data)
            self.SearchBelow(node.right, level + 1,int(item))
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
lis = []
ipp = input("Enter Input : ").split("|")
inp = [int(i) for i in ipp[0].split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
T.SearchBelow(root,0,int(ipp[1]))
print("--------------------------------------------------")
print(f"Below {ipp[1]} : ",end="")
if len(lis) != 0:   
    for i in lis:
        print(i,end=" ")
else:
    print("Not have")
