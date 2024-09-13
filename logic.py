vehicle = input("What type of vehical was seen?")
distance = input("How far did the vehical travel?")
time = input("How much time did it take?")

def speeding(vehic, dist, time):
    speed = float(dist)/float(time)
    print(str(speed)+"mph")

    if(speed>30):
        print("speeding!!")
        too_fast = True
    else:
        print("carry on, nothing to see here!")

    if too_fast == True and vehic == "bike":
        print("you're lucky, bikes can't speed")
    else:
        print("You should expect a letter!")

speeding(vehicle, distance, time)