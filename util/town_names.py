# Marvan Tennekoon (mt588), COMP6590 - Practical Project
import random

towns = ["Transylvania", "Salem", "Whitby", "Derry", "Bran", "Sleepy Hollow", "Castle Dracula", "Arkham", "Innsmouth",
         "Silent Hill", "Ravenswood", "Midwich", "Haddonfield", "Amityville", "Bates Motel"]

def get_town():
    index = random.randint(0, len(towns) - 1)
    return towns[index]
