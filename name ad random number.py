import random

name_list = ["Gemma", "Ashvin", "Lydia", "Emma", "Beau", "Maddie", "Esme"]

def name_number(names):
    for i in names:
        num = random.randint(3, 9)
        print(i, num)

name_number(name_list)