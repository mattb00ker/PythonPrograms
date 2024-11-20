#Program to convert temperatures

celsius = float(input("What is the temperature in Celsius? "))

fahrenheit = celsius * 1.8 + 32

kelvin = celsius + 273.15

print("The temp in Fahrenheit is " + str(fahrenheit))
print("The temp in Kelvin is " + str(kelvin))