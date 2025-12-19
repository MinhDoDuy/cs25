import random

def main():
    level = get_level()
    score = 0

    for i in range(10):
        print("question ", i + 1)
        x, y = generate_problem(level)
        if ask_question(x, y):
            score += 1

    print("Score: ", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
        except ValueError:
            pass

def generate_problem(level):
    if level == 1:
        return random.randint(0, 9), random.randint(0,9)
    elif level == 2:
        return random.randint(10, 99), random.randint(10,99)
    else:
        return random.randint(100, 999), random.randint(100, 999)

def ask_question(x, y):
    answer = x + y
    attempts = 0

    while attempts < 3:
        try:
            user_answer = int(input(f"{x} + {y} = "))
            if user_answer == answer:
                return True
            else:
                print("EEE")
        except ValueError:
            print("EEE")
        attempts += 1

    print(f"{x} + {y} = {answer}")
    return False

if __name__ == "__main__":
    main()
