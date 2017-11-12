"""
To inherit a class from another class, put the superclass name in parentheses after the class name.

"""



class Animal: 
  def __init__(self, name, color):
    self.name = name
    self.color = color

class Cat(Animal):
  def purr(self):
    print("Purr...")
        
class Dog(Animal):
  def bark(self):
    print("Woof!")

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()



# If a class inherits from another with the same attributes or methods, it overrides them.

class Wolf: 
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def bark(self):
    print("Grr...")

class Dog(Wolf):
  def bark(self):
    print("Woof")
        
husky = Dog("Max", "grey")
husky.bark()


"""
Inheritance can also be indirect. One class can inherit from another, and that class can inherit from a third class. However, circular inheritance is not possible.
"""
class A:
  def method(self):
    print("A method")
    
class B(A):
  def another_method(self):
    print("B method")
    
class C(B):
  def third_method(self):
    print("C method")
    
c = C()
c.method()
c.another_method()
c.third_method()




"""

The function super is a useful inheritance-related function that refers to the parent class. It can be used to find the method with a certain name in an object's superclass.
"""
class A:
  def spam(self):
    print(1)

class B(A):
  def spam(self):
    print(2)
    super().spam()
            
B().spam()