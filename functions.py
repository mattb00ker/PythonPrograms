def speed (dist, time):
    ans = dist/time
    print(ans)

def dist (speed, time):
    ans = speed*time
    print(ans)

def time(speed, dist):
    ans = dist/speed
    print(ans)

option = input("What would you like to calculate? speed = 1, dist = 2, time =3")

if option == "1":
    distance = int(input("what is the distance?"))
    tim = int(input("WHat was the time?"))
    speed(distance, tim)