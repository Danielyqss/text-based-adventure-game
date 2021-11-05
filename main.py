# Course: CS30
# Period: 1
# Date created: 21/09/21
# Date last modified: 21/11/05
# Name: Xinhao Liu
# Assignment: RPG Menu and Inventory
# Instructor: Janice Cotcher


import sys
import random

maps = {"Home": {"Place where you can get your hp back"},
        "Shop": {"Place where you can buy and upgrade weapons and armor"},
        "Castle": {"E Tier map, E Tier monsters appear,\
                   \n E Tier weapons dropping"},
        "Floating City": {"D Tier map, D Tier monsters appear,\
                          \n D Tier weapons. armor dropping"},
        "War relics": {"C Tier map, C Tier monsters appear,\
                       \n C Tier weapons, armor dropping"},
        "Kingdom Frontier": {"B Tier map, B Tier monsters appear,\
                             \n B Tier weapons, armor dropping"},
        "King's Row": {"A Tier map, A Tier monsters appear,\
                       \n A Tier weapons, armor dropping"}}


def game_map(maps):
    print("\n")
    for descriptions in maps:
        print(f"{descriptions}: ")
        for item in maps[descriptions]:
            print(f"-{item}")

roles_to_pick = {"Knight":
                 {"properties: \nHealth = 80 \nAttack damage = 20\
                 \nMovement speed = 40"},
                 "Swordsman":
                 {"properties: \nHealth = 65 \nAttack damage = 30\
                 \n Movement speed = 40"},
                 "Mage":
                 {"properties: \nHealth = 60 \nAttack damage = 35\
                 \nMovement speed = 40 "}}


def pick_ur_role(roles_to_pick):
    for rolc in roles_to_pick:
        print(f"\n{rolc}")
        for properties in roles_to_pick[rolc]:
            print(f"{properties}")


overall_inventory = {"All levels of weapons for Knight:":
                     {"Sword, Shield":
                      {"description": "level: E Tier Weapon",
                       "damage": 5, "protection": 5},
                      "Dragon's Sword, Shield":
                      {"description": "level: B Tier Weapon",
                       "damage": 15, "protection": 15},
                      "Holy Gift":
                      {"description": "level: S Tier Weapon",
                       "damage": 30, "protection": 30}},
                     "All levels of weapons for Swordsman:":
                         {"Long Sword":
                          {"description": "level: E Tier Weapon",
                           "damage": 10, "protection": 0},
                          "Sword of Victory":
                          {"description": "level: B Tier Weapon",
                           "damage": 20, "protection": 0},
                          "Sanction":
                          {"description": "level: S Tier Weapon",
                           "damage": 50, "protection": 0}},
                     "All levels of weapons for Mage:":
                         {"Staff":
                          {"description": "level: E Tier Weapon",
                           "damage": 12, "protection": 0},
                          "Staff of Flowing Water":
                          {"description": "level B Tier Weapon",
                           "damage": 24, "protection": 0},
                          "Infinity Staff":
                          {"description": "level S Tier Weapon",
                           "damage": 66, "protection": 0}}
                     }


def roles_overall_inventory(roles, overall_inventory):
    print(f"{roles}")
    for item in overall_inventory[roles]:
        description = overall_inventory[roles][item]["description"]
        damage = overall_inventory[roles][item]["damage"]
        protection = overall_inventory[roles][item]["protection"]
        print(f"-{item}")
        print(f"{description}")
        print(f"damage: {damage}")
        print(f"protection: {protection}")


def beginner_weapon(role):
        if role == "1":
            print("\n")
            current_inventory = []
            current_inventory.append("Sword, Shield")
            for c_i in current_inventory:
                print("Your current inventory is: ")
                print(f"-{c_i}")
        elif role == "2":
            print('\n')
            current_inventory = []
            current_inventory.append("Long Sword")
            for c_i in current_inventory:
                print("Your current inventory is: ")
                print(f"-{c_i}")
        elif role == "3":
            print("\n")
            current_inventory = []
            current_inventory.append("Staff")
            for c_i in current_inventory:
                print("Your current inventory is: ")
                print(f"-{c_i}")
        else:
            print("invalid 5 input")


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
        else:
            print("invalid input")


def pick_your_role():
    while True:
        # print roles for player to input
        print("Knight Press '1', Swordsman Press '2', Mage Press '3'")
        pick_ur_role(roles_to_pick)
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
            beginner_weapon(role)
        elif actA == (actions_to_do_A[3]):
            if role == "1":
                print("\n")
                roles_overall_inventory("All levels of weapons for Knight:",
                                        overall_inventory)
            elif role == "2":
                print("\n")
                roles_overall_inventory("All levels of weapons for Swordsman:",
                                        overall_inventory)
            elif role == "3":
                print("\n")
                roles_overall_inventory("All levels of weapons for Mage:",
                                        overall_inventory)
            else:
                print("invalid 1 input")
        elif actA == (actions_to_do_A[4]):
            game_map(maps)
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
            beginner_weapon(role)
        elif choice == (actions_to_do_B[5]):
            overall_inventory()
        elif choice == (actions_to_do_B[6]):
            game_map(maps)
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












































