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

    def search(self, value):
        if self.data == value:
            return True

        if value < self.data:
            # Value might be in left subtree; Recursion
            if self.left:
                return self.left.search(value)
            else: 
                return False

        if value > self.data:
            # Value might be in left subtree; Recursion
            if self.right:
                return self.right.search(value)
            else: 
                return False

    # Activity Exercise 1: (1) Find minimum element in entire binary tree
    def findMinimum(self):
        if self.left is None:
            return self.data
        return self.left.findMinimum()

    # Activity Exercise 1: (2) Find maximum element in entire binary tree
    def findMaximum(self):
        if self.right is None:
            return self.data
        return self.right.findMaximum()

def buildTree(elements):
    # Assigned first element as a root node
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.addChild(elements[i])

    return root

if __name__ == '__main__':
    numbers = [18, 5, 2, 21, 10, 24, 19, 35]
    numbersTree = buildTree(numbers)

    # Checking
    print("—" * 48)
    print("Checking:")

    # for traversal
    print("In Ordered List: ", numbersTree.inOrderTraversal()) 

    # for search
    print("Is 10 in the list?", numbersTree.search(10)) 
    print("Is 15 in the list?", numbersTree.search(15)) 
    print("—" * 48)


    # EXERCISE 1 from first YouTube Video
    # (1) Find minimum element in entire binary tree
    print('Minimum:', numbersTree.findMinimum())

    # (2) Find maximum element in entire binary tree
    print('Maximum:', numbersTree.findMaximum())

    # 3

    # 4

    # 5




