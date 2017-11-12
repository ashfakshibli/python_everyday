"""
The built-in functions map and filter are very useful higher-order functions that operate on lists (or similar objects called iterables). 
The function map takes a function and an iterable as arguments, and returns a new iterable with the function applied to each argument. 
"""


def power_up(x):
	return x**2


nums = [11, 22, 33, 44]
result = list(map(power_up,nums))
print(result)


#With Lambda


result_lambda = list(map(lambda x:x**2,nums))
print(result_lambda)


"""
The function filter filters an iterable by removing items that don't match a predicate (a function that returns a Boolean). 
"""

more_nums = [54, 45, 65, 48, 54]

filtering_result = list(filter(lambda x: x%2 == 0, more_nums))

print(filtering_result)