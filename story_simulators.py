import random


def simulate_horror_origin(location, characters):
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

    num_characters_involved = random.randint(1, len(characters))
    involved_characters = random.sample(characters, num_characters_involved)

    involvement_reasons = [
        'witnessed the event',
        'participated in the event',
        'tried to stop the event',
        'were indirectly affected by the event',
        'know a secret about the event',
    ]
    character_involvement = {}
    for character in involved_characters:
        reason = random.choice(involvement_reasons)
        character_involvement[character] = reason

    return events, character_involvement
