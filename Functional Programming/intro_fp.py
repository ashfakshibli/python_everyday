"""
Functional programming is a style of programming that (as the name suggests) is based around functions. 
A key part of functional programming is higher-order functions. We have seen this idea briefly in the previous lesson on functions as objects. Higher-order functions take other functions as arguments, or return them as results.
"""



def apply_double_power(func, base, power):
	return func(base, func(base, power))


def more_power(base,power):
	return base**power

print(apply_double_power(more_power, 2,2))


#16