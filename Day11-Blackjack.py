############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

from Day11_1_art import logo
import random
from replit import clear
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def start_blackjack(phand, chand):
    """input both player's hand list to check for blackjacks."""
    if list_total(chand) == 21:
        declare_final(phand, chand)
        print("Lose, opponent has Blackjack 😱")
        blackjack()
    elif list_total(phand) == 21:
        declare_final(phand, chand)
        print("Win with a Blackjack 😎")
        blackjack()


def check_ace(hand):
    """input hand after getting card, to check and neutralise aces. Returns hand"""
    if list_total(hand) > 21:
        for pos in range(0,len(hand)):
            if hand[pos] == 11:
                hand[pos] = 1
                return hand
    return hand


def list_total(hand):
    """sums list of any length and returns total"""
    # total = 0
    # for card in hand:
    #     total += card
    # return total
    return sum(hand)


def draw_card (hand):
    """input hand. Adds, checks, and return hand list"""
    hand.append(random.choice(cards))
    return check_ace(hand)


def declare_winner(phand,chand):
    """input both hands, decides winner and restarts"""
    if list_total(phand) == list_total(chand):
        print("Draw 🙃")
        blackjack()
    elif list_total(phand) < list_total(chand):
        print("You lose 😤")
        blackjack()
    elif list_total(phand) > list_total(chand):
        print("You win 😃")
        blackjack()


def declare_cards(phand, chand):
    print(f'Your cards: {phand}, current score: {list_total(phand)}')
    print(f'Computer\'s first card: {chand[0]}')


def declare_final(phand, chand):
    print(f'Your final hand: {phand}, final score: {list_total(phand)}')
    print(f'Computer\'s final hand: {chand}, final score: {list_total(chand)}')


def is_bust(hand):
    if list_total(hand) > 21:
        return True
    else:
        return False


# --------------END OF FUNCTIONS -------------------------------

def blackjack():
    replay = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if replay == "n":
        return

    clear()
    print(logo)
    hands = {
        "player": [],
        "com": [],
    }

    hands["player"] = draw_card(hands["player"])
    hands["player"] = draw_card(hands["player"])
    hands["com"] = draw_card(hands["com"])
    hands["com"] = draw_card(hands["com"])

    # print hand and 1 com
    declare_cards(hands["player"],hands["com"])
    # checks and declares blackjack
    start_blackjack(hands["player"], hands["com"])

    # loops player's turn
    cant_draw = False
    while not cant_draw and input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
        hands["player"] = draw_card(hands["player"])
        declare_cards(hands["player"], hands["com"])
        cant_draw = is_bust(hands["player"])

    # loops com turn
    while list_total(hands["com"]) < 17:
        hands["com"] = draw_card(hands["com"])

    # checks bust
    if is_bust(hands["player"]):
        declare_final(hands["player"], hands["com"])
        print("You went over. You lose 😭")
        blackjack()
    elif is_bust(hands["com"]):
        declare_final(hands["player"], hands["com"])
        print("Opponent went over. You win 😁")
        blackjack()

    declare_final(hands["player"],hands["com"])
    declare_winner(hands["player"],hands["com"])


blackjack()

# print("Lose, opponent has Blackjack 😱")
#
# print("Win with a Blackjack 😎")
#
# print("You went over. You lose 😭")
#
# print("Opponent went over. You win 😁")
#
# print("Draw 🙃")
#
# print("You lose 😤")
#
# print("You win 😃")









#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

