from Day14_1_art import logo, vs
from Day14_1_game_data import data
import random
from replit import clear


def rand_pick(foll=0):
    """returns new random entry. Accepts 'foll' argument, and checks to return entry with different follower count """
    roll = True
    while roll:
        curr_dict = random.choice(data)
        if foll != curr_dict["follower_count"]:
            return curr_dict


print(logo)
a_select = rand_pick()
a_foll = a_select['follower_count']
score = 0
winning = True

while winning:
    b_select = rand_pick()
    b_foll = b_select['follower_count']

    print(f"Compare A: {a_select['name']}, a {a_select['description']}, from {a_select['country']}.")
    print(vs)
    print(f"Compare B: {b_select['name']}, a {b_select['description']}, from {b_select['country']}.")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    sel_dict = {}
    sel = 0
    other = 0
    if choice == "a":
        sel_dict = a_select
        sel = a_foll
        other = b_foll
    elif choice == "b":
        sel_dict = b_select
        sel = b_foll
        other = a_foll
    else:
        print("No selection detected")
        winning = False

    if sel > other:
        a_select = sel_dict
        a_foll = a_select['follower_count']
        score += 1
        clear()
        print(logo)
        print(f"You're right! Current score: {score}.")

    elif other > sel:
        clear()
        print(f"Sorry, that's wrong. Final score: {score}")
        winning = False
