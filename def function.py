def tip(price, num_plates, qual):
	total = price* num_plates
	give_tip = total*(qual/100.)
	return give_tip
	
print tip(100,2,15.0)