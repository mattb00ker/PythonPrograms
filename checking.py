num_int = int(input("Input an integer but 0 terminates"))

count = 0
total = 0

while num_int != 0:
    count = count + 1
    total = total + num_int
    num_int = int(input("Input an integer but 0 terminates"))
else:
    print("Total equals", total, "Count equals", count)