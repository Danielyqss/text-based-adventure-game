# Course: CS30
# Period: 1
# Date created: 21/09/21
# Date last modified: 21/11/05
# Name: Xinhao Liu
# Assignment: RPG 
# Instructor: Janice Cotcher

from map import map_look
import character
from map import maps
from character import roles_to_pick
from inventory import overall_inventory
import sys
import random
import inventory
import map


print(map_look)

def direction_to_go(role):
    while True:
        print("\n")
    # print a list of valid positions for character
    # set up direct for players to input their positions
        positions = ["North", "South", "East", "West"]
        for p in positions:
            print(f"- {p}")
        direct = input("Which direction do you want to go? ")
    # after the player input print out the direction
        if direct in positions:
            print(" you have escape to " + direct + " where you may see...")
            monster()
    # players can input "quit", to leave the game anytime
        elif direct == "quit":
            sys.exit("Goodbye!")
        # check for invalid input
        else:
            print("invalid input")


def pick_your_role():
    while True:
        # print roles for player to input
        print("Knight Press '1', Swordsman Press '2', Mage Press '3'")
        character.pick_ur_role(roles_to_pick)
        role = input("Enter your choice: ")
        # after player input print out properties
        if role == "1":
            print("\n")
            Property_of_Knight = "Knight: \nHealth = 80 \nAttack = 20\
                                  \nMovement speed = 40\n"
            print("You've picked 'Knight':\n" + Property_of_Knight)
            return role
            break
        elif role == "2":
            print("\n")
            Property_of_Swordsman = "Swordsman: \nHealth = 65 \nAttack = 30\
                                     \nMovement speed = 40\n"
            print("You've picked 'Swordsman': \n", Property_of_Swordsman)
            return role
            break
        elif role == "3":
            print("\n")
            Property_of_Mage = "Mage: \nHealth = 60 \nAttack = 35\
                                \nMovement speed = 40\n"
            print("You've picked 'Mage': \n" + Property_of_Mage)
            return role
            break
        elif role == "quit":
            sys.exit("Goodbye!")
        # check for invalid inputs
        else:
            print("invalid 3 input")


def actionA(role):
    while True:
        # give valid actions for player
        actA = input("\nWhat to do now? \n-explore \n-quit \n-inventory\
                     \n-overallinventory \n-worldmap \n:")
        # after player input, print out the action choosen by the player
        actions_to_do_A = ["explore", "quit", "inventory",
                           "overallinventory", "worldmap"]
        if actA == (actions_to_do_A[0]):
            direction_to_go(role)
        elif actA == (actions_to_do_A[1]):
            sys.exit("Goodbye!")
        elif actA == (actions_to_do_A[2]):
            inventory.beginner_weapon(role)
        elif actA == (actions_to_do_A[3]):
            if role == "1":
                print("\n")
                inventory.roles_overall_inventory("All levels of weapons for Knight:",
                                        overall_inventory)
            elif role == "2":
                print("\n")
                inventory.roles_overall_inventory("All levels of weapons for Swordsman:",
                                        overall_inventory)
            elif role == "3":
                print("\n")
                inventory.roles_overall_inventory("All levels of weapons for Mage:",
                                        overall_inventory)
            else:
                print("invalid 1 input")
        elif actA == (actions_to_do_A[4]):
            map.game_map(maps)
        # check for invalid input
        else:
            print("invalid 2 input")
            print("\n")


def monster():
    print("\n")
    # random situations after player input their action
    list = ["yes", "no"]
    mon = random.choice(list)
    if mon == (list[0]):
        print("OH! A MONSTER!!")
        # unlock actionB if player is in this situation
        actionB()
    if mon == (list[1]):
        print("The sight is really beautiful")
        actionA(role)


def actionB():
    # valid actions for character when saw a monster
    actions_to_do_B = ["attack", "defend", "run", "quit", "inventory",
                       "overallinventory", "worldmap"]
    while True:
        # print a list of valid actions before player input
        print("Choose what do to now! \n-attack \n-defend \n-run \n-quit ")
        choice = input("Now I: ")
        # after the player input print out the action choosen by the player
        if choice == (actions_to_do_B[0]):
            print("Nice hit!")
            print("\n")
            actionA(role)
        elif choice == (actions_to_do_B[1]):
            print("Try to hit back!")
            print("\n")
        elif choice == (actions_to_do_B[2]):
            direction_to_go(role)
        elif choice == (actions_to_do_B[3]):
            sys.exit("Goodbye!")
        elif choice == (actions_to_do_B[4]):
            inventory.beginner_weapon(role)
        elif choice == (actions_to_do_B[5]):
            overall_inventory()
        elif choice == (actions_to_do_B[6]):
            map.game_map(maps)
        else:
            print("invaild input")
            print("\n")
    # for player to input their name

name = input("Enter your name: ")
# print out the name choosen by the player
print("Hey " + name + ", Welcome! Now pick your role.")
print("\n")
role = pick_your_role()
while True:
    # print valid choices for player to input and confirm their chooice
    print("Confirm your choice by pressing Y")
    print("Press N if not confirmed")
    conf = input("Do you confirm your choice?: ")
    # after player input print out their choice
    if conf == "Y":
        print("\n")
        break
    elif conf == "N":
        print("\n")
        pick_your_role()
    elif conf == "quit":
        sys.exit("Goodbye!")
    else:
        print("invalid input")
        print("\n")
print("You have picked your role!")
print("\n")
print("Now you can start your advanture!")
# start to enter the game loop
actionA(role)














































