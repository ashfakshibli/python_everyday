"""
When an object is destroyed, the memory allocated to it is freed up, and can be used for other purposes.
Destruction of an object occurs when its reference count reaches zero. Reference count is the number of variables and other elements that refer to an object.
If nothing is referring to it (it has a reference count of zero) nothing can interact with it, so it can be safely deleted.

In some situations, two (or more) objects can be referred to by each other only, and therefore can be deleted as well. 
The del statement reduces the reference count of an object by one, and this often leads to its deletion.
The magic method for the del statement is __del__. 
The process of deleting objects when they are no longer needed is called garbage collection.
In summary, an object's reference count increases when it is assigned a new name or placed in a container (list, tuple, or dictionary). The object's reference count decreases when it's deleted with del, its reference is reassigned, or its reference goes out of scope. When an object's reference count reaches zero, Python automatically deletes it.
"""
