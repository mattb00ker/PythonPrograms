shopping=['fugu', 'ramen', 'sake', 'shiitake mushrooms', 'soy sauce', 'wasabi']
prices={'fugu' : 100.0, 'ramen':5.o, 'sake':45.0, 'shiitake mushrooms':3.5, 'soy sauce':7.50, 'wasabi':10.0}
total=0.00

for item in shopping:
	total += prices[item]

