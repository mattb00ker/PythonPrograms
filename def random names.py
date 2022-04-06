import random

nameList = 'Tom Dick Harry Peter John Matthew'.split()

def randName(names):
	nameIndex = random.randint(0, len(names) -1)
	return names[nameIndex]

count = 0

total = raw_input('How many cycles?')
total = int(total)


while count != total:
	chosenName = randName(nameList)
	print 'Hello ' + chosenName + ' ' + str(count)
	count = count + 1