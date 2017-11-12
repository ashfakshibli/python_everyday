# recursive implementation of the factorial function.


def factorial(x):
  if x == 1:
    return 1
  else: 
    return x * factorial(x-1)


num = int(input("Enter number to factorial: "))
print(factorial(num))




"""
Recursion can also be indirect. One function can call a second, which calls the first, which calls the second, and so on. This can occur with any number of functions.
"""


def is_even(x):
  if x == 0:
    return True
  else:
    print (x)
    return is_odd(x-1)

def is_odd(x):
  return not is_even(x)


print(is_odd(17))
print(is_even(24))


"""
Fibonacci

"""


def fib(x):
  if x == 0 or x == 1:
    return 1
  else: 
    return fib(x-1) + fib(x-2)
print(fib(4))

# 5
# 
"""
                             fib(4)
              ¡----------------^----------------¡
         fib(3)             +              fib(2)
       ¡------^------¡                    ¡--------^-----¡
    fib(2)   +  fib(1)         fib(1)   +   fib(0)
  ¡----^----¡           |           |                |
fib(1)+ fib(0)   |                  |                |
  |        |         |              |                |
 1     +    1   +  1       +        1       +     1

"""

