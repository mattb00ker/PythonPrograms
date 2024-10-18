def speed():
    dist = float(input("what was the distance?"))
    tim = float(input("what was the time?"))
    sped = dist/tim
    print(sped)

def distance():
    tim = float(input("what was the time?"))
    sped = float(input("what was the speed?"))
    distance = tim * sped
    print(distance)

def time():
    dist = float(input("what was the distance?"))
    sped = float(input("what was the speed?"))
    tim = dist/sped
    print(tim)

choice = input("what would you like to calcualte, distance (1), time (2), or speed (3)?")

if choice == "1":
    distance()
elif choice == "2":
    time()
else:
    speed()