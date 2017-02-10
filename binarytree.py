class BinaryTree(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BinaryTree(value)
                else:
                    self.left.insert(value)
            else:
                if self.right is None:
                    self.right = BinaryTree(value)
                else:
                    self.right.insert(value)

        else:
            self.value = value

    def printInOrder(self):
        if self.left:
            self.left.printInOrder()
        print self.value
        if self.right:
            self.right.printInOrder()

    def printPreOrder(self):
        print self.value
        if self.left:
            self.left.printPreOrder()
        if self.right:
            self.right.printPreOrder()

    def printPostOrder(self):
        if self.left:
            self.left.printPostOrder()
        if self.right:
            self.right.printPostOrder()
        print self.value

if __name__ == "__main__":
    root = BinaryTree('F')
    root.insert('B')
    root.insert('G')
    root.insert('A')
    root.insert('D')
    root.insert('I')
    root.insert('C')
    root.insert('E')
    root.insert('H')
    root.printInOrder()
    print("#"*20)
    root.printPreOrder()
    print("#"*20)
    root.printPostOrder()
