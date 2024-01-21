winner = ['nobody', 0]
auction = True
bids = {}

print(f"\nWelcome to the secret auction program.\n")

while auction:
    bidder_name = input("What is your name?: ")
    bid = float(input("What's your bid?: $"))
    next_round = input("Are there any other bidders? (Yes/No): ").upper()

    bids[bidder_name] = bid

    auction = True if next_round[0] == 'Y' else False


def set_winner(name, value):
    winner[0], winner[1] = name, value


for k, v in bids.items():
    if v > winner[1]:
        set_winner(k, v)

print(f'\nThe winner is {winner[0]} with a bid of ${"{0:,.2f}".format(winner[1])} dollars.')
