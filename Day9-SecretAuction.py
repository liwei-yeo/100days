from replit import clear
from Day9_1_art import logo
#HINT: You can call clear() to clear the output in the console.

print(f"{logo}\nWelcome to the secret auction program.")
p_status = True
auction_list = {}

while p_status:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    auction_list[name] = bid

    p_check = input("Are there any other bidder? Type 'yes' or 'no.\n").lower()
    if p_check == "yes":
        clear()

    elif p_check == "no":
        p_status = False
        # compare function
        pname = ""
        pprice = 0
        for name in auction_list:
            if auction_list[name] > pprice:
                pname = name
                pprice = auction_list[name]
        print(f"The winner is {pname} with a bid of ${pprice}.")
