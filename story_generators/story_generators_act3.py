import random

from domain.character import Character
from domain.character_involvement import CharacterInvolvement
from domain.origin_descriptions import IgnoredBurial, AncientCurse, UnethicalExperiment, SupernaturalPortal, \
    ForbiddenRitual
from domain.preperation_progress import PreparationProgress


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
        'ignored_burial': IgnoredBurial,
        'ancient_curse': AncientCurse,
        'unethical_experiment': UnethicalExperiment,
        'supernatural_portal': SupernaturalPortal,
        'forbidden_ritual': ForbiddenRitual
    }

    origin_reason = random.choice(list(origin_description[monster_origin]))
    protagonist.knowledge.append(('monster_origin', monster_origin, origin_reason))

    if event_occurred:
        origin_discovery_variations = [
            f"In addition, {protagonist.first_name} discovers that the {story_world.monster_name} came into existence as a result of {origin_reason.value}.",
            f"They further find out that the origin of the {story_world.monster_name} is tied to {origin_reason.value}.",
            f"On top of this, {protagonist.first_name} uncovers that the {story_world.monster_name} is a consequence of {origin_reason.value}.",
            f"Moreover, it becomes clear to {protagonist.first_name} that the {story_world.monster_name} was born from {origin_reason.value}.",
            f"Additionally, {protagonist.first_name} unravels that the genesis of the {story_world.monster_name} is linked to {origin_reason.value}.",
            f"They also ascertain that the {story_world.monster_name}'s existence is due to {origin_reason.value}."
        ]
        origin_discovery = random.choice(origin_discovery_variations)
        story_progress.append(origin_discovery)

    breakthrough_story = ' '.join(story_progress)
    protagonist.breakthrough_actions = story_progress
    return breakthrough_story


def generate_preparation(protagonist, story_world):
    story_progress = []
    monster_origin_type, monster_origin_variation = None, None

    for knowledge in protagonist.knowledge:
        if knowledge[0] == 'monster_origin':
            monster_origin_type = knowledge[1]
            monster_origin_variation = knowledge[2]
            break

    if monster_origin_type == 'ignored_burial':
        if monster_origin_variation == IgnoredBurial.IMPROPERLY_LAIRED:
            story_progress.append(
                f"{protagonist.first_name} spends days gathering the necessary materials for a proper burial ritual. "
                "After a long search, they find what they need and prepare for the ritual.")
        elif monster_origin_variation == IgnoredBurial.FORGOTTEN_GRAVE:
            story_progress.append(f"{protagonist.first_name} journeys to the location of the forgotten grave. "
                                  "After hours of cleaning and marking, the grave now stands out as a testament to the lost soul.")
        elif monster_origin_variation == IgnoredBurial.UNBURIED_BODY:
            story_progress.append(f"{protagonist.first_name} searches high and low for the unburied remains. "
                                  "Their efforts pay off when they finally uncover the remains hidden deep within the forest.")
        protagonist.preparation_progress.append(PreparationProgress.FOUND_AND_PREPARED)

    elif monster_origin_type == 'ancient_curse':
        if monster_origin_variation == AncientCurse.CURSED_OBJECT:
            story_progress.append(f"{protagonist.first_name} dedicates their time to finding the cursed object. "
                                  "After a perilous journey, they find the object hidden in the depths of an ancient ruin.")
        elif monster_origin_variation == AncientCurse.FORBIDDEN_ACT:
            story_progress.append(
                f"{protagonist.first_name} embarks on a mission to make amends for the forbidden act. "
                "They manage to perform a deed of great kindness, hoping it will lift the curse.")
        elif monster_origin_variation == AncientCurse.ANCIENT_ARTIFACT:
            story_progress.append(
                f"{protagonist.first_name} sets out on a quest to return the ancient artifact to its original location. "
                "After overcoming numerous obstacles, they finally place the artifact back where it belongs.")
        protagonist.preparation_progress.append(PreparationProgress.FOUND_AND_DESTROYED)


    elif monster_origin_type == 'unethical_experiment':
        if monster_origin_variation == UnethicalExperiment.GONE_AWRY:
            story_progress.append(
                f"{protagonist.first_name} exhaustively searches for the scientist's notes to develop an antidote. "
                "After days of research, they concoct the antidote in a makeshift lab.")
        elif monster_origin_variation == UnethicalExperiment.MONSTROUS_CREATURES:
            story_progress.append(f"{protagonist.first_name} plans an attack to destroy the source of the mutation. "
                                  "With careful preparation, they manage to infiltrate the location and destroy the mutation source.")
        elif monster_origin_variation == UnethicalExperiment.RELEASED_PATHOGEN:
            story_progress.append(
                f"{protagonist.first_name} immerses themselves in their study, seeking a cure for the pathogen. "
                "After countless hours of work, they finally formulate a potential cure.")
        protagonist.preparation_progress.append(PreparationProgress.DEVELOPED_ANTIDOTE)

    elif monster_origin_type == 'supernatural_portal':
        if monster_origin_variation == SupernaturalPortal.ACCIDENTAL_OPENING:
            story_progress.append(
                f"{protagonist.first_name} devotes themselves to learning the sealing ritual to close the supernatural portal. "
                "After several failed attempts, they finally succeed in performing the ritual flawlessly.")
        elif monster_origin_variation == SupernaturalPortal.DIMENSIONAL_RIFT:
            story_progress.append(
                f"{protagonist.first_name} seeks out ancient texts and knowledgeable elders to learn about repairing damaged energy ley lines. "
                "After a long journey filled with cryptic puzzles and wise teachings, they finally understand how to mend the rift.")
        elif monster_origin_variation == SupernaturalPortal.OTHERWORLDLY_GATEWAY:
            story_progress.append(
                f"{protagonist.first_name} ventures into unknown territories in search of the artifact that opened the gateway. "
                "Their journey leads them to a remote cave where they find the artifact, enveloped in an eerie glow.")
        protagonist.preparation_progress.append(PreparationProgress.CLOSED_PORTAL)


    elif monster_origin_type == 'forbidden_ritual':
            if monster_origin_variation == ForbiddenRitual.DARK_FORCES:
                story_progress.append(
                    f"{protagonist.first_name} spends countless hours in ancient libraries, researching a counter-ritual to banish the dark forces. "
                    "After many sleepless nights, they finally uncover a counter-ritual that could potentially reverse the situation.")
            elif monster_origin_variation == ForbiddenRitual.MALEVOLENT_BEING:
                story_progress.append(
                    f"{protagonist.first_name} braves dangerous locations to gather materials needed for a sacred ritual to banish the malevolent being. "
                    "Their courage pays off when they manage to obtain the last material during a risky encounter.")
            elif monster_origin_variation == ForbiddenRitual.SINISTER_ENERGIES:
                story_progress.append(
                    f"{protagonist.first_name} cleanses the area affected by the sinister energies and starts preparing for a protective rite. "
                    "After days of meticulous preparation, the area starts to feel less oppressive, signalling the start of a protective barrier.")
            protagonist.preparation_progress.append(PreparationProgress.BANISHED_FORCES)

    story_progress.append(
        f"Filled with determination, {protagonist.first_name} is now ready to confront the {story_world.monster_name}.")
    return ' '.join(story_progress)

