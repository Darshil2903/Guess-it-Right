# Guess It Right

A command-line number-guessing game in Python. The computer picks a secret number from **1 to 100**, and you keep guessing until you find it.

## How to play

```bash
python "guees it right.py"
```

- Type a number and press Enter.
- The game tells you to go **higher** or **lower**.
- When you hit the number, it shows how many guesses you took.

```
🙏welcome to the game🙏

enter the number:50
choose the greater number
enter the number:75
choose the lesser number
enter the number:63
you guess it right!!
you have guess it in 3 times
```

## How it works

- `random.randint(1, 100)` picks the secret number.
- A `while` loop keeps asking until the guess matches, counting attempts.
- `gamewin()` compares the guess with the secret number and prints a hint.

The best strategy is binary search: always guess the middle of the remaining range. That finds any number from 1 to 100 in **7 guesses or fewer**.

## Ideas for next time

- Handle non-numeric input without crashing (`try`/`except ValueError`)
- Add a guess limit and difficulty levels
- Offer a "play again" option
