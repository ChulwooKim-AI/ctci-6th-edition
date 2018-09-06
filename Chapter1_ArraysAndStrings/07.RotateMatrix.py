"""Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

"""

"""
 1  2  3  4
 5  6  7  8
 9 10 11 12
13 14 15 16

13  9  5  1
14 10  6  2
15 11  7  3
16 12  8  4

(0,0) (0,1) (0,2) (0,3) > (0,3) (1,3) (2,3) (3,3)
(1,0) (1,1) (1,2) (1,3) > (0,2) (1,2) (2,2) (3,2)
matrix[row][col] > rotatedMatrix[col][len(matrix)-row]
"""

def rotateMatrix(matrix):
    tempLayer = [[None for i in range(len(matrix))] for j in range(len(matrix))]
    
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            tempLayer[col][len(matrix)-row-1] = matrix[row][col]
    return tempLayer

"""
 1  2  3  4
 5  6  7  8
 9 10 11 12
13 14 15 16

13  9  5  1
14 10  6  2
15 11  7  3
16 12  8  4

(0,0) > (0,3), (0,3) > (3,3), (3,3) > (3,0), (3,0) > (0,0)
(0,1) > (1,3), (1,3) > (3,2), (3,2) > (2,0), (2,0) > (0,1)
matrix[row][col] > matrix[col][len(matrix)-row-1]
matrix[col][len(matrix)-row-1] > matrix[len(matrix)-row-1][len(matrix)-col-1]
matrix[len(matrix)-row-1][len(matrix)-col-1] > matrix[len(matrix)-col-1][row]
matrix[len(matrix)-col-1][row] > matrix[row][col]
"""
def rotateMatrixInPlace(matrix):
    temp1 = 0
    temp2 = 0
    n = len(matrix)
    for row in range(n//2):
        for col in range(row, n-row-1):
            temp1 = matrix[col][n-row-1]
            matrix[col][n-row-1] = matrix[row][col]
            temp2 = matrix[n-row-1][n-col-1]
            matrix[n-row-1][n-col-1] = temp1
            temp1 = matrix[n-col-1][row]
            matrix[n-col-1][row] = temp2
            matrix[row][col] = temp1
            
    return matrix

if __name__ == "__main__":
    print(rotateMatrixInPlace([[1,2,3], [4,5,6], [7,8,9]]))