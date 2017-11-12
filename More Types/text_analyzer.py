"""

This part of the program shows a function that counts how many times a character occurs in a string.
"""

def char_count(text, char):
	count = 0
	for c in text:
		if c == char:
			count+=1
	return count


filename = input("Enter File name: ")

with open(filename) as f:
	text = f.read()


for char in "abcdefghijklmnopqrstuvwxyz":
	percent = 100* char_count(text,char)/len(text)
	print("{0}--{1} %".format(char, round(percent, 2)))