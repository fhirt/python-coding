import random

capitals = {
    "California": "Sacramento",
    "New York": "Albany",
    "Texas": "Austin",
}
print(capitals)

key_value_pairs = (
    ("California", "Sacramento"),
    ("New York", "Albany"),
    ("Texas", "Austin"),
)
print(key_value_pairs)

capitals = dict(key_value_pairs)
print(capitals)

print(capitals["Texas"])

capitals["Colorado"] = "Denver"
print(capitals)

capitals["Texas"] = "Houston"
print(capitals)

del capitals["Texas"]
print(capitals)

print("Arizona" in capitals)
print("California" in capitals)

for key in capitals:
    print(f"{key} - {capitals[key]}")

for state, capital in capitals.items():
    print(f"The capital of {state} is {capital}")

capitals[50] = "Honolulu"
print(capitals)

states = {
    "California": {
        "capital": "Sacramento",
        "flower": "California Poppy"
    },
    "New York": {
        "capital": "Albany",
        "flower": "Rose"
    },
    "Texas": {
        "capital": "Austin",
        "flower": "Bluebonnet"
    },
}

print(states["Texas"])
print(states["Texas"]["flower"])

captains = dict()
captains["Enterprise"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"

print(captains)


def check_captain(ship, caps):
    if ship not in caps:
        caps[ship] = "unknown"


check_captain("Enterprise", captains)
check_captain("Discovery", captains)

for ship, captain in captains.items():
    print(f"The {ship} is captained by {captain}.")

del captains["Discovery"]
print(captains)


capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
}

random_state = random.choice(list(capitals_dict.keys()))
correct_capital = capitals_dict[random_state].lower()

still_guessing = True

while still_guessing:
    answer = input(f"What is the capital of {random_state}? (or exit to quit the quizz)").lower()
    if answer == correct_capital:
        print("Correct")
        still_guessing = False
    elif answer == "exit":
        print(correct_capital)
        print("Goodbye")
        still_guessing = False
    else:
        print("try again")
    
    
