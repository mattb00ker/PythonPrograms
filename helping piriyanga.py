total_sum = 0
count = 0
user_input = int(input("Enter a number (0 to stop): "))
while user_input != 0:
    # This loop will continue until we break it

    if user_input != 0:
        total_sum += user_input
        count += 1
        user_input = int(input("Enter a number (0 to stop): "))
    else:
        break

print(f"Total sum of numbers: {total_sum}")
print(f"Number of inputs: {count}")
