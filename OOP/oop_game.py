
class GameObject():
	class_name = ""
	desc = ""
	objects = {}
	def __init__(self, name):
		self.name = name
		GameObject.objects[self.class_name] = self
	def get_desc(self):
		return self.class_name+"\n"+self.desc

class Goblin(GameObject):
	def __init__(self, name):
		self.class_name = "goblin"
		self.health = 3
		self._desc = "A foul creature"
		super().__init__(name)


	@property
	def desc(self):
		if self.health>=3:
			return self._desc
		elif self.health == 2:
			health_line = "It has wound in knee."
		elif self.health == 1:
			health_line = "Its left arm has benn cut off"
		elif self.health <= 0:
			health_line = "its dead."
		return self._desc+"\n"+health_line
	
	@desc.setter
	def desc(self, value):
		self._desc = value

"""
Why does desc turned into property?

It means you get a different description depending on the state of the object (gobbly, a Goblin) when the program is running and the verb examine is called. Dynamically means ”constructed when the program is running and able to depend from the state of the program at that time”. 
When self.desc was just = ”A foul creature”, it can only return that value when you executed self.desc.
But transforming it into a method of the object (well, a @property) it becomes a function as complex as you want that can construct its message having into account all the info available from that piece of code at the time the property/function desc() is executed, in this case telling you how damaged the Goblin is.


in OOP
attributes are  treated as variables.
methods are treated as functions.

a property is presented as an attribute but it is actually a method which means it can have more functionality than a variable

desc was changed from a variable(attribute)   to a property so that it can encapsulate the functionality  of the code block you see inside the method desc(you got the health line and such which is a demand that needs to be handled and was impossible to do with one variable)

also a property was added to provide the  setter function, for that  security and easy dynamic change of the the properties(method/attribute)   value.
"""


def hit(noun):
	if noun in GameObject.objects:
		thing = GameObject.objects[noun]
		if type(thing) == Goblin:
			thing.health = thing.health -1 
			if thing.health <= 0:
				msg = "You killed the Goblin!"
			else:
				msg = "You hit the {}".format(thing.class_name)
				thing.desc = "pitiful wounded {}".format(thing.class_name)
		else:
			msg = "There is no {} here".format(noun)
		return msg



class Kutta(GameObject):
	class_name = "kutta"
	desc = "A awul foul creature"

goblin = Goblin("Gobbly")
kutta = Kutta("Kuttas")


def examine(noun):
	if noun in GameObject.objects:
		return GameObject.objects[noun].get_desc()
	else:
		return "There is no {} here".format(noun)


def get_input():
	command = input(": ").split()
	verb_word = command[0]
	if verb_word in verb_dict:
		verb = verb_dict[verb_word]
	else:
		print("Unknown verb {}".format(verb_word))
		return
	if len(command) >=2:
		noun_word = command[1]
		print(verb(noun_word))
	else:
		print(verb("nothing"))

def say(noun):
	return 'You said {}'.format(noun)
def go(noun):
	return 'Go fast {}'.format(noun)
verb_dict = {
	"say":say,
	"go" : go,
	"examine": examine,
	"hit" : hit
}

while True:
	get_input()