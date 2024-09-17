
# Snake, Water, Gun - Python Game 🐍💧🔫

A simple yet exciting Python command-line game inspired by the classic *Rock, Paper, Scissors* concept with a fun twist! In this game, the player challenges the computer by choosing between Snake, Water, or Gun.

## How to Play
- The game prompts the player to choose between **Snake (s)**, **Water (w)**, or **Gun (g)**.
- The computer randomly picks one of the three choices.
- The result of the game is displayed, declaring if the player won, lost, or if it's a draw.

### Rules:
- **Snake vs. Water**: Snake drinks the Water 🐍💧 (Snake wins)
- **Snake vs. Gun**: Gun shoots the Snake 🔫🐍 (Gun wins)
- **Water vs. Gun**: Water douses the Gun 💧🔫 (Water wins)
- If both the player and computer make the same choice, it's a draw!

## Code Overview

```python
import random

'''
1 for snake
-1 for water
0 for gun
'''
# Computer randomly selects an option
computer = random.choice([1, -1, 0])

# Player input for their choice
you_str = input("Enter your Choice : ")
print("******************")

# Dictionaries to map user input and display choices
youdict = {"s": 1, "w": -1, "g": 0}
reverse_dict = {1: "Snake", -1: "Water", 0: "Gun"}

# Player's choice mapped from input
you = youdict[you_str]

# Display player and computer choices
print(f"You chose: {reverse_dict[you]}\nComputer chose: {reverse_dict[computer]}")

# Game result logic
if computer == you:
    print("It's a draw!")
else:
    if computer == -1 and you == 1:
        print("You Win! Congratulations")    
    elif computer == -1 and you == 0:
        print("You lose! Try again")    
    elif computer == 1 and you == -1:
        print("You lose! Try again")    
    elif computer == 1 and you == 0:
        print("You Win! Congratulations")    
    elif computer == 0 and you == -1:
        print("You Win! Congratulations")    
    elif computer == 0 and you == 1:
        print("You lose! Try again") 
    else:
        print("Something went wrong! Try again") 
```

## How to Run

1. Clone or download this repository.
2. Make sure Python is installed on your system.
3. Run the Python script using the command below:

```bash
python snake_water_gun.py
```

4. Follow the prompt to input your choice (`s`, `w`, or `g`).

## Future Improvements
- Add a graphical user interface (GUI) to make the game more interactive.
- Implement score tracking for multiple rounds.

## License
This project is licensed under the MIT License. Feel free to modify and use the code as needed!