def price_of_victory(protagonist, story_world):
    preparation = protagonist.preparation_progress[-1]  # Get the most recent preparation progress
    success_rate = random.random()  # Generate a random number between 0 and 1 for success/failure

    if preparation == PreparationProgress.FOUND_AND_PREPARED:
        if success_rate < 0.8:  # 80% success chance
            outcome = f"{protagonist.first_name} successfully locates the forgotten grave and performs the necessary rites. The restless ghost haunting the {story_world.monster_name} is finally put to rest, and the creature disappears."
        else:
            outcome = f"{protagonist.first_name} attempts to perform the burial rites, but something goes wrong. The {story_world.monster_name} remains, and the protagonist must continue their search for a solution."
    elif preparation == PreparationProgress.FOUND_AND_DESTROYED:
        if success_rate < 0.8:
            outcome = f"{protagonist.first_name} destroys the cursed object, breaking the ancient curse on the {story_world.monster_name}. The creature is no longer a threat to the world."
        else:
            outcome = f"{protagonist.first_name} tries to destroy the cursed object, but the curse proves too powerful. The {story_world.monster_name} continues its reign of terror."
    elif preparation == PreparationProgress.DEVELOPED_ANTIDOTE:
        if success_rate < 0.8:
            outcome = f"{protagonist.first_name} administers the antidote, reversing the horrifying transformation of the {story_world.monster_name}. The creature returns to its original form, and the nightmare is finally over."
        else:
            outcome = f"{protagonist.first_name} attempts to use the antidote, but it fails to have the desired effect. The {story_world.monster_name} remains a danger, and the protagonist must keep searching for answers."
    elif preparation == PreparationProgress.CLOSED_PORTAL:
        if success_rate < 0.8:
            outcome = f"{protagonist.first_name} successfully completes the sealing ritual, closing the supernatural portal. The {story_world.monster_name} is banished back to its own realm, and peace is restored."
        else:
            outcome = f"{protagonist.first_name} struggles to perform the sealing ritual correctly. The portal remains open, and the {story_world.monster_name} continues to wreak havoc."
    elif preparation == PreparationProgress.BANISHED_FORCES:
        if success_rate < 0.8:
            outcome = f"{protagonist.first_name} performs the counter-ritual, banishing the dark forces controlling the {story_world.monster_name}. The creature is no more, and the darkness has been vanquished."
        else:
            outcome = f"{protagonist.first_name} tries to perform the counter-ritual, but something goes awry. The dark forces remain, and the {story_world.monster_name} continues to terrorize the land."

    return outcome
