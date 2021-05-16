import random

hands = {
    "player" : [],
    "com" : [],
}

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def start_blackjack(phand, chand):
    """input both player's hand list to check for blackjacks. Returns False if no Backjack"""
    if list_total(phand) == 22 or list_total(phand) == 21:
        print("Win with a Blackjack 😎")
        # RESTART ALGO
    elif list_total(chand) == 22 or list_total(chand) == 21:
        print("Lose, opponent has Blackjack 😱")
        # RESTART AlGO
    else:
        return False


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
    total = 0
    for card in hand:
        total += card
    return total


def draw_card (hand):
    """input hand. Adds, checks, and return hand list"""
    hand.append(random.choice(cards))
    return check_ace(hand)


hands["player"] = draw_card(hands["player"])
hands["player"] = draw_card(hands["player"])
hands["com"] = draw_card(hands["com"])
hands["com"] = draw_card(hands["com"])


print(f'Your cards: {hands["player"]}, current score: {list_total(hands["player"])}')
print(f'Computer\'s first card: {hands["com"][0]}')


start_blackjack(hands["player"],hands["com"])