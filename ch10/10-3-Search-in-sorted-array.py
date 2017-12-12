import unittest

def isInThisSection(section, key):
    start = section[0]
    end = section[-1]
    
    if start >= end:
        if key > end and key < start:
            return False
        if key >= start or key <= end:
            return True

    if start <= end:
        if key >= start and key <= end:
            return True
        else:
            return False

def solution(array, key, low, high):
    if key == array[low]:
        return low
    if key == array[high]:
        return high

    mid = low + (high - low) // 2
    if isInThisSection(array[low:mid+1], key):
        return solution(array, key, low, mid)
    else:
        return solution(array, key, mid, high)

class Test(unittest.TestCase):
    array = [15,16,19,20,25,1,3,4,5,7,10,14]
    def testA(self):
        answer = solution(self.array, 5, 0, len(self.array)-1)
        self.assertEqual(answer, 8)

    def testB(self):
        answer = solution(self.array, 16, 0, len(self.array)-1)
        self.assertEqual(answer, 1)

    def testC(self):
        answer = solution(self.array, 7, 0, len(self.array)-1)
        self.assertEqual(answer, 9)

if __name__ == "__main__":
    unittest.main()
