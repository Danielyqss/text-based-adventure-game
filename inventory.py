
# a nested dictionary of overall inventory in the game and their levels
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
    # generate a list of overall inventory
    for item in overall_inventory[roles]:
        # take everything out from the dictionary
        description = overall_inventory[roles][item]["description"]
        damage = overall_inventory[roles][item]["damage"]
        protection = overall_inventory[roles][item]["protection"]
        # print the descriptions of weapons
        print(f"-{item}")
        print(f"{description}")
        print(f"damage: {damage}")
        print(f"protection: {protection}")


def beginner_weapon(role):
        if role == "1":
            print("\n")
            # set the current inventory empty
            current_inventory = []
            current_inventory.append("Sword, Shield")
            for c_i in current_inventory:
                # after the user input print the list of their weapons
                print("Your current inventory is: ")
                print(f"-{c_i}")
        elif role == "2":
            print('\n')
            # set the current inventory empty
            current_inventory = []
            current_inventory.append("Long Sword")
            for c_i in current_inventory:
                # after the user input print the list of their weapons
                print("Your current inventory is: ")
                print(f"-{c_i}")
        elif role == "3":
            print("\n")
            # set the current inventory empty
            current_inventory = []
            current_inventory.append("Staff")
            for c_i in current_inventory:
                # after the user input print the list of their weapons
                print("Your current inventory is: ")
                print(f"-{c_i}")
        # check for invalid inputs
        else:
            print("invalid 5 input")
