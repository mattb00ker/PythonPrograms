import os
from tkinter import *
import random

TK_SILENCE_DEPRECATION=1

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOUR = "#00FF00"
FOOD_COLOUR = "#FF0000"
BACKGROUND_COLOUR = "#000000"

class Snake:
    pass

class Food:
    def __init__(self):
        x =random.randint(0,(GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y =random.randint(0,(GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x,y]

        canvas.create_oval(x,y, x+SPACE_SIZE, y+SPACE_SIZE, fill = FOOD_COLOUR, tag="FOOD")
    

def next_turn():
    pass

def change_direction(new_direction):
    pass

def check_collision():
    pass

def game_over():
    pass

window = Tk()
window.title("Snek Game")
window.resizable(False, False)

score = 0 
direction = 'down'

label1 = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label1.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOUR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

snake = Snake()
food = Food()

window.mainloop()