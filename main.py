from horror_grammar import get_horror_grammar
import geonamescache
import random

if __name__ == "__main__":
    horror_grammar = get_horror_grammar()
    generated_story = horror_grammar.flatten("#origin#")
    print(generated_story)

    # Todo: set up the character name generator and location name generator
