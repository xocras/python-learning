auction = True
bids = {}

print(f"\nWelcome to the secret auction program.\n")

while auction:
    bidder_name = input("What is your name?: ")
    bid = float(input("What's your bid?: $"))
    next_round = input("Are there any other bidders? (Yes/No): ").upper()

    bids[bidder_name] = bid

    auction = True if next_round[0] == 'Y' else False

w = ['nobody', 0]


def set_winner(name, value):
    w[0] = name
    w[1] = value


for k, v in bids.items():
    if v > w[1]:
        set_winner(k, v)

print(f'\nThe winner is {w[0]} with a bid of ${"{0:,.2f}".format(w[1])} dollars.')
