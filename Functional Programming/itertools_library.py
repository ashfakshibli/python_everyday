"""
The module itertools is a standard library that contains several functions that are useful in functional programming. 
One type of function it produces is infinite iterators. 
The function count counts up infinitely from a value. 
The function cycle infinitely iterates through an iterable (for instance a list or string). 
The function repeat repeats an object, either infinitely or a specific number of times.
"""


from itertools import count

for i in count(3):
  print(i)
  if i >=11:
    break



"""
There are many functions in itertools that operate on iterables, in a similar way to map and filter. 
Some examples:
takewhile - takes items from an iterable while a predicate function remains true;
chain - combines several iterables into one long one; 
accumulate - returns a running total of values in an iterable.

"""


#Bug accumulate not importing
#
from itertools import accumulate, takewhile

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x<= 6, nums)))



"""
There are also several combinatoric functions in itertool, such as product and permutation.
These are used when you want to accomplish a task with all possible combinations of some items.
"""

from itertools import product, permutations

letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters))) 