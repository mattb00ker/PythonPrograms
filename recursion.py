def evennumbers(num):
    print(num)
    if num % 2 !=0:
        print("the number needs to be even")
    elif num == 2:
        return num
    else:
        return evennumbers(num-2)
    
evennumbers(101)