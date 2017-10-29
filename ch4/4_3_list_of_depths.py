import unittest

class node():
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

def solution(root):
    res = []
    queue = []
    queue.append(root)

    while queue:
        numberOfNodesInThisLevel = len(queue)
        level = [queue.pop() for _ in range(numberOfNodesInThisLevel)]
        res.append(level)
        for n in level:
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)
    
    for level in res:
        print(*[n.value for n in level])

    return res

class Test(unittest.TestCase):
    tree_1 = node(1)
    tree_1.left = node(2)
    tree_1.right = node(3)
    tree_1.left.left = node(4)
    tree_1.left.right = node(5)
    tree_1.right.left = node(6)
    tree_1.right.right = node(7)

    def testTree1(self):
        solution(self.tree_1)

if __name__ == "__main__":
    unittest.main()
