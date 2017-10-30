import unittest

class node():
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def insert(root, value):
    if root is None:
        return node(value)
    else:
        if value <= root.value:
            temp = insert(root.left, value)
            root.left = temp
            temp.parent = root 
        else:
            temp = insert(root.right, value)
            root.right = temp
            temp.parent = root 

    return root

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.value)
        inOrder(root.right)

def leftMostChild(root):
    while root.left != None:
        root = root.left
    return root

def solution(root, givenNode):
    if givenNode.right is not None:
        return leftMostChild(givenNode.right)

    p = givenNode.parent
    while(p is not None):
        if givenNode != p.right:
            break
        givenNode = p
        p = p.parent
    return p

class Test(unittest.TestCase):
    tree = None
    tree = insert(tree, 3)
    tree = insert(tree, 1)
    tree = insert(tree, 2)
    tree = insert(tree, 4)
    tree = insert(tree, 5)

    def test1(self):
        answer = solution(tree, tree)
        self.assertTrue(answer.value, 4)

    def test2(self):
        answer = solution(tree, tree.left)
        self.assertTrue(answer.value, 2)

    def test3(self):
        answer = solution(tree, tree.right)
        self.assertTrue(answer.value, 5)


if __name__ == "__main__":
    tree = None
    tree = insert(tree, 3)
    tree = insert(tree, 1)
    tree = insert(tree, 2)
    tree = insert(tree, 4)
    tree = insert(tree, 5)
    
    inOrder(tree)
    unittest.main()
