#making a blind auction software 
import os

keepGoing = True
bidders = []
winner = 0

import os
import sys

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        sys.stdout.write("\033[2J\033[H")
        sys.stdout.flush()

# Usage:


def addBidders(name,bid):
    temp = {}
    temp["Name"] = name
    temp["Bid"] = bid
    bidders.append(temp)

print("Welcome to the secret auction program")


while keepGoing:
    
    userName = input("What's your name:\n")
    userBid = int(input("What's your bid?:\n"))
    question = input("Are there any other bidders? Type 'yes' or 'no'\n")
    addBidders(userName,userBid)
    if question == "yes":
        clear_console()
        keepGoing = True
    else:
        for bidder in bidders:
            if bidder["Bid"] > winner:
                winner = bidder["Bid"]
                winnerName = bidder["Name"]
        print(f"The winner is: {winnerName}")
        keepGoing = False

