"""
List comprehensions are a useful way of quickly creating lists whose contents obey a simple rule. List comprehensions are inspired by set-builder notation in mathematics.
"""


cubes = [i**3 for i in range(50)]

print(cubes)


#[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859, 8000, 9261, 10648, 12167, 13824, 15625, 17576, 19683, 21952, 24389, 27000, 29791, 32768, 35937, 39304, 42875, 46656, 50653, 54872, 59319, 64000, 68921, 74088, 79507, 85184, 91125, 97336, 103823, 110592, 117649]
#[Finished in 0.4s]
#





power_of_twos = [2**i for i in range(11)]

print(power_of_twos)

# [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]


#Memory Error. 

even = [2*i for i in range(10**100)]
#OverflowError: range() result has too many items
#Solved by generators next.