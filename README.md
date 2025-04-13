# Snake Game

## Overview
This is a simple Snake Game implemented in Python using the `turtle` module. The player controls a snake that grows in size by eating food while avoiding collisions with the walls and its own tail. The game ends when the snake collides with a wall or itself.

---

## Files
- `snake_game.py`: Main game logic and setup.  
- `snake.py`: Defines the `Snake` class for controlling the snake's behavior.  
- `food.py`: Defines the `Food` class for generating food on the game board.  
- `score_board.py`: Defines the `Scoreboard` class for tracking and displaying the score.  

---

## Features
- **Snake Movement**: The snake moves in four directions (up, down, left, right).  
- **Food**: Randomly placed food that the snake eats to grow.  
- **Score Tracking**: Displays the current score on the screen.  
- **Game Over**: Ends the game when the snake collides with the wall or itself.  
- **Green Border**: A visual green border around the game area.  

---

## How to Play
Use the arrow keys to control the snake's movement:
- **Up**: Move up  
- **Down**: Move down  
- **Left**: Move left  
- **Right**: Move right  

Eat the red food to increase your score and grow the snake.  
Avoid colliding with the walls or the snake's tail.  

---

## Classes

### Snake
Handles the creation, movement, and growth of the snake.  
**Methods**:  
- `create_snake()`  
- `move()`  
- `up()`  
- `down()`  
- `left()`  
- `right()`  
- `extend()`  

### Food
Generates food at random positions on the board.  
**Method**:  
- `refresh()`  

### Scoreboard
Tracks and displays the score.  
**Methods**:  
- `increase_score()`  
- `clear_score()`  
- `show_score()`  
- `game_over()`  

---

## Requirements
- Python 3.x  
- `turtle` module (built-in)  

---

## How to Run
1. Place all files in the same directory.  
2. Run `snake_game.py`:
   ```bash
   python snake_game.py
   ```