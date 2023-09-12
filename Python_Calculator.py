operations = {"+":"Add","-":"subtract","*":"multiply","/":"divide"}
def add(num1,num2):
    return num1 + num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1 * num2
def div(num1,num2):
    return num1/num2
def calculator():
    num3 = 0
    num1 = float(input("What is your first number?: "))
    should_continue = True
    while should_continue != False:
        num2 = float(input("What is your second number?: "))
        for symbol in operations:
            print(symbol)
        choice = ""
        for key in operations:
            if key == '/':
                choice = input(f"{operations[key]}. Type a symbol: ")
            else:
                print(f"{operations[key]}, or",end = " ")
        if choice == "+":
            num3 = add(num1,num2)
        elif choice == "-":
            num3 = sub(num1,num2)
        elif choice == "*":
            num3 = mul(num1,num2)
        elif choice == "/":
            num3 = div(num1,num2)
        print(f"Your result is {num3}")
        choice = input("Would you like to keep calculating? 'y' or 'n': ")
        if choice == 'n':
            should_continue = False
            calculator()
        else:
            num1 = num3
calculator()
