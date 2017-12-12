import unittest
from collections import Counter

class Node():
    code = ''
    value = None
    weight = None
    leftChild = None
    rightChild = None
    parent = None
    depth = 0

    def __init__(self, value=None, freq=None,
            leftChild=None, rightChild=None, parent=None):
        self.value = value
        self.weight = freq
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.parent = parent

    def isLeaf(self):
        return (not (self.leftChild or self.rightChild))

    def isRoot(self):
        return (not self.parent)

    def asLeftChildOf(self, parentNode):
        self.parent = parentNode
        self.depth = parentNode.depth + 1
        parentNode.leftChild = self

    def asRightChildOf(self, parentNode):
        self.parent = parentNode
        self.depth = parentNode.depth + 1
        parentNode.rightChild = self

    def bfs(self):
        totalNode = [self]
        nextLevel = [e for e in [self.leftChild, self.rightChild] if e]
        while len(nextLevel) > 0:
            currentlevel = nextLevel
            totalNode += nextLevel
            nextLevel = []
            for e in currentlevel:
                if e.leftChild:
                    nextLevel.append(e.leftChild)
                if e.rightChild:
                    nextLevel.append(e.rightChild)
        return totalNode

    def compareTree(self, anotherNode):
        nodeList = self.bfs()
        anotherNodeList = anotherNode.bfs()
        if len(nodeList) == len(anotherNodeList):
            if all([i.value == j.value for i, j in zip(nodeList, anotherNodeList)]):
                return True
        return False

    def compareNode(self, anotherNode):
        return anotherNode and self.value == anotherNode.value

    def isLeftChild(self):
        if (not self.parent):
            return False
        else:
            if self.compareNode(self.parent.leftChild):
                return True
            else:
                return False

    def isRightChild(self):
        if (not self.parent):
            return False
        else:
            if self.compareNode(self.parent.rightChild):
                return True
            else:
                return False

    def zig(self):
        root = self
        if root.isLeaf():
            return root
        else:
            tempRootParent = root.parent
            tempLrChild = root.leftChild.rightChild

            if root.isRoot():
                root.leftChild.parent = tempRootParent
            elif root.isLeftChild():
                root.leftChild.asLeftChildOf(tempRootParent)
            elif root.isRightChild():
                root.leftChild.asRightChildOf(tempRootParent)

            root.asRightChildOf(root.leftChild)
            if tempLrChild:
                tempLrChild.asLeftChildOf(root)
            else:
                root.leftChild = None


            newRoot = root.parent
            return newRoot

    def zag(self):
        root = self
        if root.isLeaf():
            return root
        else:
            tempRootParent = root.parent
            tempRlChild = root.rightChild.leftChild

            if root.isRoot():
                root.rightChild.parent = tempRootParent
            elif root.isLeftChild():
                root.rightChild.asLeftChildOf(tempRootParent)
            elif root.isRightChild():
                root.rightChild.asRightChildOf(tempRootParent)

            root.asLeftChildOf(root.rightChild)
            if tempRlChild:
                tempRlChild.asRightChildOf(root)
            else:
                root.rightChild = None


            newRoot = root.parent
            return newRoot

    def zigzig(self):
        root = self
        root = root.zig()
        root = root.zig()
        return root

    def zagzag(self):
        root = self
        root = root.zag()
        root = root.zag()
        return root

    def zigzag(self):
        root = self
        root.leftChild = root.leftChild.zag()
        newRoot = root.zig()
        return newRoot

    def zagzig(self):
        root = self
        root.rightChild = root.rightChild.zig()
        newRoot = root.zag()
        return newRoot

    def __repr__(self):
        return "{} : {}, {}\n".format(self.value, self.code, self.weight)

    def __str__(self):
        return "{} : {}, {}\n".format(self.value, self.code, self.weight)


