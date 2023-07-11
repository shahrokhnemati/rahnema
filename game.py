import random

def alphabet_game_name():
    names = ["Alice", "Bob", "Charlie", "David", "Emily", "Frank", "Grace", "Henry", "Isabella", "Jack",
             "Katie", "Liam", "Mia", "Noah", "Olivia", "Peter", "Quinn", "Ryan", "Sophia", "Thomas",
             "Uma", "Victoria", "William", "Xavier", "Yasmine", "Zachary"]

    chosen_name = random.choice(names)

    print("Let's play the Alphabet Game Name!")
    print("Guess a name starting with the given letter.")
    print("Type 'exit' to quit the game.\n")

    score = 0

    while True:
        print("Current Score:", score)
        print("Letter:", chosen_name[0])

        user_input = input("Enter a name: ")

        if user_input.lower() == "exit":
            break

        if user_input.lower().startswith(chosen_name[0].lower()):
            print("Correct!")
            score += 1
            chosen_name = random.choice(names)
        else:
            print("Wrong! Try again.")

    print("Final Score:", score)
    print("Thanks for playing!")

alphabet_game_name()