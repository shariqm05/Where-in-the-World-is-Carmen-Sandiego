# Where in the World is Carmen Sandiego?

This is a digital adaptation of the classic game **"Where in the World is Carmen Sandiego?"** In this version, I've implemented **recursive pathfinding** to navigate through various locations across Europe, bringing a layer of complexity and challenge to developing and designing the source code of this game. This project was both a fun way to dive into algorithmic problem-solving and my first time dipping my toes in recursive algorithms.

## Project Overview

This game takes you on a quest to capture the elusive Carmen Sandiego. Starting in Rome, you’ll gather clues, talk to various characters, and travel across Europe, all while utilizing recursive pathfinding to progress the game and determine your next move. The game is fully text-based, and you interact with the world through simple commands.

### What Makes This Project Unique?

- **Recursive Pathfinding**: One of the key features I wanted to emphasize in this project is the use of recursive algorithms to solve the problem of navigating between locations. This method ensures that you can only travel to places that are both connected and unlocked, adding a strategic element to your pursuit of Carmen.

- **Dynamic Interactions**: As you progress, new locations, characters, and clues become available, depending on your actions. The world evolves based on your decisions, making each playthrough unique.

- **Clear Objectives**: The game is straightforward yet challenging. You win by catching Carmen, but you only have three attempts to find her. This adds a level of urgency to your decisions.

### How to Play

1. **Starting Point**: The game begins in Rome. From here, you decide your next steps—whether to talk to people, travel, or investigate clues.

2. **Traveling**: You can move between locations using the `go to` or `travel to` command. The recursive pathfinding algorithm I implemented checks if there's a valid path to your destination before you proceed.

3. **Interacting with Characters**: Use the `talk to` command to engage with the game’s characters. These conversations can unlock new locations, clues, or other characters, helping you get closer to catching Carmen.

4. **Investigating**: The `investigate` command lets you search for clues in your current location. These clues are crucial for tracking Carmen’s movements.

5. **Capturing Carmen**: Once you think you’ve pinpointed Carmen’s location, use the `catch Carmen` command. If she’s there, you win! If not, you’ll need to continue your search—but remember, you only have three tries.

### Commands Overview

- `display people`: Shows available characters at your current location.
- `display locations`: Lists locations that you can currently travel to.
- `display clues`: Displays clues you've uncovered so far.
- `go to [location]` or `travel to [location]`: Moves you to a specified location.
- `talk to [person]`: Engages in conversation with a character.
- `investigate`: Searches for clues at your current location.
- `catch Carmen`: Attempts to capture Carmen Sandiego at your current location.
- `quit` or `exit`: Exits the game.

### The Recursive Pathfinding

The heart of this game lies in its recursive pathfinding algorithm, which I designed to ensure that you can only travel along valid locations/paths you have unlocked, hence the term "pathfinding." The algorithm explores all possible routes, backtracking when necessary, to find a way to your desired destination.

### Game Endings

- **Victory**: Catch Carmen Sandiego and win the game.
- **Defeat**: Fail to find Carmen after three searches, and you lose.

## Requirements

- Python 3

## How to Run

1. Clone this repository to your local machine.
2. Run the game with Python:
   ```bash
   python carmen.py
   ```
3. Follow the prompts and enjoy the game!
