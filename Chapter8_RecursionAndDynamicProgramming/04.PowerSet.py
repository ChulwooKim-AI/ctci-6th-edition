"""Power Set

Write a method to return all subsets of a set.

Hints: 
#273
How can you build all subsets of {a, b, c} from the subsets of {a, b}?
#290
Anything that is a subset of {a, b} is also a subset of {a, b, c}. Which sets are
subsetsof{a, b, c}butnot{a, b}?
#338
Subsets that contain c will be subsets {a, b, c} but not {a, b}. Can you build these
subsets from the subsets of {a, b}?
#354
You can build the remaining subsets by adding c to all the subsets of {a, b}.
#373
You can also do this by mapping each subset to a binary number. The ith bit could
represent a "boolean" flag for whether an element is in the set.
"""