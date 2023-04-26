import tracery
from tracery.modifiers import base_english
from story_generators import generate_stage1_variations

def get_horror_grammar():
    horror_rules = {
        "origin": ["#act1#\n\n#act2#\n\n#act3#"],
        "act1": [
            "#stage1#\n#stage2#\n#stage3#\n#stage4#"
        ],
        "stage1": [
            "The hidden monster: #monsterHint#."
        ],
        # ... (rest of  grammar rules)

        "monsterHint": "test",
    }



    horror_grammar = tracery.Grammar(horror_rules)
    horror_grammar.add_modifiers(base_english)

    return horror_grammar
