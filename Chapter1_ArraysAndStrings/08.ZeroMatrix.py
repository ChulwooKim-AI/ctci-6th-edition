"""Zero Matrix

Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to O.
"""
def makeZero(row, col, result):
    n = len(result)
    for rowInResult in range(n):
        for colInResult in range(len(result[0])):
            if row == rowInResult or col == colInResult:
                result[rowInResult][colInResult] = 0
    return result

def checkZero(matrix):
    n = len(matrix)
    result = [[None for x in range(len(matrix[0]))] for x in range(n)]

    for row in range(n):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                result = makeZero(row, col, result)
    for row in range(n):
        for col in range(len(matrix[0])):
            if result[row][col] == None:
                result[row][col] = matrix[row][col]
    return result

import unittest
class Test(unittest.TestCase):
    def test_checkZero(self):
        matrix = [[1,2,3,4], [9,0,3,2], [8,7,0,1], [9,8,4,3],[1,2,3,4]]
        result = [[1,0,0,4], [0,0,0,0], [0,0,0,0], [9,0,0,3],[1,0,0,4]]
        self.assertEqual(checkZero(matrix), result)

if __name__ == '__main__':
    unittest.main()
    