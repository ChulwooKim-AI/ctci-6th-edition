"""Sorted Matrix Search

Given an M x N matrix in which each row and each column is sorted in
ascending order, write a method to find an element.

Hints: 
#193
Start with a naive solution. (But hopefully not too naive. You should be able to use the
fact that the matrix is sorted.)
#211
We can do a binary search in each row. How long will this take? How can we do better?
#229
If you're considering a particular column, is there a way to quickly eliminate it (in some
cases at least)?
#251
Since each column is sorted, you know that the value can't be in this column if it's
smaller than the min value in this column. What else does this tell you?
#266
If the value x is smaller than the start of the column, then it also can't be in any columns
to the right.
#279
Think about the previous hint in the context of rows.
#288
What would happen if we tried to keep track of this using an array? What are the pros
and cons of this?
#291
Can we use the previous hints to move up, down, left, and right around the rows and
columns?
#303
Another way to think about this is that if you drew a rectangle around a cell extending
to the bottom, right coordinate of the matrix, the cell would be bigger than all the items
in this square.
#317
A cell will be larger than all the items below it and to the right. It will be smaller than all
cells above it and to the left. If we wanted to eliminate the most elements first, which
element should we compare the value x to?
#330
If we compare x to the center element in the matrix, we can eliminate roughly one
quarter of the elements in the matrix.
"""

'''Method 1

This solution uses binary search.

Time complexity : O(M*logN)
'''

def search_matrix(matrix, number):
    for row in range(len(matrix)):
        if binary_search(matrix[row], number):
            return True
    return False

def binary_search(array, number):
    first = 0
    last = len(array) - 1
    result = False
    while first <= last and not result:    
        mid = (first + last) // 2
        if number == array[mid]:
            result = True
        else:
            if number < array[mid]:
                last = mid - 1
            elif number > array[mid]:
                first = mid + 1        
    return result

'''Method 2

This solution compares matrix elements with target number by moving down and left.

Time complexity : O(M*N)
'''

def search_matrix_by_moving(matrix, number):
    row = 0
    column = len(matrix[0]) - 1
    while row < len(matrix) and column >= 0:
        if number > matrix[row][column]:
            row += 1
        elif number < matrix[row][column]:
            column -= 1
        else:
            return True
    return False


'''Method 3

This is a solution using binary search based on diagonal movement
1. Set start to start of diagonal and end to the end of the diagonal. 
   Since the grid may not be square, the end of the diagonal may not equal dest.
2. Do binary search on the diagonal, looking for the first element greater than element
3. Split the grid into quadrants. Search the bottom left and the top right.

Time complexity : O(N+M)
'''

class Coordinate:
    def __init__(self, row, column):
        self.row = row
        self.column = column
    
    def inbounds(self, matrix):
        return self.row >= 0 and self.column >= 0 and \
            self.row < len(matrix) and self.column < len(matrix[0])
    
    def is_before(self, pivot):
        return self.row <= pivot.row and self.column <= pivot.column
    
    def set_to_average(self, min, max):
        self.row = (min.row + max.row) // 2
        self.column = (min.column + max.column) // 2
    
    def clone(self):
        return Coordinate(self.row, self.column)

def find_element(matrix, element):
    origin = Coordinate(0, 0)
    destination = Coordinate(len(matrix)-1, len(matrix[0])-1)
    return __find_element(matrix, origin, destination, element)

def __find_element(matrix, origin, destination, element):
    if not origin.inbounds(matrix) or not destination.inbounds(matrix):
        return False
    if matrix[origin.row][origin.column] == element:
        return True
    elif not origin.is_before(destination):
        return False
    start = origin.clone()
    diagonal_distance = min(destination.row - origin.row, destination.column - origin.column)
    end = Coordinate(start.row + diagonal_distance, start.column + diagonal_distance)
    pivot = Coordinate(0, 0)
    while start.is_before(end):
        pivot.set_to_average(start, end)
        if element > matrix[pivot.row][pivot.column]:
            start.row = pivot.row + 1
            start.column = pivot.column + 1
        else:
            end.row = pivot.row - 1
            end.column = pivot.column - 1
    return partition_and_search(matrix, origin, destination, start, element)

def partition_and_search(matrix, origin, destination, pivot, element):
    lower_left_origin = Coordinate(pivot.row, origin.column)
    lower_left_destination = Coordinate(destination.row, pivot.column - 1)
    upper_right_origin = Coordinate(origin.row, pivot.column)
    upper_right_destination = Coordinate(pivot.row - 1, destination.column)
    
    lower_left = __find_element(matrix, lower_left_origin, lower_left_destination, element)
    if not lower_left:
        return __find_element(matrix, upper_right_origin, upper_right_destination, element)
    return lower_left


import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.matrix = [[1,  2,  3,  4,  5,  6,  7,  8,  9],
                    [5,  10, 15, 20, 25, 30, 35, 40, 45],
                    [10, 20, 30, 40, 50, 60, 70, 80, 90],
                    [13, 23, 33, 43, 53, 63, 73, 83, 93],
                    [14, 24, 34, 44, 54, 64, 74, 84, 94],
                    [15, 25, 35, 45, 55, 65, 75, 85, 95],
                    [16, 26, 36, 46, 56, 66, 77, 88, 99]]
    
    def test_sorted_matrix_search(self):    
        self.assertTrue(search_matrix(self.matrix, 65))
        self.assertTrue(search_matrix(self.matrix, 94))
        self.assertTrue(search_matrix(self.matrix, 13))
        self.assertFalse(search_matrix(self.matrix, 67))

    def test_sorted_matrix_search_by_moving(self):    
        self.assertTrue(search_matrix_by_moving(self.matrix, 65))
        self.assertTrue(search_matrix_by_moving(self.matrix, 94))
        self.assertTrue(search_matrix_by_moving(self.matrix, 1))
        self.assertFalse(search_matrix_by_moving(self.matrix, 67))

    def test_find_element(self):
        self.assertTrue(find_element(self.matrix, 65))
        self.assertTrue(find_element(self.matrix, 94))
        self.assertTrue(find_element(self.matrix, 1))
        self.assertFalse(find_element(self.matrix, 67))


if __name__ == "__main__":
  unittest.main()