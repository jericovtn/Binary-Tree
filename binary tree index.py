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

    # Part 1 | Exercise : (4) Performs post order traversal of binary tree
    def postOrderTraversal(self):
        elements = []

        # Visit left node
        if self.left:
            elements += self.left.postOrderTraversal()

        # Visit right node
        if self.right:
            elements += self.right.postOrderTraversal()

        # Visit base node
        elements.append(self.data) 
        
        return elements

    # Part 1 | Exercise : (5) Performs pre order traversal of binary tree
    def preOrderTraversal(self):
        elements = [self.data]

        # Visit left node
        if self.left:
            elements += self.left.preOrderTraversal()
        
        # Visit right node
        if self.right:
            elements += self.right.preOrderTraversal()

        return elements

    # Part 1 | Exercise: (1) Find minimum element in entire binary tree
    def minimum(self):
        if self.left is None:
            return self.data
        return self.left.minimum()

    # Part 1 | Exercise: (2) Find maximum element in entire binary tree
    def maximum(self):
        if self.right is None:
            return self.data
        return self.right.maximum()

    # Part 1 | Exercise: (3) Calculate sum of all elements
    def sum(self):
        leftSum = self.left.sum() if self.left else 0
        rightSum = self.right.sum() if self.right else 0
        return self.data + leftSum + rightSum

    # Part 2 | Exercise: Modify delete method and remove the following given
    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right

            maximumValue = self.left.maximum()
            self.data = maximumValue
            self.left = self.left.delete(maximumValue)
        
        return self

def buildTree(elements):
    print("—" * 54)
    print("\n⚪ Building tree with these elements:\n", elements, "\n")
    # Assigned first element as a root node
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.addChild(elements[i])

    return root

if __name__ == '__main__':
    numbers = [18, 5, 2, 21, 10, 24, 19, 35]
    numbersTree = buildTree(numbers)

    # —————————————————————————————————————————————————————————————
    # Checking from YouTube Tutorial
    print("—" * 54)
    print("⚪ Checking:")

    # for traversal
    print("\nIn Ordered Traversal: ", numbersTree.inOrderTraversal()) 

    # for search
    print("Is 10 in the list?", numbersTree.search(10)) 
    print("Is 15 in the list?", numbersTree.search(15)) 
    print("—" * 54)

    # —————————————————————————————————————————————————————————————
    # Part 1 | EXERCISE from first YouTube Video
    print("⚪ Part 1 | Exercise:")

    # (1) Find minimum element in entire binary tree
    print('\nMinimum:', numbersTree.minimum())

    # (2) Find maximum element in entire binary tree
    print('Maximum:', numbersTree.maximum())

    # (3) Calculate sum of all elements
    print("Sum:", numbersTree.sum())

    # (4) Performs post order traversal of binary tree
    print("Post Order Traversal:", numbersTree.postOrderTraversal())

    # (5) Performs pre order traversal of binary tree
    print("Pre order traversal:", numbersTree.preOrderTraversal())
    print("—" * 54)

    # —————————————————————————————————————————————————————————————
    # Part 2 | EXERCISE from second YouTube Video
    print("⚪ Part 2 | Exercise:")

    # (1) Deleting number 5
    numbersTree.delete(5)
    print("\nNumber 5 was successfully deleted. \nUpdated List:", numbersTree.inOrderTraversal())

    # (2) Deleting number 10
    numbersTree.delete(10)
    print("\nNumber 10 was successfully deleted. \nUpdated List:", numbersTree.inOrderTraversal())

    # (3) Deleting number 35
    numbersTree.delete(35)
    print("\nNumber 5 was successfully deleted. \nUpdated List:", numbersTree.inOrderTraversal())
    print("—" * 54)





