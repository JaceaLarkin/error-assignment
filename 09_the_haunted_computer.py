import random
import time

messages = [
    "I can see you.",
    "Don't look behind you.",
    "You are not alone.",
    "The lights will go out soon.",
    "I know your name."
]

for i in range(10):
    number = random.randint(0, 5)

    try:
        print(messages[number])

    except IndexError:
        print("ERROR: Something is trying to communicate...")

    finally:
        print("The computer is watching you.")
    print()
    time.sleep(1)