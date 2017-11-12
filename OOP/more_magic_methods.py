"""

More magic methods for common operators:
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |

The expression x + y is translated into x.__add__(y). 
However, if x hasn't implemented __add__, and x and y are of different types, then y.__radd__(x) is called. 
There are equivalent r methods for all magic methods just mentioned.

"""

class SpecialString():
	def __init__(self, cont):
		self.cont = cont
	def __truediv__(self, other):
		line = "=" * len(other.cont)
		return "\n".join([self.cont, line, other.cont])



name = SpecialString("Ashfak MD. Shibli")
varsity = SpecialString("CUET")
print(name / varsity)