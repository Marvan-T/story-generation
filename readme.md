# Story Generation Project

This project is a practical application developed as part of a university module. The goal of the project was to create a system that uses artificial intelligence to produce work that might seem creative to someone observing it. In other words, the aim was to "make something that makes something".

## Overview

The project is a story generator, specifically designed to create horror stories. It uses a combination of pre-defined story structures, random selection, and a variety of story elements to generate unique narratives. The story elements include characters, locations, and events, which are combined in different ways to create a wide variety of stories.

The project is structured into several parts:

- [`domain`](command:_github.copilot.openRelativePath?%5B%22domain%22%5D "domain"): This directory contains the core classes and enums used to represent the elements of a story, such as characters, locations, and events. It also includes the `StoryWorld` class, which is used to generate and manage the elements of a story.

- [`story_generators`](command:_github.copilot.openRelativePath?%5B%22story_generators%22%5D "story_generators"): This directory contains the functions used to generate the different parts of a story. These functions take a `StoryWorld` object as input and modify it to add new elements to the story.

- [`util`](command:_github.copilot.openRelativePath?%5B%22util%22%5D "util"): This directory contains utility functions used throughout the project, such as functions to generate random names for characters and locations.

- [`horror_grammar.py`](command:_github.copilot.openRelativePath?%5B%22horror_grammar.py%22%5D "horror_grammar.py"): This file uses the [Tracery](https://github.com/aparrish/tracery) library to define the grammar rules used to generate the text of a story.

- [`story_simulators.py`](command:_github.copilot.openRelativePath?%5B%22story_simulators.py%22%5D "story_simulators.py"): This file contains a function to simulate some events that initialize the story world.

- [`main.py`](command:_github.copilot.openRelativePath?%5B%22main.py%22%5D "main.py"): This is the entry point of the project. It creates a new `StoryWorld` object, generates a story using the functions in [`story_generators`](command:_github.copilot.openRelativePath?%5B%22story_generators%22%5D "story_generators"), and then prints the generated story.



https://github.com/Marvan-T/story-generation/assets/65969444/d072f264-7d66-4a1f-a861-9004fa56a251




## Examples of differnet output
![Example Output - 2 (mt588)](https://github.com/Marvan-T/story-generation/assets/65969444/206856d1-1bdd-4eae-89e3-64bc4b48a168)

![Example Output - 1 (mt588)](https://github.com/Marvan-T/story-generation/assets/65969444/2cf0b07f-62b4-418c-be82-bb08ec5e3c83)


## Running the Project

Install the following dependencies before running:

1. Names - to generate character names: [https://github.com/treyhunner/names](https://github.com/treyhunner/names)
   - Use the command: `pip install names`

2. Tracery for working with grammars: [https://github.com/aparrish/pytracery](https://github.com/aparrish/pytracery)
   - Use the command: `pip install tracery`

To run the project, simply execute the [`main.py`](command:_github.copilot.openRelativePath?%5B%22main.py%22%5D "main.py") file. This will generate a new story and print it to the console.

```sh
python main.py
```

