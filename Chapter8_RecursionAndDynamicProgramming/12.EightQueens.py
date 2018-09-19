"""Eight Queens

Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board
so that none of them share the same row, column, or diagonal. In this case, "diagonal" means all
diagonals, not just the two that bisect the board.

Hints:
# 308
We know that each row must have a queen. Can you try all possibilities?
# 350
Each row must have a queen. Start with the last row. There are eight different columns
on which you can put a queen. Can you try each of these?
# 371
Break this down into smaller subproblems. The queen at row 8 must be at column 1, 2,
3,4,5, 6,7, or 8. Can you print all ways of placing eight queens where a queen is at row
8 and column 3? You then need to check all the ways of placing a queen on row 7.
"""


def arrange_queens(number):
    results = list()
    __arrange_queens(number, 0, list(), results)
    return results


def __arrange_queens(number, target_row, positions, results):
    if number == target_row:        
        results.append(positions)
    else:    
        for column in range(number):        
            if is_right_place(target_row, column, positions):
                temp = positions.copy()
                temp.append((target_row, column))            
                __arrange_queens(number, target_row+1, temp, results)


def is_right_place(new_row, new_col, positions):
    for row, col in positions:
        if col == new_col:
            return False
        elif (row-col == new_row-new_col) or (row+col == new_row+new_col):
            return False
    return True


import unittest

class Test(unittest.TestCase):
    def test_arrange_queens(self):        
        self.assertEqual(len(arrange_queens(8)), 92)
        self.assertListEqual(arrange_queens(4), [[(0, 1), (1, 3), (2, 0), (3, 2)], 
                                                [(0, 2), (1, 0), (2, 3), (3, 1)]])
                

if __name__ == "__main__":
    unittest.main()
