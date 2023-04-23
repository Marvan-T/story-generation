from HorrorGrammar import get_horror_grammar


if __name__ == "__main__":
    horror_grammar = get_horror_grammar()
    generated_story = horror_grammar.flatten("#origin#")
    print(generated_story)
