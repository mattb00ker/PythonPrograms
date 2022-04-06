# Program to brute force crack a randomly generated number string
import random

guessesTaken = 0
number = random.randint(0,1000000)
numPrint = 0

numPrint = number
numPrint =str(numPrint)

print numPrint + ' This is the number to guess.' 

guess = random.randint(0,1000000)

while guess != number:
    guess = random.randint(0,1000000)
    print guess
    guessesTaken = guessesTaken + 1

    if guess == number:
        break
    
guessesTaken = str(guessesTaken)
number = str(number)
print 'Found ' + number + ' in ' + guessesTaken + ' cycles.'

raw_input()
