#BST tree implementation
#BST is a data structure that allows you to store data in a tree-like structure
def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
        return root

def search(root, data):
    if root is None:
        return False
    else:
        if data == root.data:
            return True
        elif data < root.data:
            return search(root.left, data)
        else:
            return search(root.right, data)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)
#test cases

#create a test with 1 million elements and search for 100 items and return the time it takes
def test_bst():
    root = None
    for i in range(996):
        root = insert(root, i)
    for i in range(10):
        search(root, i)

    print("All test cases passed!")
import datetime
print(datetime.datetime.now())
test_bst()
print(datetime.datetime.now())
