import copy
import random

two_by_two = [[1, 2], [3, 4]]
print(len(two_by_two))

print(two_by_two[0])
print(two_by_two[1])

print(two_by_two[1][0])


for sub_list in two_by_two:
    for element in sub_list:
        print(element)

animals = ["lion", "tiger", "frumious Bandersnatch"]
large_cats = animals[:]
large_cats.append("Tigger")
print(animals)
print(large_cats)

matrix1 = [[1, 2], [3, 4]]
matrix2 = matrix1[:]
matrix2[0] = [5, 6]
print(matrix2)
print(matrix1)

matrix2[1][0] = 1
print(matrix2)
print(matrix1)

matrix3 = copy.deepcopy(matrix1)
matrix3[1][0] = 3
print(matrix3)
print(matrix1)

colors = ["red", "yellow", "green", "blue"]
colors.sort()
print(colors)

numbers = [1, 10, 5, 3]
numbers.sort()
print(numbers)

colors.sort(key=len)
print(colors)


def get_second_element(item):
    return item[1]


items = [(4, 1), (1, 2), (-9, 0)]
items.sort(key=get_second_element)
print(items)

data = ((1, 2), (3, 4))
for idx, row in enumerate(data):
    print(f"Row {idx+1} sum: {sum(row)}")

numbers = list(range(1, 5))
numbers.reverse()
print(numbers)
num2 = numbers[:]
numbers.sort()
print(num2)
print(numbers)


universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


def enrollment_stats(unis):
    students = [uni[1] for uni in unis]
    fees = [uni[2] for uni in unis]
    return students, fees


def median(lst):
    lst.sort()
    return lst[int(len(lst)/2)]


def mean(lst):
    return sum(lst) / len(lst)


students, fees = enrollment_stats(universities)

print(f"total students={sum(students)}, fees={sum(fees)}")
print(f"mean students={mean(students)}, fees={mean(fees)}")
print(f"median students={median(students)}, fees={median(fees)}")


def generate_poem():
    possible_nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango",
                      "extrovert", "gorilla"]
    possible_verbs = ["kicks", "jingles", "bounces", "slurps", "meows",
                      "explodes", "curdles"]
    possible_adjectives = ["furry", "balding", "incredulous", "fragrant",
                           "exuberant", "glistening"]
    possible_prepositions = ["against", "after", "into", "beneath", "upon",
                             "for", "in", "like", "over", "within"]
    possible_adverbs = ["curiously", "extravagantly", "tantalizingly",
                        "furiously", "sensuously"]

    nouns = random.sample(possible_nouns, 3)
    verbs = random.sample(possible_verbs,3)
    adjectives = random.sample(possible_adjectives, 3)
    prepositions = random.sample(possible_prepositions,2)
    adverb = random.sample(possible_adverbs,1)

    return f"""
{'*' * 50}
A {adjectives[0]} {nouns[0]}

A {adjectives[0]} {nouns[0]} {verbs[0]} {prepositions[0]} the {adjectives[1]} {nouns[1]}
{adverb[0]}, the {nouns[0]} {verbs[1]}
the {nouns[1]} {verbs[2]} {prepositions[1]} a {adjectives[2]} {nouns[2]}
{'*' * 50}
"""


def choose(num, choices):
    chosen = []
    for i in range(num):
        chosen.append(random.sample(choices, num))
    return chosen


print(generate_poem())
