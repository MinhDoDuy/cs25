#1 Guessing Game
import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

number = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < number:
            print("Too Small")
        elif guess > number:
            print("Too Large")
        else:
            print("Just Right")
            break
    except ValueError:
        pass