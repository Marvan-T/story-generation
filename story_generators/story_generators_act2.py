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
    hint_chance = 0.4  # Probability of discovering a hint during the pursuit

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


def generate_desperation(protagonist, story_world):
    injury_faint_chance = 0.3
    monster_distracted_chance = 0.2

    intense_sentences_sets = [
        [
            f"{protagonist.first_name} struggles to breathe as the cold, damp air fills their lungs, each gasp accompanied by a sharp pain in their chest.",
            f"The darkness engulfs {protagonist.first_name}, making it impossible to see even a few inches in front of them, heightening their fear and desperation.",
            f"Every sound sends a shiver down {protagonist.first_name}'s spine, as their senses become overwhelmed by the oppressive atmosphere and the relentless pursuit.",
        ],
        [
            f"{protagonist.first_name} feels their heart pounding in their chest, the rapid beats echoing in their ears as they try to escape the {story_world.monster_name}.",
            f"Sweat beads on {protagonist.first_name}'s forehead, the salty droplets stinging their eyes and blurring their vision in the most crucial moments.",
            f"An overwhelming sense of dread washes over {protagonist.first_name} as they realize that their situation has become direr with each passing moment.",
        ],
        [
            f"Despair settles heavily upon {protagonist.first_name}'s shoulders as they stumble through the unfamiliar terrain, feeling more lost and alone than ever before.",
            f"The eerie silence is deafening, punctuated only by {protagonist.first_name}'s ragged breaths and the distant, haunting sounds of the {story_world.monster_name}.",
            f"{protagonist.first_name}'s legs feel like lead, their muscles screaming in protest as they force themselves to continue running from the relentless {story_world.monster_name}.",
        ],
    ]

    intense_sentences = random.choice(intense_sentences_sets)
    intense_description = ' '.join(intense_sentences)

    result = random.random()

    # Let the protagonist get injured or faint with a probability. There is a chance that the monster will be distracted by something else as well.
    if result < injury_faint_chance:
        injury_or_faint = random.choice(["injury", "faint"])

        if injury_or_faint == "injury":
            protagonist.status = "injured"
            injury_description = f"{protagonist.first_name} suffers a painful injury while trying to escape the {story_world.monster_name}, which hinders their movement and forces them to leave something valuable behind."
            return intense_description + ' ' + injury_description

        elif injury_or_faint == "faint":
            protagonist.status = "fainted"
            faint_description = f"Exhausted and overwhelmed, {protagonist.first_name} loses consciousness. They wake up days later in a more dangerous and isolated place, disoriented and struggling to piece together what happened."
            return intense_description + ' ' + faint_description

    elif result < injury_faint_chance + monster_distracted_chance:
        distraction_description = f"Unexpectedly, the {story_world.monster_name} becomes distracted by something and leaves {protagonist.first_name}'s sight, providing a brief moment of relief."
        return intense_description + ' ' + distraction_description

    else:
        normal_description = f"{protagonist.first_name}'s heart pounds as they continue to evade the {story_world.monster_name}, feeling more isolated and hopeless than ever before."
        return intense_description + ' ' + normal_description
