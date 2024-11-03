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

#Make characters
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("I love Spurs")
dave.set_weakness("cheese")

helen = Enemy("Helen", "A scary vampire")
helen.set_conversation("Can i interest you in a time-share?")
helen.set_weakness("garlic")

#Making items
sword = Item("Sword")
sword.set_description("A sharp short sword")

#Adding items to rooms
kitchen.add_items(sword)

#Adding characters to rooms
dining_hall.set_character(dave)
ballroom.set_character(helen)
#dining_hall.get_details()
#kitchen.get_details()
#ballroom.get_details()

current_room = kitchen          

while True:    
    print("\n")         
    current_room.get_details()   
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()   
           
    command = input("> ")

    # Check whether a direction was typed
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk() 
        else:
            print("There's no one here dude!")
    elif command == "fight":
        if inhabitant is not None:
            combat_item = input("What would you like to fight with? ")
            if inhabitant.fight(combat_item) == False:
                break
        else:
            print("There's no one here dude!")