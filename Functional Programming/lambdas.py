"""
Creating a function normally (using def) assigns it to a variable automatically. 
This is different from the creation of other objects - such as strings and integers - which can be created on the fly, without assigning them to a variable. 
The same is possible with functions, provided that they are created using lambda syntax. Functions created this way are known as anonymous.
This approach is most commonly used when passing a simple function as an argument to another function. The syntax is shown in the next example and consists of the lambda keyword followed by a list of arguments, a colon, and the expression to evaluate and return.
"""


def my_func(f, arg):
  return f(arg)

print(my_func(lambda x: 2*x*x, 5))



#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda
print((lambda x: x**2 + 5*x + 4) (-4))

print((lambda x: x**2 + 5*x + 6) (-3))


#Also in Variable

triple = lambda x: x * 3
add = lambda x, y: x + y
print(add(triple(3), 4))