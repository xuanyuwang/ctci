import unittest

def merge(arrayA, arrayB, k):
    """ As A has enough buffer to store all numbers of B, we need
        to use k to indicate the end of A.
        i is used to indicate the tail of A's unsorted numbers.
        j is used to indicate the tail of B's unsorted numbers.
        tail is the tail of the result.
    """
    N = len(arrayA)
    i = k - 1
    j = len(arrayB) - 1
    tail = N - 1

    while i >= 0 and j >= 0:
        if arrayA[i] > arrayB[j]:
            arrayA[tail] = arrayA[i]
            i -= 1
        else:
            arrayA[tail] = arrayB[j]
            j -= 1
        tail -= 1

    if i < 0 and j < 0:
        return arrayA[-(len(arrayB) + k):]

    if i < 0 and j >= 0:
        arrayA[tail - j: tail + 1] = arrayB[:j+1]
        return arrayA[-(len(arrayB) + k):]

    if i >= 0 and j < 0:
        arrayA[tail - i: tail + 1] = arrayA[:i + 1]
        return arrayA[-(len(arrayB) + k):]

class Test(unittest.TestCase):
    def testA(self):
        """ All numbers in B are bigger than A"""
        arrayA = list(range(10))
        arrayB = list(range(6,8))
        arrayA = merge(arrayA, arrayB, 3)
        self.assertEqual(arrayA, [0,1,2,6,7])

    def testB(self):
        arrayA = [6,7,8,0,0,0,0,0,0]
        arrayB = [0,1,2]
        arrayA = merge(arrayA, arrayB, 3)
        self.assertEqual(arrayA, [0,1,2,6,7,8])

    def testC(self):
        arrayA = [3,7,9,0,0,0,0,0,0]
        arrayB = [2,4,8]
        arrayA = merge(arrayA, arrayB, 3)
        self.assertEqual(arrayA, [2,3,4,7,8,9])


if __name__ == "__main__":
    unittest.main()
