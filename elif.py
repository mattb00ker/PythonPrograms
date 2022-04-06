price = raw_input('What is the price?')

price = int(price)

if price < 20:
	print 'Thats cheap'
elif price < 100:
        print 'Reasonable price!'
else:
	print 'Thats expensive!!'