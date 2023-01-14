# Name: Jerico James F. Viteño
# Laboratory Exercise 5: Binary Tree
# January 14, 2023

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self, data):
        if data == self.data:
            return 
            # Status: Node Exist
        
        if data < self.data:
            # Add: Data in left subtree
            if self.left:
                self.left.addChild(data)
            else:
                self.left = BinarySearchTreeNode(data)
        
        else:
            # Add: Data in right subtree
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def inOrderTraversal(self):
        elements = []
        
        return elements
        
