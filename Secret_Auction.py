complete = False
auction = {}
while complete != True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    auction[name] = bid
    choice = input("Are there any other bidders? 'yes' or 'no': ")
    if choice == 'no':
        complete = True
highest_bidder = ""
highest_bid = -1
for key in auction:
    if auction[key] > highest_bid:
        highest_bidder = key
        highest_bid = auction[key]
print(f"The winner is {highest_bidder}, with a bid of ${highest_bid}")