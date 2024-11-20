from turtle import Turtle
from random import randint


laura = Turtle()
laura.color('red')
laura.shape('turtle')

laura.penup()
laura.goto(-160, 100)
laura.pendown()

kevin = Turtle()
kevin.color('blue')
kevin.shape('turtle')
kevin.penup()
kevin.goto(-160, 70)
kevin.pendown()

james = Turtle()
james.color('green')
james.shape('turtle')
james.penup()
james.goto(-160, 40)
james.pendown()

jess = Turtle()
jess.color('purple')
jess.shape('turtle')
jess.penup()
jess.goto(-160, 10)
jess.pendown()

for movement in range(100):
    laura.forward(randint(1,5))
    kevin.forward(randint(1,5))
    james.forward(randint(1,5))
    jess.forward(randint(1,5))

input("Press Enter to close")
