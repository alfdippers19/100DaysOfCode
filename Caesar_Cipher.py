alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def encode():
    print("Type your message:")
    message = input()
    print("Type the shift number:")
    shift = int(input())
    new_message = ""
    for letter in message:
        current_pos = alphabet.index(letter)
        new_pos = current_pos + shift
        if new_pos > 25:
            new_pos-=26
            if new_pos < 0:
                abs(new_pos)
        new_letter = alphabet[new_pos]
        new_message+=new_letter
    print(f"Here's the encoded result: {new_message}")

def decode():
    print("Type your message:")
    message = input()
    print("Type the shift number:")
    shift = int(input())
    new_message = ""
    for letter in message:
        current_pos = alphabet.index(letter)
        new_pos = current_pos - shift
        new_letter = alphabet[new_pos]
        new_message+=new_letter
    print(f"Here's the decoded result: {new_message}")

complete = False
while complete != True:
    message = ""
    print("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    choice = input()
    if choice == 'encode':
        encode()
    elif choice == 'decode':
        decode()
    else:
        print("Invalid input!")
    print("Type 'yes' if you want to go again. Otherwise type 'no'.")
    choice = input()
    if choice == 'no':
        complete = True