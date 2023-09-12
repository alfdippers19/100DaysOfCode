import random

word_list = ["building","computer","road"]
game_over = False
lives = 7

word_index = random.randint(0,len(word_list)-1)
word = word_list[word_index]

display_word = ["_"] * len(word)

while game_over != True:
    temp_str = ""
    if  word == temp_str.join(display_word):
        print("\nConcratulations you got the word!")
        game_over = True
    elif lives == 0:
        print("\nYou are out of lives!")
        game_over = True
    else:
        temp_char = ""
        temp_list = []
        for x in range(0,len(display_word)):
            temp_list.append(display_word[x])
        for x in range(0, len(display_word)):
            print(display_word[x],end = " ")
        guess = input("\n\nPlease guess a letter: ")
        for x in range(0, len(word)):
            if  guess == word[x]:
                temp_char = word[x]
                display_word[x] = temp_char
        if display_word != temp_list:
            print("\nYou got a letter!")
        else:
            print("\nYou guessed incorrectly!")
            lives-=1