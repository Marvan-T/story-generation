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
