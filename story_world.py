from story_simulators import simulate_horror_origin
from util.locations import get_horror_location
from util.monster_names import get_random_monster_name
from util.character_names import get_random_name
from domain.character import Character
from domain.character_involvement import CharacterInvolvement


class StoryWorld:
    def __init__(self):
        self.character_involvement = None
        self.events = None
        self.characters = self.generate_characters(6)
        self.location = get_horror_location()
        self.monster_name = get_random_monster_name()
        simulate_horror_origin(self)

    def generate_characters(self, num_characters):
        characters = [Character("protagonist", CharacterInvolvement.PROTAGONIST),
                      Character("victim", CharacterInvolvement.VICTIM)]

        for _ in range(num_characters - 2):  # subtract 2 to account for the protagonist and victim
            characters.append(Character("other"))

        return characters
