import random

moves = ["Rock", "Paper", "Scissors"]
comp_choice = random.randint(0,2)

player_choice = int(input("Which do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

player = moves[player_choice]
comp = moves[comp_choice]

print(f"You picked {player}, and the computer chose {comp}.")

if player == "Rock":
    if comp == "Paper":
        print("You loose.")
    elif comp == "Scissors":
        print("You Win!")
    else:
        print("It's a draw.")
elif player == "Paper":
    if comp == "Rock":
        print("You win!")
    elif comp == "Scissors":
        print("You loose.")
    else:
        print("It's a draw.")
elif player == "Scissors":
    if comp == "Rock":
        print("You loose.")
    elif comp == "Paper":
        print("You win!")
    else:
        print("It's a draw.")