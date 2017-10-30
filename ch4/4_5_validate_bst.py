import unittest
from math import inf
from math import isinf

class node():
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


def solution(root):
    if not root:
        return -inf

    leftMax = solution(root.left)
    rightMax = solution(root.right)
    if leftMax != inf and rightMax != inf and(leftMax < root.value) and (rightMax == -inf or root.value < rightMax):
        return max(leftMax, rightMax, root.value)
    else:
        return inf


class Test(unittest.TestCase):
    tree_1 = node(1)
    tree_1.left = node(4)
    tree_1.left.left = node(2)

    tree_2 = node(1)
    tree_2.left = node(0)
    tree_2.right = node(3)
    tree_2.right.right = node(4)

    def testTree1(self):
        answer = solution(self.tree_1)
        self.assertTrue(isinf(answer))

    def testTree2(self):
        answer = solution(self.tree_2)
        self.assertFalse(isinf(answer))

if __name__ == "__main__":
    unittest.main()
