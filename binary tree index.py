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
        # Returns a list of elements in a specific order
        elements = []

        # Visit left node
        if self.left:
            elements += self.left.inOrderTraversal()

        # Visit base node
        elements.append(self.data)

        # Visit right node
        if self.right:  
            elements += self.right.inOrderTraversal()
        
        return elements 

if __name__ == 'main':
    numbers = [18, 5, 2, 21, 10, 24, 19, 35]


