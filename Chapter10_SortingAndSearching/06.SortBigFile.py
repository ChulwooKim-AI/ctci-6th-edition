"""Sort Big File

Imagine you have a 20 GB file with one string per line. Explain how you would sort the file.

Hints: 
#207
Think about merge sort versus quick sort. Would one of them work well for this purpose?
"""

'''
# External sorting
External sorting is a class of sorting algorithms that can handle massive amounts of data. 
External sorting is required when the data being sorted do not fit into the main memory of 
a computing device (usually RAM) and instead they must reside in the slower external memory, 
usually a hard disk drive. Thus, external sorting algorithms are external memory algorithms 
and thus applicable in the external memory model of computation.

External sorting algorithms generally fall into two types, 
distribution sorting, which resembles quicksort, and external merge sort, which resembles merge sort. 
The latter typically uses a hybrid sort-merge strategy. 
In the sorting phase, chunks of data small enough to fit in main memory are read, sorted, and 
written out to a temporary file. 
In the merge phase, the sorted subfiles are combined into a single larger file.

For example, for sorting 900 megabytes of data using only 100 megabytes of RAM:

1. Read 100 MB of the data in main memory and sort by some conventional method, like quicksort.
2. Write the sorted data to disk.
3. Repeat steps 1 and 2 until all of the data is in sorted 100 MB chunks 
   (there are 900MB / 100MB = 9 chunks), which now need to be merged into one single output file.
4. Read the first 10 MB (= 100MB / (9 chunks + 1)) of each sorted chunk into input buffers in 
   main memory and allocate the remaining 10 MB for an output buffer. 
   (In practice, it might provide better performance to make the output buffer larger and 
   the input buffers slightly smaller.)
5. Perform a 9-way merge and store the result in the output buffer. 
   Whenever the output buffer fills, write it to the final sorted file and empty it. 
   Whenever any of the 9 input buffers empties, fill it with the next 10 MB of its associated 100 MB 
   sorted chunk until no more data from the chunk is available. 
   This is the key step that makes external merge sort work externally 
   -- because the merge algorithm only makes one pass sequentially through each of the chunks, 
   each chunk does not have to be loaded completely; rather, sequential parts of the chunk can be 
   loaded as needed.

# Reference by 
https://en.wikipedia.org/wiki/External_sorting

This code is about k-sorted array merge.
'''

import heapq

def merge_arrays(arrays):    
    result = list()
    heap = list()
    for array in arrays:
        if array:
            heapq.heappush(heap, (array.pop(0), array))

    while heap:
        smallest = heapq.heappop(heap)
        result.append(smallest[0])              
        if smallest[1]:
            heapq.heappush(heap, (smallest[1].pop(0), smallest[1]))

    return result


import unittest

class Test(unittest.TestCase):
    def setUp(self):
        array1 = [1, 3, 6]
        array2 = [2, 4]
        self.arrays = [array1, array2]
    
    def test_merge_arrays(self):
        self.assertListEqual(merge_arrays(self.arrays), [1,2,3,4,6])


if __name__ == "__main__":
    unittest.main()