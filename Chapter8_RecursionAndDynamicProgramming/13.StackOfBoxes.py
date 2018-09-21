"""Stack of Boxes

You have a stack of n boxes, with widths W_i, heights h_i, and depths d_i. The boxes
cannot be rotated and can only be stacked on top of one another if each box in the stack is strictly
larger than the box above it in width, height, and depth. Implement a method to compute the
height of the tallest possible stack. The height of a stack is the sum of the heights of each box.

Hints: 
#155
Will sorting the boxes help in any way?
#194
We can sort the boxes by any dimension in descending order. This will give us a partial
order for the boxes, in that boxes later in the array must appear before boxes earlier in the array.
#214
Try to break it down into subproblems.
#260
Think about the first decision you have to make. The first decision is which box will be at
the bottom.
#322
Once we pick the box on the bottom, we need to pick the second box. Then the third box.
#368
Once you have a basic recursive algorithm implemented, think about if you can optimize it. 
Are there any repeated subproblems?
#378
Alternatively, we can think about the repeated choices as: Does the first box go on the stack? 
Does the second box go on the stack? And so on.
"""

def find_max_height(boxes):
    boxes = sorted(boxes, key = lambda box: box[0], reverse=True)
    max_height = 0
    max_heights = [None for _ in range(len(boxes))]
    for i in range(len(boxes)):
        height = __find_max_height(boxes, i, max_heights)
        max_height = max(height, max_height)
    return max_height

def __find_max_height(boxes, bottom_index, max_heights):
    if max_heights[bottom_index]:        
        return max_heights[bottom_index]    
    max_height = 0
    for i in range(bottom_index+1, len(boxes)):        
        if check_requirements(boxes[bottom_index], boxes[i]):                        
            height = __find_max_height(boxes, i, max_heights)            
            max_height = max(height, max_height)            
    max_height += boxes[bottom_index][1]    
    max_heights[bottom_index] = max_height
    return max_height

def check_requirements(lower, upper):
    for i in range(len(lower)):
        if lower[i] < upper[i]:
            return False
    return True


def find_max_height_with_optimization(boxes):
    boxes = sorted(boxes, key=lambda box: box[1], reverse=True)
    max_heights = [ 0 for _ in range(len(boxes)) ]
    return __find_max_height_with_optimization(boxes, None, 0, max_heights)

def __find_max_height_with_optimization(boxes, bottom, offset, max_heights):
    if offset >= len(boxes):
        return 0
    new_bottom = boxes[offset]
    height_with_bottom = 0    
    if bottom is None or check_requirements(bottom, new_bottom):        
        if max_heights[offset] == 0:
            max_heights[offset] = __find_max_height_with_optimization(boxes, new_bottom, offset+1, max_heights)
            max_heights[offset] += new_bottom[1]            
        height_with_bottom = max_heights[offset]        
    height_without_bottom = __find_max_height_with_optimization(boxes, bottom, offset+1, max_heights)    
    return max(height_with_bottom, height_without_bottom)

import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.boxes = list()
        self.boxes.append([100, 100, 100])
        self.boxes.append([10, 5, 10])
        self.boxes.append([30, 20, 20])
        self.boxes.append([15, 10, 15])
        self.boxes.append([40, 10, 20])
    
    def test_find_max_height(self):
        self.assertEqual(find_max_height(self.boxes), 135)

    def test_find_max_height_with_optimization(self):
        self.assertEqual(find_max_height_with_optimization(self.boxes), 135)

if __name__ == "__main__":
    unittest.main()