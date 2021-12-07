import random


def coin_toss():
    return random.choice(['h', 't'])

def count_flips():
    first_toss = coin_toss()
    flips = 1

    while True:
        flips += 1
        if first_toss != coin_toss():
            return flips

NUM_TRIES = 10_000

total_flips = 0

for trial in range(0, NUM_TRIES):
    total_flips += count_flips()

avg_flips = total_flips / NUM_TRIES

print(f"Average number of flips needed to change sides: {avg_flips}")
