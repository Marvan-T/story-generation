# Marvan Tennekoon (mt588), COMP6590 - Practical Project
from story_simulators import simulate_horror_origin
from util.locations import get_horror_location
from util.monster_names import get_random_monster_name
from domain.character import Character
from domain.character_involvement import CharacterInvolvement
from util.town_names import get_town
import names

class StoryWorld:
    def __init__(self):
        self.events = None
        self.characters = self.generate_characters(6)
        self.horror_location = get_horror_location()
        self.monster_name = get_random_monster_name()
        self.town_name = get_town()
        simulate_horror_origin(self)

    def generate_characters(self, num_characters):
        unique_names = set()
        while len(unique_names) < num_characters:
            unique_names.add(names.get_full_name())

        character_names = list(unique_names)

        characters = [Character(character_names.pop(0), CharacterInvolvement.PROTAGONIST),
                      Character(character_names.pop(0), CharacterInvolvement.VICTIM)]

        for _ in range(num_characters - 2):  # subtract 2 to account for the protagonist and victim
            characters.append(Character(character_names.pop(0)))

        return characters

    def get_protagonist(self):
        for character in self.characters:
            if character.involvement == CharacterInvolvement.PROTAGONIST:
                return character

    # Returns a list of all characters except the protagonist and victim
    def get_other_characters(self):
        other_characters = []
        for character in self.characters:
            if character.involvement != CharacterInvolvement.PROTAGONIST or character.involvement != CharacterInvolvement.VICTIM:
                other_characters.append(character)
        return other_characters
