import unittest
import math

class node():
    def __init__(self,value=None):
        self.left = None
        self.right = None
        self.value = value 

def recursionSol(array):
    # Base case
    if len(array) == 0:
        return None
    
    if len(array) % 2 == 0:
        mid = int(len(array) / 2 - 1)
    else:
        mid = int(math.floor(len(array) / 2)) 

    root = node(array[mid])
    root.left = recursionSol(array[:mid])
    root.right = recursionSol(array[mid + 1:])
    return root

def maxDepth(root):
    if root == None:
        return 0
    else:
        return 1 + max(maxDepth(root.left), maxDepth(root.right))

class Test(unittest.TestCase):
    """
    For a array of N elements, there will be ceil(log2(N + 1)) levels
    """
    caseEven = [1,2,3,4,5,6,7,8,9,10]
    caseEvenT = 4 

    caseOdd = [1,2,3,4,5,6,7,8,9]
    caseOddT = 4

    def testCaseEven(self):
        answer = maxDepth(recursionSol(self.caseEven))
        self.assertEqual(answer, self.caseEvenT)

    def testCaseOdd(self):
        answer = maxDepth(recursionSol(self.caseOdd))
        self.assertEqual(answer, self.caseOddT)

if __name__ == "__main__":
    unittest.main()
