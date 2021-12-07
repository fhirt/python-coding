import random


def roll():
    return random.randint(1, 6)


counts = [-1, 0, 0, 0, 0, 0, 0]

for r in range(0, 10000):
    dice_value = roll()
    counts[dice_value] += 1

print(f"dice_value\t#rolls")
print(f"one\t\t{counts[1]}")
print(f"two\t\t{counts[2]}")
print(f"three\t\t{counts[3]}")
print(f"four\t\t{counts[4]}")
print(f"five\t\t{counts[5]}")
print(f"six\t\t{counts[6]}")
