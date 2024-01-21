import random


# Define functions

def deal(hand, n):
    """Deals an n amount of cards to the specified hand."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    for card in range(n): hand.append(random.choice(cards))


def check(hand):
    """Checks if the specified hand is greater than 21. Turns 11s into 1s if that's the case."""
    if sum(hand) > 21:
        for i in range(len(hand)):
            hand[i] = 1 if \
                hand[i] == 11 else \
                hand[i]

    return sum(hand) > 21


def play():
    """Executes the Blackjack Game"""

    # Deal cards

    player_hand, cpu_hand = [], []

    deal(player_hand, 2)

    deal(cpu_hand, 2)

    # Check if either played busted (e.g. 11,11)
    busted = check(player_hand)

    check(cpu_hand)

    # Print hands

    print(f"\nYour cards: {player_hand}")

    print(f"\nComputer's first card: {cpu_hand[0]}")

    # Check if player wants another card

    while not busted:

        more = input("\nDo you want another card? Y/N: ")

        if more.upper() == "Y":

            deal(player_hand, 1)

            busted = check(player_hand)

            print(f"\nYour cards: {player_hand}")

        else:
            break

    if busted:
        print(f"\nBusted! Your total is {sum(player_hand)}, you lose.")
        return

    # Print final hands

    print(f"\nYour final hand: {player_hand}")
    print(f"\nComputer's final hand: {cpu_hand}")

    # Evaluate hand totals to determine the result

    result = "You win!" if sum(player_hand) > sum(cpu_hand) else \
        "You lost!" if sum(player_hand) < sum(cpu_hand) else "It's a tie"

    print(f"\n{result}")


# Play as long as the player says "Y"

while input("\nDo you want to play a game of Blackjack? Y/N: ").upper()[0] == "Y":
    play()

# End

print("\nGoodbye!")
