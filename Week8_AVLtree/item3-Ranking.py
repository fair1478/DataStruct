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
        self.lis = []

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            self.lis.append(data)
            return self.root
        node = self.root
        while True:
            if data < node.data:
                if node.left == None:
                    node.left = Node(data)
                    self.lis.append(data)
                    return self.root
                node = node.left
            else: 
                if node.right == None:
                    node.right = Node(data)
                    self.lis.append(data)
                    return self.root
                node = node.right

    def pre_order(self, node):
        if node == None:
            return ''

        s = str(node.data) + ' '\
            + self.pre_order(node.left)\
                + self.pre_order(node.right)
        return s

    def in_order(self, node):
        if node == None:
            return ''

        s = self.in_order(node.left)\
             + str(node.data) + ' '\
                 + self.in_order(node.right)
        return s

    def post_order(self, node):
        if node == None:
            return ''
        
        s = self.post_order(node.left)\
            + self.post_order(node.right)\
                + str(node.data) + ' '
        return s

    def BreadthFirstSearch(self): 
        q = []
        q.insert(0,self.root)
        s = ""
        while not q.is_empty():
            node = q.pop(0)
            s += str(node.data) + ' '
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        return s

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def Rank(self,data):
        self.lis.sort()
        for i in range(len(self.lis)):
            if data < self.lis[i]:
                return i
        return len(self.lis)

# ----------------------------------- main ----------------------------------- #

T = BST()
inp = [ x for x in input("Enter Input : ").split("/")]
inpTree = [int(x) for x in inp[0].split()]
for i in inpTree:
    T.insert(i)
T.printTree(T.root)
print("--------------------------------------------------")
print(f"Rank of {inp[1]} : {T.Rank(int(inp[1]))}")