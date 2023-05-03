import random

from domain.character import Character
from domain.character_involvement import CharacterInvolvement


def generate_breakthrough(protagonist, story_world):
    story_progress = []
    days_passed = random.randint(2, 4)
    story_progress.append(
        f"{days_passed} days have passed since {protagonist.first_name}'s harrowing escape from the {story_world.monster_name}. The trauma lingers, haunting their every waking moment.")

    event_occurred = False

    # mutually exclusive - 1
    if protagonist.knowledge:
        met_characters = [item for item in protagonist.knowledge if isinstance(item[0], Character)]

        if met_characters:
            met_character_tuple = random.choice(met_characters)
            met_character = met_character_tuple[0]
            character_role = met_character.involvement
            motive = f"Determined to confront their fears and find answers, {protagonist.first_name} decides to reconnect with {met_character.first_name}, hoping to gather more information and discuss their experiences."

            if character_role == CharacterInvolvement.VICTIM:
                interaction = f"{met_character.first_name} offers a truthful account of their observations regarding the {story_world.monster_name}, revealing that the creature seems to avoid water."
                protagonist.knowledge.append(("witness_info", "monster_avoids_water"))
            elif character_role == CharacterInvolvement.INVOLVED_IN_ORIGIN:
                interaction = f"{met_character.first_name} hesitantly admits to being involved in the {story_world.monster_name}'s creation and discloses that the creature is sensitive to a specific sound frequency."
                protagonist.knowledge.append(("origin_info", "monster_sensitive_frequency"))
            elif character_role == CharacterInvolvement.TRIED_TO_STOP:
                interaction = f"{met_character.first_name} shares honest details about their efforts to intervene and stop the {story_world.monster_name}, revealing that they discovered a specific type of plant that seemed to weaken the monster."
                protagonist.knowledge.append(("stop_attempt_info", "monster_weakened_by_plant"))
            elif character_role == CharacterInvolvement.INDIRECTLY_AFFECTED:
                interaction = f"{met_character.first_name} expresses empathy for {protagonist.first_name}'s ordeal and shares their own experiences related to the {story_world.monster_name}, mentioning that the creature seems to be more active during the night."
                protagonist.knowledge.append(("indirectly_affected_info", "monster_more_active_at_night"))
            else:  # KNOW_A_SECRET
                interaction = f"{met_character.first_name} remains secretive but subtly alludes to the {story_world.monster_name}'s terrifying origins, hinting at the existence of an ancient artifact that could control or banish the monster."
                protagonist.knowledge.append(("secret_info", "ancient_artifact"))

            story_progress.append(motive)
            story_progress.append(interaction)

            for info in protagonist.knowledge[-len(met_characters):]:
                research_story = []
                if info[1] == "monster_avoids_water":
                    research = f"{protagonist.first_name} investigates further and learns that the {story_world.monster_name} can be weakened or defeated using water, possibly due to its aversion to the element. To defeat the monster, {protagonist.first_name} must find a way to use water against it in their next encounter."
                    protagonist.knowledge.append(("research_info", "use_water_against_monster"))
                elif info[1] == "monster_sensitive_frequency":
                    research = f"{protagonist.first_name} conducts more research and discovers that the {story_world.monster_name} can be incapacitated by emitting a specific sound frequency, exploiting its sensitivity to disrupt its actions. {protagonist.first_name} decides to create a device that can emit this frequency to use in the battle against the monster."
                    protagonist.knowledge.append(("research_info", "create_frequency_device"))
                elif info[1] == "monster_weakened_by_plant":
                    research = f"{protagonist.first_name} delves into the properties of the plant mentioned by {met_character.first_name} and realizes that its essence can be used to create a concoction that weakens the {story_world.monster_name}, making it vulnerable to attack. {protagonist.first_name} must collect the plant and prepare the concoction before facing the monster again."
                    protagonist.knowledge.append(("research_info", "prepare_plant_concoction"))
                elif info[1] == "monster_more_active_at_night":
                    research = f"Taking note of the {story_world.monster_name}'s heightened activity at night, {protagonist.first_name} strategizes that the best time to confront and defeat the creature would be during daylight hours, when it is less active. {protagonist.first_name} plans to confront the monster during the day to increase their chances of success."
                    protagonist.knowledge.append(("research_info", "confront_monster_during_day"))
                elif info[1] == "ancient_artifact":
                    research = f"{protagonist.first_name} spends countless hours researching the ancient artifact hinted at by {met_character.first_name}. They learn that it holds the power to control or banish the {story_world.monster_name}, but must be found and activated to do so. {protagonist.first_name} is determined to locate the artifact and use it to put an end to the monster's reign of terror."
                    protagonist.knowledge.append(("research_info", "find_and_activate_artifact"))

                research_story.append(research)
                story_progress.extend(research_story)
                event_occurred = True

    # mutually exclusive - 2 (only if #mutually exclusive - 1 did not happen)
    if not event_occurred and any('hint' in attribute for attribute in protagonist.knowledge):
        clue = [item for item in protagonist.knowledge if item[0] == "hint"]
        if clue:
            hint = clue[0][-1]
            investigation = f"Recalling the hint they found - {hint}, {protagonist.first_name} decides to investigate further. They search local newspapers and talk to residents, hoping to uncover the truth about the {story_world.monster_name}."
            story_progress.append(investigation)
        event_occurred = True

    # mutually exclusive - 3 (only if #mutually exclusive - 1 and #mutually exclusive - 2 did not happen)
    if not event_occurred and random.random() < 0.5:
        ally = random.choice(["a skilled investigator", "a knowledgeable historian", "an experienced monster hunter"])
        ally_interaction = f"While feeling overwhelmed and desperate, {protagonist.first_name} encounters {ally}, who offers to help them in their quest for the truth. With their unique skills and resources, they provide fresh insights into the {story_world.monster_name}'s origins."
        story_progress.append(ally_interaction)
        event_occurred = True

    # mutually exclusive - 4 (only if #mutually exclusive - 1, #mutually exclusive - 2, and #mutually exclusive - 3 did not happen)
    if not event_occurred:
        location_revisit = f"Filled with trepidation, {protagonist.first_name} retraces their steps to the location of their initial encounter with the {story_world.monster_name}. The chilling atmosphere is palpable, but the monster is nowhere to be seen. During their visit, {protagonist.first_name} inadvertently uncovers a crucial element that could help defeat the {story_world.monster_name}, and then returns home with newfound determination."
        story_progress.append(location_revisit)
        event_occurred = True

    monster_origin = story_world.events[0][0]
    origin_description = {
        'ignored_burial': [
            "an improperly laid to rest spirit, which could be appeased by performing a proper burial ritual",
            "a restless ghost due to a forgotten grave, which can be pacified by cleaning and marking the grave",
            "an angry spirit of an unburied body, which can be calmed by finding and burying the remains"
        ],
        'ancient_curse': [
            "a powerful ancient curse, which can be broken by finding and destroying the cursed object",
            "a deadly curse unleashed by a forbidden act, which can be lifted by making amends for the act",
            "a malediction linked to an ancient artifact, which can be nullified by returning the artifact to its original location"
        ],
        'unethical_experiment': [
            "an unethical experiment gone awry, which may be reversed by finding the scientist's notes and developing an antidote",
            "a failed experiment resulting in monstrous creatures, which can be neutralized by destroying the source of their mutation",
            "a dangerous experiment that released a pathogen, which can be contained by discovering a cure and administering it to the affected population"
        ],
        'supernatural_portal': [
            "a supernatural portal accidentally opened, which can be closed by performing a sealing ritual",
            "a dimensional rift connecting to another realm, which can be sealed by repairing the damaged energy ley lines",
            "an otherworldly gateway inadvertently activated, which can be shut down by finding and deactivating the artifact that opened it"
        ],
        'forbidden_ritual': [
            "a forbidden ritual that unleashed dark forces, which can be stopped by banishing the dark forces using a counter-ritual",
            "a dark summoning that brought forth a malevolent being, which can be banished by completing a sacred ritual",
            "an occult ceremony that invoked sinister energies, which can be dispelled by cleansing the area and performing a protective rite"
        ]
    }

    origin_reason = random.choice(origin_description[monster_origin])
    protagonist.knowledge.append(('monster_origin', monster_origin, random.choice(origin_description[monster_origin])))

    if event_occurred:
        origin_discovery = f"{protagonist.first_name} learns that the {story_world.monster_name} is the result of {origin_reason}."
        story_progress.append(origin_discovery)

    breakthrough_story = ' '.join(story_progress)
    protagonist.breakthrough_actions = story_progress
    return breakthrough_story
