


# a dictionary of every places in the game and their explainations
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

map_creature = {"Monsters": {"description": "location of monsters in a map",
                             "pass": "defeat all"},
                "Shop": {"description": "location of shops in a map",
                         "pass": "free to go or you can upgrade your weapon"},
                "Teleport": {"description": "appears when you finished the map",
                             "pass": "finish the map"}}
def print_map():
    map_look = """
    Home       Teleport gate     
          |           lol 
          |   shop
          |
          |            teleport gate
          |
    """
    print(map_look)
# generate a list of map and their descriptions
def game_map(maps):
    print("\n")
    for descriptions in maps:
        print(f"{descriptions}: ")
        # print items in descriptions
        for item in maps[descriptions]:
            print(f"-{item}")

map_look = """
    Home        Shop       Teleport gate     
          |           
    E tier| E Tier Monsters | Shop | Boss | Award | Teleport gate 
          |
    D tier| B Tier Monsters | Shop | Boss | Award | Teleport gate         
          |
    C tier| C Tier Monsters | Shop | Boss | Award | Teleport gate
          |            
    B tier| B Tier Monsters | Shop | Boss | Award | Teleport gate
          |                           
    A tier| A Tier Monsters | Shop | Boss | Award | Teleport gate                             |
    S tier| S Tier Monsters | Shop | Boss | Award | Teleport gate
    """
print(map_look) 