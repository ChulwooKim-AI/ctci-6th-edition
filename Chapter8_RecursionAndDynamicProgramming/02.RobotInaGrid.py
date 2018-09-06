"""Robot in a Grid

Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits" such that
the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
the bottom right.

Hints: 
#331
For the robot to reach the last cell, it must find a path to the second-to-last cells. For it to
find a path to the second-to-last cells, it must find a path to the third-to-last cells.
#360
Simplify this problem a bit by first figuring out if there's a path. Then, modify your algorithm
to track the path.
#388
Think again about the efficiency of your algorithm. Can you optimize it?
"""

import unittest

def find_path(grid):
    if grid is None:
        return None
    path = list()
    if __find_path(len(grid)-1, len(grid[0])-1, grid, path):
        return path
    return None

def __find_path(row, col, grid, path):        
    if row < 0 or col < 0 or grid[row][col] == -1:    
        return False    
    if (row == 0 and col == 0) or __find_path(row-1, col, grid, path) or __find_path(row, col-1, grid, path):        
        path.append((row, col))
        return True

'''Extra work: find all paths of grid

If it uses pre-order, it is possible to find all paths in grid.
Note that coordinate to insert in base condition should be sum of row and column to store it as each path 
because pre-order accumulates all paths.

'''
def find_all_paths(grid):
    return __find_all_paths(0, 0, grid, path=[], result=[])

def __find_all_paths(row, col, grid, path, result):    
    if row == len(grid)-1:
        temp = path.copy()
        for i in range(col, len(grid[0])):            
            temp.insert(row+i, (row, i))            
        result.append(temp[:len(grid)+len(grid[0])-1])        
        return
    if col == len(grid[0])-1:
        temp = path.copy()
        for i in range(row, len(grid)):
            temp.insert(col+i, (i, col))
        result.append(temp[:len(grid)+len(grid[0])-1])        
        return
    path.insert(row+col, (row, col))
    if grid[row+1][col] != -1:
        __find_all_paths(row+1, col, grid, path, result)
    if grid[row][col+1] != -1:
        __find_all_paths(row, col+1, grid, path, result)
    return result
    

class Test(unittest.TestCase):
    def setUp(self):
        self.grid = [[0, -1, 0], [0, 0, 0], [-1, 0, 0]]
        
    def test_find_path(self):
        self.assertListEqual(find_path(self.grid), [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)])

    def test_find_all_paths(self):            
        self.assertListEqual(find_all_paths(self.grid), [[(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)], 
                                                        [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]])
        
if __name__ == "__main__":
    unittest.main()