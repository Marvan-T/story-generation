# Marvan Tennekoon (mt588), COMP6590 - Practical Project
from horror_grammar import get_horror_grammar
from domain.story_world import StoryWorld

if __name__ == "__main__":
    story_world = StoryWorld()
    horror_grammar = get_horror_grammar(story_world)
    generated_story = horror_grammar.flatten("#origin#")
    print(generated_story)



