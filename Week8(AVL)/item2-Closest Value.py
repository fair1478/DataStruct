class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return self.root
        node = self.root
        while True:
            if data < node.data:
                if node.left == None:
                    node.left = Node(data)
                    return self.root
                node = node.left
            else: 
                if node.right == None:
                    node.right = Node(data)
                    return self.root
                node = node.right

    def searchClosest(self,data):
        diffVal = []
        traversal = []
        node = self.root
        while True:
            if data == node.data:
                print(f"Closest value of {data} : {node.data}")
                return
            if data < node.data:
                diffVal.append(abs(node.data-data))
                traversal.append(node.data)
                if node.left == None:
                    break
                node = node.left
            else:
                diffVal.append(abs(node.data-data))
                traversal.append(node.data)
                if node.right == None:
                    break
                node = node.right

        minn = min(diffVal)
        inde = -1
        for i in diffVal:
            inde+=1
            if minn == diffVal[inde]:
                break
        print(f"Closest value of {data} : {traversal[inde]}")

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
        q = Queue()
        q.enqueue(self.root)
        s = ""
        while not q.is_empty():
            node = q.dequeue()
            s += str(node.data) + ' '
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)
        return s

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


# ----------------------------------- main ----------------------------------- #

T = BST()
inp = [ x for x in input("Enter Input : ").split("/")]
inpTree = [int(x) for x in inp[0].split()]
for i in inpTree:
    T.printTree(T.insert(i))
    print("--------------------------------------------------")
T.searchClosest(int(inp[1]))
