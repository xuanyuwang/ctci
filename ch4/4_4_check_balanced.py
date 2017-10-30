import unittest

class node():
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


def solution(root):
    if not root:
        return 0

    leftHeight = solution(root.left)
    rightHeight = solution(root.right)
    if leftHeight != -1 and rightHeight != -1 and abs(leftHeight - rightHeight) <= 1:
        return max(leftHeight, rightHeight) + 1
    else:
        return -1

class Test(unittest.TestCase):
    tree_1 = node(1)
    tree_1.left = node(2)
    tree_1.left.left = node(4)

    tree_2 = node(1)
    tree_2.left = node(2)
    tree_2.right = node(3)
    tree_2.left.left = node(4)

    def testTree1(self):
        answer = solution(self.tree_1)
        self.assertEqual(answer, -1)

    def testTree2(self):
        answer = solution(self.tree_2)
        self.assertTrue(answer > -1)

if __name__ == "__main__":
    unittest.main()

