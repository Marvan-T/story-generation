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


def generate_character_intro(story_world, num_sentences=5):
    protagonist = story_world.get_protagonist()
    town_name = story_world.town_name

    character_attributes = [
        "curious",
        "determined",
        "kind-hearted",
        "resourceful",
        "skeptical",
        "brave",
        "compassionate",
        "witty",
    ]

    selected_attributes = random.sample(character_attributes, 2)

    starting_sentences = [
        f"in the small town of {town_name},",
        f"on the outskirts of {town_name},",
        f"deep within the heart of {town_name},",
        f"in the quiet village of {town_name},",
    ]

    modifiers = [
        "a newcomer to the area,",
        "a local with a sense of adventure,",
        "a curious visitor,",
        "a long-time resident,",
        "an inquisitive traveler,",
    ]

    story_beginnings = [
        "Our story begins",
        "Our tale unfolds",
        "The adventure starts",
        "It all commences",
    ]

    character_intros = []

    for _ in range(num_sentences):
        starting_sentence = random.choice(starting_sentences)
        modifier = random.choice(modifiers)

        # Set the protagonist's modifier
        protagonist.modifier = modifier.strip(", ")

        # Combine the elements in a sentence
        story_beginning = random.choice(story_beginnings)
        character_intro = f"{story_beginning} {starting_sentence} we meet {protagonist.name}, {modifier} a {selected_attributes[0]} and {selected_attributes[1]} individual."
        character_intros.append(character_intro)

    return character_intros

