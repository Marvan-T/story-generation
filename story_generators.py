import random


def generate_stage1_variations(monster, location):
    sentences = []

    beginnings = [
        f"A mysterious presence lurks",
        f"An eerie silence surrounds",
        f"A sense of dread pervades",
    ]

    middles = [
        f"in the shadows of {location.name}",
        f"within the chilling atmosphere of {location.name}",
        f"among the abandoned buildings of {location.name}",
    ]

    endings = [
        f", known as {monster.name}.",
        f", and whispers of {monster.name} haunt the residents.",
        f", as stories of {monster.name} continue to terrify.",
    ]

    for i in range(5):
        beginning = random.choice(beginnings)
        middle = random.choice(middles)
        ending = random.choice(endings)

        sentence = beginning + middle + ending
        sentences.append(sentence)

    return sentences
