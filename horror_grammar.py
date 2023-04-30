import tracery
from tracery.modifiers import base_english
from story_generators.story_generators_act1 import generate_stage1_variations, generate_character_intro, generate_starting_journey, \
    generate_meeting_other_characters, generate_isolation, generate_first_encounter
from story_generators.story_generators_act2 import generate_danger_obvious, generate_pursuit, \
    generate_first_confrontation, generate_desperation


def get_horror_grammar(story_world):
    monster = story_world.monster_name
    horror_location = story_world.horror_location
    protagonist = story_world.get_protagonist()

    stage1_variations = generate_stage1_variations(monster, horror_location)
    character_intros = generate_character_intro(story_world)
    starting_journeys = generate_starting_journey(story_world.town_name, protagonist.modifier, protagonist.first_name)
    meeting_conversations, is_horror_related = generate_meeting_other_characters(protagonist,
                                                                                 story_world.get_other_characters(),
                                                                                 story_world)

    isolation_sentences = generate_isolation(protagonist, story_world)
    first_encounter_scenarios = generate_first_encounter(protagonist, story_world)

    danger_obvious = generate_danger_obvious(protagonist, story_world)
    pursuit_sentences = generate_pursuit(protagonist, story_world)
    first_confrontation = generate_first_confrontation(protagonist, story_world)
    desperation = generate_desperation(protagonist, story_world)

    horror_rules = {
        "origin": ["#act1#\n\n#act2#\n\n#act3#"],

        "act1": [
            "#stage1#\n#stage2#\n#stage3#\n#stage4#"
        ],
        "stage1": [
            "The hidden monster: #monsterHint#.",
        ],
        "stage2": [
            "Introducing the protagonist: #characterIntro# "
            "#startingJourney# "
            "#meetingOtherCharacters#.",
        ],
        "stage3": [
            "The journey begins: #isolation#."
        ],
        "stage4": [
            "Meeting the monster: #firstEncounter#."
        ],

        "act2": [
            "#stage5#\n#stage6#\n#stage7#\n#stage8#"
        ],
        "stage5": [
            "The turning point: #dangerObvious#."
        ],
        "stage6": [
            "Pursuit: #pursuit#."
        ],
        "stage7": [
            "The first confrontation: #firstConfrontation#."
        ],
        "stage8": [
            "Desperation: #desperation#."
        ],

        "act3": [
            "#stage9#\n#stage10#\n#stage11#\n#stage12#"
        ],
        "stage9": [
            "Breakthrough: #breakthrough#."
        ],
        "stage10": [
            "Preparing for the final confrontation: #preparation#."
        ],
        "stage11": [
            "The price of victory: #priceOfVictory#."
        ],
        "stage12": [
            "The fallout: #fallout#."
        ],

        "monsterHint": stage1_variations,
        "characterIntro": character_intros,
        "startingJourney": starting_journeys,
        "meetingOtherCharacters": meeting_conversations,
        "isolation": isolation_sentences,
        "firstEncounter": first_encounter_scenarios,
        "dangerObvious": danger_obvious,
        "pursuit": pursuit_sentences,
        "firstConfrontation": first_confrontation,
        "desperation": desperation,
        "breakthrough": ["..."],
        "preparation": ["..."],
        "priceOfVictory": ["..."],
        "fallout": ["..."]
    }

    horror_grammar = tracery.Grammar(horror_rules)
    horror_grammar.add_modifiers(base_english)

    return horror_grammar
