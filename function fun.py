def speed(distance, time):
    answer = distance / time
    print(answer)

def distance(speed, time):
    answer = speed * time


def time(speed, distance):
    answer = distance / speed

choice = input("What do you want to calculate , 1 for speed , 2 for distance , 3 for time")
if choice == "1":
    disti = input("distance:")
    distance = int(disti)
    time = int(input("time:"))
    speed(distance, time)




elif choice == "2":
    speed = int(input("speed:"))
    time = int(input("time:"))




elif input == "3":
    distance = input(int("distance:"))
    speed = input(int("speed:"))




    print(answer)

