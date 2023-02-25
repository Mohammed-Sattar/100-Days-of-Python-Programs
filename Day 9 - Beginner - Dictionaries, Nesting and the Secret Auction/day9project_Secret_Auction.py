# Day 9 Project - Secret Auction
import art
import os

clear = lambda: os.system('cls') #on Windows System

print(art.logo)
print("Welcome to the secret auction program.")

bidders = {}
another_bidder = "yes"
while (another_bidder.lower() == "yes"):
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bidders[name] = bid

    another_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    clear()

highest_bid = 0
highest_bidder = ""     # stores the name of the highest bidder
for x in bidders:           # x iterates through all the names stored as a key value in the bidders dictionary
    if bidders[x] > highest_bid:
        highest_bid = bidders[x]
        highest_bidder = x

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
# print(bidders)