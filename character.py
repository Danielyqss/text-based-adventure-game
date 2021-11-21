# character properties
roles_to_pick = {"Knight":
                 {"properties: \nHealth = 80 \nAttack damage = 20\
                 \nMovement speed = 40"},
                 "Swordsman":
                 {"properties: \nHealth = 65 \nAttack damage = 30\
                 \n Movement speed = 40"},
                 "Mage":
                 {"properties: \nHealth = 60 \nAttack damage = 35\
                 \nMovement speed = 40 "}}


# generate a list of characters and their properties
def pick_ur_role(roles_to_pick):
    for rolc in roles_to_pick:
        # print the list of characters
        print(f"\n{rolc}")
        for properties in roles_to_pick[rolc]:
            # print the list of properties under each character
            print(f"{properties}")

