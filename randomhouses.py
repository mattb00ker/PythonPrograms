import random

names = ["Clare", "Savvini", "Hannah", "Jo", "Kemi", "Rachel"]
houses = ["Bohun", "Mandeville", "Devereux", "Bourchier"]

def housePicker(names, houses):
    for i in names:
        house = random.randint(0,3)
        print(i, "should be added to", houses[house])

housePicker(names, houses)
