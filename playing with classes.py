class Person(object):
	def __init__(self, name, age=0):
		self.name = name
		self.age = age
		self.ammo = 1000
		self.armor = 12
		
		
	def sayHi(self):
		print 'Hello, my name is', self.name
	def whatAge(self):
		print 'I\'m ', self.age, 'years old.'

#myPerson = Person('Matt', '26')

p = Person(name=raw_input('what\'s your name? '))
p.sayHi()

p = Person(age = raw_input('what\'s your age? '))
p.whatAge()

print p.name, p.age, p.ammo, p.armor
#print myPerson
