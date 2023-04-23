import tracery
from tracery.modifiers import base_english


def get_horror_grammar():
    horror_rules = {
        "origin": ["#act1#\n\n#act2#\n\n#act3#"],
        # ... (rest of  grammar rules)
    }

    horror_grammar = tracery.Grammar(horror_rules)
    horror_grammar.add_modifiers(base_english)

    return horror_grammar
