import random


def generate_stage1_variations(monster, location):
    sentences = []

    beginnings = [
        f"A mysterious presence lurks",
        f"An eerie silence surrounds",
        f"A sense of dread pervades",
    ]

    middles = [
        f"in the shadows of {location}",
        f"within the chilling atmosphere of {location}",
        f"among the abandoned buildings of {location}",
    ]

    extra_parts = [
        f"Locals speak in hushed tones about it",
        f"People avoid going out at night, fearing an encounter",
        f"The fear of the unknown grips the town",
    ]

    endings = [
        f", known as {monster}.",
        f", and whispers of {monster} haunt the residents.",
        f", as stories of {monster} continue to terrify.",
    ]

    for i in range(5):
        beginning = random.choice(beginnings)
        middle = random.choice(middles)
        extra_part = random.choice(extra_parts)
        ending = random.choice(endings)

        sentence = f"{beginning} {middle}, {extra_part}{ending}"
        sentences.append(sentence)

    return sentences
