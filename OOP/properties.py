"""
Properties provide a way of customizing access to instance attributes. 
They are created by putting the property decorator above a method, which means when the instance attribute with the same name as the method is accessed, the method will be called instead. 
One common use of a property is to make an attribute read-only.
"""
class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings
    
  @property
  def pineapple_allowed(self):
    return False

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
##pizza.pineapple_allowed = True


"""
Properties provide a way of customizing access to instance attributes. 
They are created by putting the property decorator above a method, which means when the instance attribute with the same name as the method is accessed, the method will be called instead. 

One common use of a property is to make an attribute read-only.
Properties can also be set by defining setter/getter functions.
The setter function sets the corresponding property's value.
The getter gets the value.
To define a setter, you need to use a decorator of the same name as the property, followed by a dot and the setter keyword.
The same applies to defining getter functions.
Example:
"""
class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings
    self._pineapple_allowed = False

  @property
  def pineapple_allowed(self):
    return self._pineapple_allowed

  @pineapple_allowed.setter
  def pineapple_allowed(self, value):
    if value:
      password = input("Enter the password: ")
      if password == "Sw0rdf1sh!":
        self._pineapple_allowed = value
      else:
        raise ValueError("Alert! Intruder!")

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)