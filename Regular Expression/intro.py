"""

Regular expressions in Python can be accessed using the re module, which is part of the standard library. 
After you've defined a regular expression, the re.match function can be used to determine whether it matches at the beginning of a string.
If it does, match returns an object representing the match, if not, it returns None.
To avoid any confusion while working with regular expressions, we would use raw strings as r"expression".
Raw strings don't escape anything, which makes use of regular expressions easier.
"""


import re

pattern = r"sp"

if re.match(pattern, "spamspamspam"):
   print("Match")
else:
   print("No match")
"""
Other functions to match patterns are re.search and re.findall. 
The function re.search finds a match of a pattern anywhere in the string.
The function re.findall returns a list of all substrings that match a pattern.
"""
if re.search(pattern, "eggspamsausagespam"):
   print("Match")
else:
   print("No match")
    
print(re.findall(pattern, "eggspamsausagespam"))
iterable = re.finditer(pattern, "eggspamsausagespam")

for s in iterable:
	print(s)


"""

The regex search returns an object with several methods that give details about it. 
These methods include group which returns the string matched, start and end which return the start and ending positions of the first match, and span which returns the start and end positions of the first match as a tuple.
"""


import re

pattern = r"pam"

match = re.search(pattern, "eggspamsausage")
if match:
   print(match.group())
   print(match.start())
   print(match.end())
   print(match.span())


"""
   One of the most important re methods that use regular expressions is sub.
Syntax:

This method replaces all occurrences of the pattern in string with repl, substituting all occurrences, unless max provided. This method returns the modified string. 

"""

import re

str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)