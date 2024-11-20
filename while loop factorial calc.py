number = int(input("Enter a number to calculate its factorial: "))
result = 1
while number > 0:
    result *= number
    number -= 1
print(f"The factorial is {result}")


