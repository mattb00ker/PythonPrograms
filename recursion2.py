def get_to_zero(number, count):
    print(number, count)
    if number > 0:
        number = number - 1
        count = count + 1
        # print("count",count, "number", number)
        get_to_zero(number, count)
    else:
        print(count)
        return count

count = get_to_zero(7, 0)

print(count)