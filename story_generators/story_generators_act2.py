import random

def generate_danger_obvious(protagonist, story_world):
    danger_scenarios = [
        f"Panicked, {protagonist.first_name} tries to flee, but the {story_world.monster_name} relentlessly pursues them, making it clear that there's no escape.",
        f"As {protagonist.first_name} desperately searches for a way out, the {story_world.monster_name} lets out a spine-chilling roar, confirming the severity of the danger.",
        f"The {story_world.monster_name} suddenly lunges at {protagonist.first_name}, forcing them to narrowly dodge its attack, and the terrifying reality of their situation becomes all too clear.",
        f"With a sinister grin, the {story_world.monster_name} corners {protagonist.first_name}, leaving them with no choice but to confront the horrifying creature.",
        f"As the {story_world.monster_name} inches closer, its malevolent intentions become undeniably apparent, and {protagonist.first_name} knows they must find a way to survive the nightmarish ordeal.",
    ]

    return random.choice(danger_scenarios)

def generate_pursuit(protagonist, story_world):
    hint_chance = 0.5  # Probability of providing a hint

    hints = {
        "ignored_burial": "an unmarked grave",
        "ancient_curse": "an ancient artifact",
        "unethical_experiment": "a hidden laboratory",
        "forbidden_ritual": "a mysterious altar",
        "supernatural_portal": "a strange portal"
    }

    hint_present = random.random() < hint_chance
    hint = ""

    if hint_present:
        hint_key = story_world.events[0][0]
        hint = hints[hint_key]
        protagonist.knowledge.append(("hint", "monster origin", hint))

    pursuit_scenarios = [
        f"While being chased by the {story_world.monster_name}, {protagonist.first_name} stumbles upon {hint} and becomes more determined to confront their inner demons and escape the nightmare." if hint_present else f"While being chased by the {story_world.monster_name}, {protagonist.first_name} becomes more determined to confront their inner demons and escape the nightmare.",
        f"The pursuit of the {story_world.monster_name} forces {protagonist.first_name} to face their deepest fears, pushing them to their limits. During the chase, they catch a glimpse of {hint}." if hint_present else f"The pursuit of the {story_world.monster_name} forces {protagonist.first_name} to face their deepest fears, pushing them to their limits.",
        f"Cornered by the {story_world.monster_name}, {protagonist.first_name} starts to hear faint whispers of {hint}, urging them to confront their past and find the strength to fight." if hint_present else f"Cornered by the {story_world.monster_name}, {protagonist.first_name} is urged to confront their past and find the strength to fight.",
        f"In the midst of the harrowing pursuit, {protagonist.first_name} discovers {hint}, which forces them to confront the source of the {story_world.monster_name}'s existence and their own fears." if hint_present else f"In the midst of the harrowing pursuit, {protagonist.first_name} is forced to confront the source of the {story_world.monster_name}'s existence and their own fears.",
    ]

    return random.choice(pursuit_scenarios)

def generate_first_confrontation(protagonist, story_world):
    failure_reasons = {
        "lack of information": "fumbling in the dark",
        "wrong assumptions": "misguided by their own misconceptions",
        "inner conflicts": "held back by their own doubts"
    }

    chosen_reason = random.choice(list(failure_reasons.values()))

    confrontation_scenarios = [
        f"Gathering their courage, {protagonist.first_name} attempts to fight back against the {story_world.monster_name}, but their efforts prove futile as they find themselves {chosen_reason}.",
        f"With a surge of adrenaline, {protagonist.first_name} tries to stand up to the {story_world.monster_name}, only to realize that {chosen_reason} is preventing them from making any progress.",
        f"Desperate to survive, {protagonist.first_name} faces the {story_world.monster_name} head-on but soon discovers that {chosen_reason} is a significant obstacle in their struggle.",
        f"{protagonist.first_name} musters all their strength to confront the {story_world.monster_name}, but their attempts are in vain as they grapple with the challenges posed by {chosen_reason}.",
    ]

    return random.choice(confrontation_scenarios)