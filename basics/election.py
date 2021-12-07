import random


def count_votes():
    return [random.random() < .87, random.random()
             < .65, random.random() < .17]


def determine_winner():
    candidate_a = 0
    for region in count_votes():
        if region:
            candidate_a += 1

    if candidate_a > 1:
        return "A"
    else:
        return "B"


SIMULATIONS = 10_000

winner_a = 0

for simulation in range(0, SIMULATIONS):
    if determine_winner() == "A":
        winner_a += 1

print(f"Candidate A wins with probability of {(winner_a / SIMULATIONS) * 100:.2f}%")