class Test(unittest.TestCase):

    def testBsf(self):
        y = Node(value='y')
        x = Node(value='x')
        A = Node(value='A')
        B = Node(value='B')
        C = Node(value='C')
        A.asLeftChildOf(x)
        B.asRightChildOf(x)
        x.asLeftChildOf(y)
        C.asRightChildOf(y)

        answer = [y, x, C, A, B]

        self.assertEqual(y.bfs(), answer)

    def testCompare(self):
        y = Node(value='y')
        x = Node(value='x')
        A = Node(value='A')
        B = Node(value='B')
        C = Node(value='C')
        A.asLeftChildOf(x)
        B.asRightChildOf(x)
        x.asLeftChildOf(y)
        C.asRightChildOf(y)
        self.assertEqual(y.compareTree(y), True)

    def testZig(self):
        y = Node(value='y')
        x = Node(value='x')
        A = Node(value='A')
        B = Node(value='B')
        C = Node(value='C')
        A.asLeftChildOf(x)
        B.asRightChildOf(x)
        x.asLeftChildOf(y)
        C.asRightChildOf(y)

        y2 = Node(value='y')
        x2 = Node(value='x')
        C2 = Node(value='C')
        A2 = Node(value='A')
        B2 = Node(value='B')
        B2.asLeftChildOf(y2)
        C2.asRightChildOf(y2)
        y2.asRightChildOf(x2)
        A2.asLeftChildOf(x2)

        answer = y.zig()
        self.assertTrue(answer.compareTree(x2))

    def testZag(self):
        y = Node(value='y')
        x = Node(value='x')
        A = Node(value='A')
        B = Node(value='B')
        C = Node(value='C')
        A.asLeftChildOf(x)
        B.asRightChildOf(x)
        x.asLeftChildOf(y)
        C.asRightChildOf(y)

        y2 = Node(value='y')
        x2 = Node(value='x')
        C2 = Node(value='C')
        A2 = Node(value='A')
        B2 = Node(value='B')
        B2.asLeftChildOf(y2)
        C2.asRightChildOf(y2)
        y2.asRightChildOf(x2)
        A2.asLeftChildOf(x2)

        answer = x2.zag()
        self.assertTrue(answer.compareTree(y))

    def testZigZig(self):
        y = Node(value='y')
        x = Node(value='x')
        z = Node(value='z')
        C = Node(value='C')
        A = Node(value='A')
        B = Node(value='B')
        D = Node(value='D')

        y2 = Node(value='y')
        x2 = Node(value='x')
        z2 = Node(value='z')
        C2 = Node(value='C')
        A2 = Node(value='A')
        B2 = Node(value='B')
        D2 = Node(value='D')

        A.asLeftChildOf(x)
        B.asRightChildOf(x)
        x.asLeftChildOf(y)
        C.asRightChildOf(y)
        y.asLeftChildOf(z)
        D.asRightChildOf(z)

        C2.asLeftChildOf(z2)
        D2.asRightChildOf(z2)
        z2.asRightChildOf(y2)
        B2.asLeftChildOf(y2)
        A2.asLeftChildOf(x2)
        y2.asRightChildOf(x2)

        answer = z.zigzig()
        self.assertTrue(answer.compareTree(x2))

    def testZagZag(self):
        y = Node(value='y')
        x = Node(value='x')
        z = Node(value='z')
        C = Node(value='C')
        A = Node(value='A')
        B = Node(value='B')
        D = Node(value='D')

        y2 = Node(value='y')
        x2 = Node(value='x')
        z2 = Node(value='z')
        C2 = Node(value='C')
        A2 = Node(value='A')
        B2 = Node(value='B')
        D2 = Node(value='D')

        A.asLeftChildOf(x)
        B.asRightChildOf(x)
        x.asLeftChildOf(y)
        C.asRightChildOf(y)
        y.asLeftChildOf(z)
        D.asRightChildOf(z)

        C2.asLeftChildOf(z2)
        D2.asRightChildOf(z2)
        z2.asRightChildOf(y2)
        B2.asLeftChildOf(y2)
        A2.asLeftChildOf(x2)
        y2.asRightChildOf(x2)

        answer = x2.zagzag()
        self.assertTrue(answer.compareTree(z))

    def testZigzag(self):
        y = Node(value='y')
        x = Node(value='x')
        z = Node(value='z')
        C = Node(value='C')
        A = Node(value='A')
        B = Node(value='B')
        D = Node(value='D')

        y2 = Node(value='y')
        x2 = Node(value='x')
        z2 = Node(value='z')
        C2 = Node(value='C')
        A2 = Node(value='A')
        B2 = Node(value='B')
        D2 = Node(value='D')
        B.asLeftChildOf(x)
        C.asRightChildOf(x)
        A.asLeftChildOf(y)
        x.asRightChildOf(y)
        y.asLeftChildOf(z)
        D.asRightChildOf(z)

        A2.asLeftChildOf(y2)
        B2.asRightChildOf(y2)
        C2.asLeftChildOf(z2)
        D2.asRightChildOf(z2)
        y2.asLeftChildOf(x2)
        z2.asRightChildOf(x2)

        answer = z.zigzag()
        self.assertTrue(answer.compareTree(x2))

if __name__ == '__main__':
    unittest.main()
