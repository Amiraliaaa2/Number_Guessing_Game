# 🎮 Number Guessing Game
![Free License](https://img.shields.io/badge/License-Free-brightgreen.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Easy Afzar](https://img.shields.io/badge/Easy%20Afzar-Tailored%20Development-red?style=flat&logo=https://imgur.com/a/xaNKqQFlink=https://easyafzar.com)

## 📋 Table of Contents
- [Overview](##Overview)
- [Features](##Features)
- [Gameplay](##Gameplay)
- [Installation](##Installation)
- [Usage](##Usage)
- [Customization](##Customization)
- [Code Structure](##Code-Structure)
- [Example Output](##Example-Output)
- [Testing](##Testing)
- [Contribution Guidelines](##Contribution-Guidelines)
- [Future Enhancements](##Future-Enhancements)
- [License](##License)


## 📝 Overview
** The Number Guessing Game is a fun and interactive Python program where the player attempts to guess a randomly selected number between 1 and 100. The game offers feedback on whether the guess is too high, too low, or correct, all while keeping track of the number of attempts made. It’s an excellent project for beginners to get familiar with Python programming concepts like loops, conditionals, and user input. **

## ✨ Features
- Random Number Generation: A random number between 1 and 100 is generated at the start of each game.
- Interactive Gameplay: Players receive feedback on their guesses, helping them zero in on the correct number.
- Attempt Limitation: Players have up to 10 attempts to guess the correct number, after which the game ends.
- Error Handling: The game gracefully handles invalid inputs, prompting the user to enter a valid number.
- Customizable Settings: Easily adjust the number range and attempt limit by modifying the code.

## 🎮 Gameplay
1. Game Start: Upon running the game, the player is welcomed and informed that a number between 1 and 100 has been randomly selected.
2. Making Guesses: The player is prompted to enter their guess. After each guess, the game provides feedback:
   - "Higher!" if the guess is too low.
   - "Lower!" if the guess is too high.
   - "Congratulations! You guessed the number!" if the guess is correct.
3. Winning: If the player guesses the correct number within the allotted attempts, they win the game.
4. Losing: If the player fails to guess the correct number within 10 attempts, the game reveals the correct number and ends.

## 💻 Installation
To run the Number Guessing Game on your local machine, follow these steps:
1. Clone the Repository:
  ```bash
    git clone https://github.com/your-username/number-guessing-game.git
    cd number-guessing-game
  ```
2. Ensure Python is Installed: Make sure you have Python 3.x installed. You can download it from
[Python's official website.](https://www.python.org/downloads/)
3. Run the Game:
  ```bash
    python guessing_game.py
  ```

🚀 Usage
Once the game is running:
1. Follow the on-screen instructions to guess the number.
2. Input your guesses when prompted.
3. Enjoy the game and try to guess the number in as few attempts as possible!

## 🔧 Customization
You can easily customize the game to make it more challenging or adapt it to different scenarios:
- Change the Number Range: Modify the `get_random_number` function to generate a number in a different range.
- Adjust the Maximum Attempts: Change the `max_attempts` variable in the `play_game` function to allow more or fewer guesses.
Example:
```python
def get_random_number():
    return random.randint(1, 500)  # Changes the range to 1-500

max_attempts = 15  # Allows 15 guesses instead of 10
```

## 📂 Code Structure
`guessing_game.py` : The main script containing the game logic.
  - Functions:
    - `get_random_number()`: Generates a random number within a specified range.
    - `evaluate_guess(guess, correct_number)`: Evaluates the user's guess and returns feedback.
    - `play_game()`: Manages the overall game flow, including user interaction and game logic.

## 📊 Example Output
Here’s what the game output might look like during a session:
```vbnet
Welcome to the Number Guessing Game!
I have chosen a number between 1 and 100. Can you guess it?
What is your guess? 45
Higher!
What is your guess? 75
Lower!
What is your guess? 63
Congratulations! You guessed the number in 3 attempts!
```
## 🧪 Testing
To ensure the game runs smoothly:
- Manual Testing: Run the game multiple times, entering both valid and invalid inputs to observe the behavior.
- Unit Testing: Implement unit tests to validate the behavior of individual functions like `evaluate_guess` and `get_random_number`.

Example of a basic unit test using unittest:
```python
import unittest
from guessing_game import evaluate_guess

class TestGuessingGame(unittest.TestCase):
    def test_evaluate_guess(self):
        self.assertEqual(evaluate_guess(50, 75), "Higher!")
        self.assertEqual(evaluate_guess(85, 75), "Lower!")
        self.assertEqual(evaluate_guess(75, 75), "Congratulations! You guessed the number!")

if __name__ == "__main__":
    unittest.main()
```

## 🤝 Contribution Guidelines
We welcome contributions to improve this project! Here's how you can help:
1. Fork the Repository: Click on the "Fork" button at the top right of this page.
2. Clone the Forked Repository:
```bash
git clone https://github.com/your-username/number-guessing-game.git
```
3. Create a Branch:
```bash
git checkout -b feature-name
```
4. Make Your Changes: Implement your feature, fix bugs, or improve documentation.
5. Commit and Push:
```bash
git add .
git commit -m "Description of changes"
git push origin feature-name
```
6. Submit a Pull Request: Go to the original repository on GitHub and click on "New Pull Request."

## 🔮 Future Enhancements
Some ideas for future improvements:
- Difficulty Levels: Implement different difficulty levels by adjusting the number range and attempts.
- Leaderboard: Add a feature to track the best scores (fewest attempts) across multiple sessions.
- GUI Version: Develop a graphical user interface version using libraries like Tkinter or PyQt.

## 📜 License
This project is licensed under the MIT License. You are free to use, modify, and distribute this software as long as the original license is included.
