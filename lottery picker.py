#This is a lottery number picker

import random

numbersChosen = []

print("this program will randomly pick numbers for use in the lottery")

while len(numbersChosen) < 6:
    

    
    numbersChosen.append(random.randint(1, 50))

print(numbersChosen)
