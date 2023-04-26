import random

names = ["Mike The Magician", "Alaxesis", "Prancer", "The Adrenaline Junkie", "Big Bad Bully", "Gallow Garry",
         "The Good Priest", "Red Riding Hood", "Smokers", "The Genie", "Elyse of Elysium", "Lucid Luna",
         "Fantasy Fiona", "The Tooth Fairy", "The Lurker", "Guardian Demon", "The Scientist", "Tweety Bird", "Gazer",
         "Elyse of Elysium"]


def get_random_monster_name():
    return random.choice(names)
