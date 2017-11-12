"""
The class describes what the object will be, but is separate from the object itself. In other words, a class can be described as an object's blueprint, description, or definition.
You can use the same class as a blueprint for creating multiple different objects. 

Classes are created using the keyword class and an indented block, which contains class methods (which are functions). 

"""

class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs
  def bark(self):
    print("Woof! by "+self.color+" Colored")

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)


print(felix.color)
felix.bark()

"""
Trying to access an attribute of an instance that isn't defined causes an AttributeError. This also applies when you call an undefined method.


class Rectangle: 
  def __init__(self, width, height):
    self.width = width
    self.height = height

rect = Rectangle(7, 8)
print(rect.color)

"""