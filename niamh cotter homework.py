x = int(input("What is your number: "))
count = 0
total = 0
while x != 0:
    total = total + x
    count = count + 1
    x = int(input("What is your number: "))
else:
    print(total, count)

