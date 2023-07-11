import random

def fam_game():
    names = ["Ali", "newyork", "mina", "mona", "Emily", "abi", "ghermez", "sabz", "nooshabe", "doogh",
             "amin", "amir", "tehran", "amrica", "iran", "Peter", "zard", "kerman", "yazd", "shiraz",
             "saber", "reza", "ghormesabzi", "pasta", "yasaman", "Zachary"]

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
            score += 10
            chosen_name = random.choice(names)
        else:
            print("Wrong! Try again.")

    print("Final Score:", score)
    print("Thanks for playing!")

fam_game()