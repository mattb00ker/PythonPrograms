# program to determine if a vehicle is speeding

vehicle = input("what type of vehicle was used? ")

distance = float(input("how far did they travel in metres? "))

time = float(input("how long did it take in seconds? "))

speed = distance/time

if speed > 13.4 and vehicle!= "bike":
    print("the", vehicle, "was speeding")
else:
    print("the", vehicle, "was within the speed limit")






