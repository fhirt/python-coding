import random

def coin_flip():
    """Randomly return 'heads' or 'tails'."""
    if random.randint(0,1) == 0:
        return "heads"
    else:
        return "tails"

heads_count = 0
tails_count = 0

for flip in range(10_000):
    if coin_flip() == "heads":
        heads_count += 1
    else:
        tails_count += 1

print(f"heads: {heads_count}\ntails: {tails_count}")