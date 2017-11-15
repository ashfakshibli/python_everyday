"""

There are various special sequences you can use in regular expressions. They are written as a backslash followed by another character. 
One useful special sequence is a backslash and a number between 1 and 99, e.g., \1 or \17. This matches the expression of the group of that number.

"""


import re

pattern = r"(.+) \1"

match = re.match(pattern, "word word")
if match:
   print ("Match 1")

match = re.match(pattern, "?! ?!")
if match:
   print ("Match 2")    

match = re.match(pattern, "abc cde")
if match:
   print ("Match 3")

"""
Note, that "(.+) \1" is not the same as "(.+) (.+)", because \1 refers to the first group's subexpression, which is the matched expression itself, and not the regex pattern.

"""


"""

More useful special sequences are \d, \s, and \w.
These match digits, whitespace, and word characters respectively. 
In ASCII mode they are equivalent to [0-9], [ \t\n\r\f\v], and [a-zA-Z0-9_].
In Unicode mode they match certain other characters, as well. For instance, \w matches letters with accents.
Versions of these special sequences with upper case letters - \D, \S, and \W - mean the opposite to the lower-case versions. For instance, \D matches anything that isn't a digit.

(\D+\d) matches one or more non-digits followed by a digit.

"""
import re

pattern = r"(\D+\d)"

match = re.match(pattern, "Hi 999!")

if match:
   print("Match 1")

match = re.match(pattern, "1, 23, 456!")
if match:
   print("Match 2")

match = re.match(pattern, " ! $?")
if match:
    print("Match 3")


"""
 'SPAM!'

Will match         \AS...\b.\Z


\AS (beginning with S)
...\b (any character inbetween)
.\Z (ending in any character or instance)


1. Remember, \A is a special sequence meaning starting the string.  Putting it in the middle of the pattern would either give an error, or never be possible. Basically you are asking for 'SP' to be before the start of the string.

2. Again the \A means at the start of the string, and the dots mean any character. So the expression '\AS...\b.\Z' translates to "at the start of the string look for a capital s followed by any three characters to form a word (the \b) and any character (the period after the b), and then an end of the string (\Z)"

"""

import re

pattern = r"\AS...\b.\Z"
pattern1 = r"SP\AM!\Z"
pattern2 = r"\ASPAM\Z"

match = re.search(pattern, "SPAM!")
match1 = re.search(pattern1, "SPAM!")
match2 = re.search(pattern2, "SPAM!")


if match2:
	print ("Matched Pattern")