import random
number = random.randint(0,101)
choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
if choice == 'easy':
    lives = 10
else:
    lives = 5
while lives>0:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it! The answer was {number}")
        break
    elif guess > number:
        print("Too high.")
        lives-=1
    elif guess < number:
        print("Too low.")
        lives-=1
if lives == 0:
    print("You've run out of guesses, you loose.")