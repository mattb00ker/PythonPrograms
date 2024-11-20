weather_good = False  # Imagine this is a sensor reading from the rocket control system

for countdown in range(10, 0, -1):
    if not weather_good:
        print("Launch paused due to bad weather.")
        break
    print(countdown)
print("Liftoff!")
