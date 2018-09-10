"""Paint Fill

Implement the "paint fill" function that one might see on many image editing programs.
That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color,
fill in the surrounding area until the color changes from the original color.

Hints: 
#364
Think about this as a graph.
#382
You can implement this using depth-first search (or breadth-first search). Each adjacent
pixel of the "right" color is a connected edge.
"""

def fill_paint(screen, point, new_color):
    __fill_paint(screen, point, new_color, screen[point[0]][point[1]])
    return screen

def __fill_paint(screen, point, new_color, old_color):
    if point[0] < 0 or point[0] >= len(screen) or point[1] < 0 or point[1] >= len(screen[0]) or \
        screen[point[0]][point[1]] != old_color:
        return
    screen[point[0]][point[1]] = new_color
    surrounding = [(point[0]-1, point[1]), (point[0], point[1]-1), 
                    (point[0]+1, point[1]), (point[0], point[1]+1)]
    for neighborhood in surrounding:
        __fill_paint(screen, neighborhood, new_color, old_color)


import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.screen = [[1, 1, 1, 1],
                        [1, 0, 0, 1],
                        [2, 2, 0, 0],
                        [2, 2, 0, 0]]
    
    def test_paint_fill(self):
        self.assertListEqual(fill_paint(self.screen, (2, 2), 3), 
                                [[1, 1, 1, 1],
                                [1, 3, 3, 1],
                                [2, 2, 3, 3],
                                [2, 2, 3, 3]])


if __name__ == "__main__":
    unittest.main()