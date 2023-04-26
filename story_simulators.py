import random
from domain.character_involvement import CharacterInvolvement


def simulate_horror_origin(story_world):
    events = []

    possible_events = [
        ('ignored_burial', 0.2),
        ('ancient_curse', 0.1),
        ('unethical_experiment', 0.3),
        ('supernatural_portal', 0.15),
        ('forbidden_ritual', 0.25),
    ]

    main_event = random.choices(possible_events, weights=[prob for _, prob in possible_events], k=1)[0]
    events.append(main_event)

    secondary_events = ['flood', 'fire', 'theft', 'festival', 'drought']
    num_secondary_events = random.randint(1, 4)
    for _ in range(num_secondary_events):
        event = random.choice(secondary_events)
        events.append(event)

    characters = story_world.characters
    num_characters_involved = random.randint(1, len(characters))
    involved_characters = random.sample(characters, num_characters_involved)

    involvement_reasons = [
        CharacterInvolvement.WITNESS,
        CharacterInvolvement.INVOLVED_IN_ORIGIN,
        CharacterInvolvement.TRIED_TO_STOP,
        CharacterInvolvement.INDIRECTLY_AFFECTED,
        CharacterInvolvement.KNOW_A_SECRET,
    ]

    for character in involved_characters:
        reason = random.choice(involvement_reasons)
        character.involvement = reason

    story_world.events = events
