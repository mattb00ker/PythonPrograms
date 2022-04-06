shopping=['fugu', 'ramen',  'sake', 'rubbish']
prices = {'fugu':4, 'ramen':4, 'sake':50, 'rubbish':12}

total = 0

for item in shopping:
	total+= prices[item]

total = str(total)
print 'your shopping costs ' + total

raw_input()