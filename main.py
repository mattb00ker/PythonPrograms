from room import Room
from item import Item
from character import Character
from character import Enemy

#Building rooms
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")
#kitchen.get_describe()

dining_hall = Room("Dining Hall")
dining_hall.set_description("A lage room with ornate things")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny dance floor")

#Room links
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

#Making items
sword = Item("Sword")
sword.set_description("A sharp short sword")

#Adding items to rooms
kitchen.add_items(sword)

#dining_hall.get_details()
#kitchen.get_details()
#ballroom.get_details()

dave = Enemy("Dave", "A smelly zombie")
dave.describe()
dave.set_conversation("I love Spurs")
dave.talk()

current_room = kitchen          

while True:    
    print("\n")         
    current_room.get_details()         
    command = input("> ")    
    current_room = current_room.move(command) 