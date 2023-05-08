import tracery
import random
from tracery.modifiers import base_english
from story_generators.story_generators_act1 import generate_stage1_variations, generate_character_intro, \
    generate_starting_journey, \
    generate_meeting_other_characters, generate_isolation, generate_first_encounter
from story_generators.story_generators_act2 import generate_danger_obvious, generate_pursuit, \
    generate_first_confrontation, generate_desperation
from story_generators.story_generators_act3 import generate_breakthrough, generate_preparation, price_of_victory


def get_horror_grammar(story_world):
    monster = story_world.monster_name
    horror_location = story_world.horror_location
    protagonist = story_world.get_protagonist()

    leeway_to_break = 0.7  # 70% chance of executing the functions
    guaranteed_probability = 1.0  # 100% chance of executing the functions

    stage1_variations = execute_with_probability(leeway_to_break, generate_stage1_variations, monster, horror_location)
    character_intros = execute_with_probability(leeway_to_break, generate_character_intro, story_world)
    starting_journeys = execute_with_probability(leeway_to_break, generate_starting_journey, story_world.town_name,
                                                 protagonist.modifier, protagonist.first_name)
    meeting_conversations, is_horror_related = execute_with_probability(guaranteed_probability,
                                                                        generate_meeting_other_characters,
                                                                        protagonist, story_world.get_other_characters(),
                                                                        story_world)

    isolation_sentences = execute_with_probability(leeway_to_break, generate_isolation, protagonist, story_world)
    first_encounter_scenarios = execute_with_probability(leeway_to_break, generate_first_encounter, protagonist,
                                                         story_world)

    danger_obvious = execute_with_probability(leeway_to_break, generate_danger_obvious, protagonist, story_world)
    pursuit_sentences = execute_with_probability(leeway_to_break, generate_pursuit, protagonist, story_world)
    first_confrontation = execute_with_probability(leeway_to_break, generate_first_confrontation, protagonist,
                                                   story_world)
    desperation = execute_with_probability(leeway_to_break, generate_desperation, protagonist, story_world)

    breakthrough = execute_with_probability(guaranteed_probability, generate_breakthrough, protagonist, story_world)
    preparation = execute_with_probability(guaranteed_probability, generate_preparation, protagonist, story_world)

    outcome = execute_with_probability(guaranteed_probability, price_of_victory, protagonist, story_world)

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
            "#stage9#\n#stage10#\n#stage11#"
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
        "breakthrough": breakthrough,
        "preparation": preparation,
        "priceOfVictory": outcome
    }

    horror_grammar = tracery.Grammar(horror_rules)
    horror_grammar.add_modifiers(base_english)

    return horror_grammar


def execute_with_probability(probability, function, *args, **kwargs):
    if random.random() <= probability:
        return function(*args, **kwargs)
    return ""
