import random
dict = {0:["Ronaldo","Footballer","Portugal",604],
        1:["Messi","Footballer","Argentena",486],
        2:["Selena Gomez","Singer","America",429]}
game_over = False
the_same = False
score = 0
while game_over == False:
    if score>0:
        print(f"Your current score is: {score}")
    temp1 = random.randint(0,len(dict)-1)
    print(f"Compare A: {dict[temp1][0]} a {dict[temp1][1]} from {dict[temp1][2]}")
    temp2 = random.randint(0,len(dict)-1)
    if temp1 == temp2:
        the_same = True
    while the_same == True:
        temp2 = random.randint(0,len(dict)-1)
        if temp1 != temp2:
            the_same = False
    print(f"Againsed B: {dict[temp2][0]} a {dict[temp2][1]} from {dict[temp2][2]}")
    choice = input("Who has more followers? Type 'A' or 'B': ")
    if choice == 'A':
        if dict[temp1][3]>dict[temp2][3]:
            print("That's right!")
            score+=1
        else:
            print(f"That's wrong. Final score: {score}")
            game_over = True
    else: 
        if dict[temp2][3]>dict[temp1][3]:
            print("That's right!")
            score+=1
        else:
            print(f"That's wrong. Final score: {score}")
            game_over = True