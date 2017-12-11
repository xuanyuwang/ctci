from itertools import product
import unittest
from node import *

def solution(tree):
    print(tree.value)
    if tree.isLeaf():
        print(tree.value, "is leaf")
        return [[tree.value]]

    if tree.leftChild and tree.rightChild:
        print(tree.value, "has left child & right child")
        ls = solution(tree.leftChild)
        rs = solution(tree.rightChild)
        pd = product(ls, rs)
        res = []
        for e in pd:
            res.append([tree.value] + e[0] + e[1])
            res.append([tree.value] + e[1] + e[0])
        return res

    if tree.leftChild and not tree.rightChild:
        print(tree.value, "has left child & ! right child")
        res = []
        ls = solution(tree.leftChild)
        res = []
        for e in ls:
            res.append([tree.value] + e)
        return res

    if tree.rightChild and not tree.leftChild:
        print(tree.value, "has ! left child & right child")
        res = []
        rs = solution(tree.rightChild)
        res = []
        for e in rs:
            res.append([tree.value] + e)
        return res

class Test(unittest.TestCase):
    def testSingleNode(self):
        root = Node(value=3)
        answer = solution(root)
        self.assertEqual(answer, [[3]])

    def testMiniTree(self):
        root = Node(value=2)
        l = Node(value=1)
        r = Node(value=3)
        r.asRightChildOf(root)
        l.asLeftChildOf(root)
        answer = solution(root)
        self.assertEqual(answer, [[2,1,3], [2,3,1]])
        

if __name__ == "__main__":
    unittest.main()
