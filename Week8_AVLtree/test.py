class Node:
    def __init__(self, data:int):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

# listinp = [2,5,3,4,7,9]


# root = Node(listinp[0])
# def add(lis:list):
#     for i in lis[1:]:
#         cur = root
#         while cur is not None:
#             if i < cur.data:
#                 if cur.left is None:
#                     cur.left = Node(i)
#                     break
#                 cur = cur.left
#             elif i > cur.data:
#                 if cur.right is None:
#                     cur.right = Node(i)
#                     break
#                 cur = cur.right

# def printtt(node,lev=0):
#     if node:
#         printtt(node.right,lev+1)
#         print('     '*lev,node.data)
#         printtt(node.left,lev+1)

# add(listinp)
# printtt(root)



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

    def Maxxx(self,node):
        node = self.root
        max = self.root.data
        while node is not None:
            if max < node.data:
                max = node.data
            node = node.right
        return max
    
    def sizeOf(self,node):
        if node is None:
            return 0
        
        sizeL = self.sizeOf(node.left)
        sizeR = self.sizeOf(node.right)

        return sizeL + 1 + sizeR  

    def highTree(self,node):
        if node is None:
            return -1
        highL = self.highTree(node.left)
        highR = self.highTree(node.right)

        return 1 + max(highL,highR)
    

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def delete(self,data:int,node:Node):
        if node is None:
            return node

        if data < int(node.data):
            node.left = self.delete(data,node.left)
        elif data > int(node.data):
            node.right = self.delete(data, node.right)
        else:


            if node.left is None:
                temp = node.right
                node = None
                return temp
            if node.right is None:
                temp = node.left
                node = None
                return temp

            temp = node.right
            while temp.left is not None:
                temp = temp.left
            
            node.data = temp.data
            node.right = self.delete(temp.data,node.right)
        return node

            



    
tree = BST()
inp = input("ENTER").split()
for i in inp:
    tree.root = tree.insert(int(i))
tree.printTree(tree.root)
tree.delete(int(3),tree.root)
print("-----------------------------------------------")
tree.printTree(tree.root)