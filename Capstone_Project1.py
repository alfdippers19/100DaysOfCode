import random

deck = [1,2,3,4,5,6,7,8,9,10,10,10,10] * 4
player_hand = []
dealer_hand = []
player_total = 0
dealer_total = 0

game_finish = False

def deck_shuffler():
    for x in range(0,len(deck)):
        rnd = random.randint(0,len(deck))
        temp = deck[x]
        deck[x] = deck[rnd-1]
        deck[rnd-1] = temp

def player_deal():
    card = random.randint(0,len(deck))
    player_hand.append(deck[card-1])
    for x in range(0,len(deck)):
        if deck[x] == card:
            deck.remove(card)
            break

def dealer_deal():
    card = random.randint(0,len(deck))
    dealer_hand.append(deck[card-1])
    for x in range(0,len(deck)):
        if deck[x] == card:
            deck.remove(card)
            break

def compare_hands():
    if player_total == dealer_total:
        print(f"The dealers hand was: {dealer_hand}")
        print("Draw")
    elif player_total>dealer_total:
        print(f"The dealers hand was: {dealer_hand}")
        print("You win!")
    elif player_total<dealer_total:
        print(f"The dealers hand was: {dealer_hand}")
        print("Dealer wins!")

while game_finish != True:
    deck = [1,2,3,4,5,6,7,8,9,10,10,10,10] * 4
    hit_or_stand = ""
    deal = False
    player_hand = []
    dealer_hand = []
    deck_shuffler()
    print("Deck has been shuffled")
    while deal != True:
        choice = input("Deal? 'y' or 'n': ")
        if choice == "y":
            deal = True
    for x in range(0,2):
        player_deal()
    for x in range(0,2):
        dealer_deal()
    while hit_or_stand != "s":
        player_total = 0
        dealer_total = 0
        for x in range(0,len(player_hand)):
            player_total+=player_hand[x]
        for x in range(0,len(dealer_hand)):
            dealer_total+=dealer_hand[x]
        for x in range(0,len(player_hand)):
            if player_hand[x] == 1:
                print(f"Your hand is: {str(player_hand)}")
                print("You have an ace")
                choice = input("Use it as a 1 or an 11?: ")
                if choice == "1":
                    player_hand[x] = 1
                else:
                    player_hand[x] = 11
        for x in range(0,len(dealer_hand)):
            if dealer_hand[x] == 1:
                choice = random.randint(0,2)
                if choice == 1:
                    dealer_hand[x] = 1
                else:
                    dealer_hand[x] = 11
        print(f"Your hand is: {str(player_hand)}")
        if len(dealer_hand) == 2:
            print(f"Dealer's hand is: [?, {str(dealer_hand[1])}]")
        else:
            print(f"Dealer's hand is: [?, {str(dealer_hand[1])}, {str(dealer_hand[2])}]")
        if player_total>21:
            print("Player is bust")
            print("Dealer wins!")
            break
        elif dealer_total>21:
            print("Dealer is bust")
            print("You win!")
            break
        if dealer_total<17:
            dealer_deal()

        hit_or_stand = input("Hit or Stand? 'h' or 's': ")
        if hit_or_stand == 'h':
            player_deal()
    compare_hands()
    choice = input("Play again? 'y' or 'n': ")
    if choice == "n":
        game_finish = True