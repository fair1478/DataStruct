import AVLtree

class nNode(AVLtree.Node):
    def __init__(self, data, left=None, right=None):
        super().__init__(data, left, right)

class tavl(AVLtree.AVL):
    
    def __init__(self):
        super().__init__()

    def insert(self, node: nNode, data: int):
        
        if node is None:
            return nNode(data)

        if data < node.data:
            node.left = self.insert(node.left,data)
        elif data > node.data:
            node.right = self.insert(node.right,data)

        
        balance = self.getBalance(node)

        # left left
        if balance > 1 and data < node.data:
            return self.rightRotate(node)

        # right right
        if balance < -1 and data > node.data:
            return self.leftRotate(node)

        # left right
        if balance > 1 and data > node.data:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        
        # right left
        if balance < -1 and data < node.data:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)


        return node

    def getHight(self, node: nNode):
        if node is None:
            return 0

        return 1 + max(self.getHight(node.left),self.getHight(node.right))

    def getBalance(self, node: nNode):
        if node is None:
            return 0

        return self.getHight(node.left) - self.getHight(node.right)

    def leftRotate(self, node:nNode):

        y = node.right
        z = y.left

        y.left = node
        node.right = z

        return y

    def rightRotate(self, node:nNode):
        temp = node.left
        temp2 = temp.right

        temp.right = node
        node.left = temp2

        return temp



ter = tavl()
for i in [2,4,6,7,9,12,1,3,5,45]:
    ter.root = ter.insert(ter.root,i)
# ca = dict(sorted([13,5,15,2]))
ca = {"1":15,"2":13}
ca = dict(sorted(ca.items(),key= lambda x : x[::-1]))
for i in ca.items():
    print(list(i))

ter.printTree(ter.root)