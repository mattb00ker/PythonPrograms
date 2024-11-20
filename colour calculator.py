wavelength = float(input("What is the wavelength?")) #in nm

SOL = 299729458 #m/s

frequency = SOL / (wavelength*1000)

print(str(frequency))

# frequencies converted to THz
if(frequency >= 668):
    print("violet")
elif(frequency >= 606):
    print("blue")
elif(frequency >= 526):
    print("green")
elif(frequency >= 508):
    print("yellow")
elif (frequency >= 484):
    print("orange")
elif(frequency >= 400):
    print("red")
else:
    print("it's outside our ability to see")

