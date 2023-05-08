import random

from domain.character_modifiers import CharacterModifiers


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
        CharacterModifiers.NEWCOMER,
        CharacterModifiers.LOCAL_ADVENTURER,
        CharacterModifiers.CURIOUS_VISITOR,
        CharacterModifiers.LONG_TIME_RESIDENT,
        CharacterModifiers.INQUISITIVE_TRAVELER,
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
        protagonist.modifier = modifier

        modifier_description = protagonist.modifier.value.strip(", ")

        story_beginning = random.choice(story_beginnings)
        character_intro = f"{story_beginning} {starting_sentence} we meet {protagonist.name}, {modifier_description} a {selected_attributes[0]} and {selected_attributes[1]} individual."
        character_intros.append(character_intro)

    return character_intros


def generate_starting_journey(location, modifier, first_name):
    sentences = []

    if not modifier:
        return ""

    journey_options = {
        CharacterModifiers.NEWCOMER: [
            f"Having recently moved to {location}, {first_name} gets to know the area and meets some locals.",
            f"New to {location}, {first_name} spends time exploring the town and encounters a group of residents.",
            f"As a newcomer to {location}, {first_name} is eager to learn about the town's stories and meet its people.",
        ],
        CharacterModifiers.LOCAL_ADVENTURER: [
            f"While exploring the outskirts of {location}, {first_name} stumbles upon a group of locals.",
            f"On a sunny day, {first_name} sets out on an adventure in {location} and comes across a group of people.",
            f"As {first_name} enjoys the natural beauty of {location}, they cross paths with some local adventurers.",
        ],
        CharacterModifiers.CURIOUS_VISITOR: [
            f"During a stroll around {location}, {first_name} encounters a few of its friendly residents.",
            f"As {first_name} explores the town of {location}, they bump into a group of intriguing locals.",
            f"While sightseeing in {location}, {first_name} finds themselves in conversation with some of the townsfolk.",
        ],
        CharacterModifiers.LONG_TIME_RESIDENT: [
            f"As a long-time resident of {location}, {first_name} decides to reconnect with the community and meets new faces.",
            f"Living in {location} for years, {first_name} ventures out to forge new connections with fellow residents.",
            f"Having known {location} for a long time, {first_name} seizes an opportunity to engage with the local community.",
        ],
        CharacterModifiers.INQUISITIVE_TRAVELER: [
            f"As {first_name} delves into the history of {location}, they meet some knowledgeable residents.",
            f"While visiting the landmarks of {location}, {first_name} engages in conversations with locals.",
            f"As {first_name} investigates the legends surrounding {location}, they come across some interesting characters.",
        ],
    }

    options = journey_options[modifier]

    for _ in range(3):
        sentence = random.choice(options)
        sentences.append(sentence)

    return sentences


def generate_meeting_other_characters(protagonist, other_characters, story_world):
    character1, character2 = random.sample(other_characters, 2)

    normal_conversations = [
        f"{character1.first_name} and {character2.first_name} talk about the upcoming town festival.",
        f"{character1.first_name} and {character2.first_name} discuss the recent weather changes.",
        f"{character1.first_name} and {character2.first_name} share stories about their daily lives.",
        f"{character1.first_name} and {character2.first_name} chat about a new restaurant in town.",
    ]

    main_event = story_world.events[0][0]
    event_descriptions = {
        'ignored_burial': f"a series of strange occurrences after an ignored burial in {story_world.town_name}",
        'ancient_curse': f"an ancient curse that haunts the town of {story_world.town_name}",
        'unethical_experiment': f"unethical experiments conducted in a secret facility near {story_world.town_name}",
        'supernatural_portal': f"rumors of a supernatural portal hidden somewhere in {story_world.town_name}",
        'forbidden_ritual': f"disturbing rituals performed in the shadows of {story_world.town_name}",
    }

    horror_related_conversations = [
        (f"{character1.first_name} and {character2.first_name} mention {event_descriptions[main_event]}.",
         event_descriptions[main_event]),
        (f"{character1.first_name} and {character2.first_name} whisper about {story_world.horror_location}.",
         story_world.horror_location),
        (
            f"{character1.first_name} and {character2.first_name} tell a chilling ghost story related to {story_world.monster_name}.",
            story_world.monster_name),
        (
            f"{character1.first_name} and {character2.first_name} discuss the local legend of the haunted woods near {story_world.town_name}.",
            f"the haunted woods near {story_world.town_name}")
    ]

    probability_of_horror_conversation = 0.5

    if random.random() < probability_of_horror_conversation:
        conversation, knowledge_item = random.choice(horror_related_conversations)
        is_horror_related = True
        protagonist.knowledge.append((character1, character2, knowledge_item))
    else:
        conversation = random.choice(normal_conversations)
        is_horror_related = False

    return conversation, is_horror_related


def generate_isolation(protagonist, story_world):
    if protagonist.knowledge:
        knowledge_item = protagonist.knowledge[-1][2]
        explore_reasons = [
            f"Driven by curiosity, {protagonist.first_name} decides to explore the {knowledge_item} further, unknowingly placing themselves in the path of the {story_world.monster_name}.",
            f"Unable to shake the feeling that something isn't right, {protagonist.first_name} ventures to {knowledge_item}, inadvertently stepping into the lair of the {story_world.monster_name}.",
            f"Feeling a strong need to know more about {knowledge_item}, {protagonist.first_name} embarks on a journey to explore the area, only to find themselves face to face with the {story_world.monster_name}.",
        ]
        return random.choice(explore_reasons)
    else:
        subtle_approaches = [
            f"As evening falls, {protagonist.first_name} decides to take a stroll around the town to clear their thoughts, but soon finds themselves in the territory of the {story_world.monster_name}.",
            f"Feeling a bit lonely, {protagonist.first_name} takes a walk through the woods to enjoy some quiet time, only to stumble upon the {story_world.monster_name}'s hunting grounds.",
            f"Deciding to explore the town a little more, {protagonist.first_name} ends up in a secluded and eerie location, where the {story_world.monster_name} lurks in the shadows.",
        ]
        return random.choice(subtle_approaches)


def generate_first_encounter(protagonist, story_world):
    encounter_scenarios = [
        f"As {protagonist.first_name} cautiously moves forward, they catch a glimpse of the {story_world.monster_name}, and their mind struggles to comprehend the horrifying sight.",
        f"While investigating the area, {protagonist.first_name} suddenly finds themselves face to face with the {story_world.monster_name}, causing their entire perception of reality to be shaken.",
        f"{protagonist.first_name} hears an eerie sound and turns around, only to be confronted by the monstrous figure of the {story_world.monster_name}, making them question their own sanity.",
        f"The terrifying form of the {story_world.monster_name} emerges from the shadows, and as {protagonist.first_name} locks eyes with the creature, they grapple with the horrifying reality before them.",
        f"{protagonist.first_name} stumbles upon the hideous {story_world.monster_name}, and the sight of the creature defies all logic and reason, leaving them feeling utterly disoriented.",
    ]

    return random.choice(encounter_scenarios)
