class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class AVL:

    def __init__(self):
        self.root = None

    def insert(self,node:Node,data:int):
    
        if node is None:
            return Node(data)

        if data < node.data:
            node.left = self.insert(node.left,data)
        elif data > node.data:
            node.right = self.insert(node.right,data)

        balance = self.getBalance(node)

        if balance > 1 and data < node.data:
            return self.rightRotate(node)

        if balance < -1 and data > node.data:
            return self.leftRotate(node)

        if balance > 1 and data > node.data:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        if balance < -1 and data < node.data:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node

    def leftRotate(self,node):
        temp = node.right
        temp2 = temp.left

        temp.left = node
        node.right = temp2

        return temp
    
    def rightRotate(self,node):
        temp = node.left
        temp2 = temp.right

        temp.right = node
        node.left = temp2

        return temp


    def getHight(self,node:Node):
        if node is None:
            return 0
        
        return  1 + max(self.getHight(node.right),self.getHight(node.left))

    def getBalance(self,node:Node):
        if node is None:
            return 0

        return self.getHight(node.left) - self.getHight(node.right)

    def printTree(self, node:Node, level = 0):
            if node != None:
                # print(node.data)
                self.printTree(node.right, level + 1)
                print('     ' * level, node.data)
                self.printTree(node.left, level + 1)

# tree = AVL()
# inp = input("ENTER").split(",")
# for i in inp:
#     tree.root = tree.insert(tree.root,int(i))
#     tree.printTree(tree.root)
#     print("-----------------------------------------------------")
# tree.printTree(tree.root)


