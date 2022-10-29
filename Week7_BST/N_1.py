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

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
            return self.root
        cur = self.root
        while 1:
            if cur.data > data:
                if cur.left != None:
                    cur = cur.left
                else:
                    cur.left = Node(data)
                    break
            else:
                if cur.right != None:
                    cur = cur.right
                else:
                    cur.right = Node(data)
                    break
        return self.root
                
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)