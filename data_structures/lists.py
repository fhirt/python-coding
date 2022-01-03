colors = ["red", "yellow", "green", "blue"]
print(type(colors))
print(colors)

numbers = (1,2,3)
print(numbers)
numbers_list = list(numbers)
print(numbers_list)
print(list("Fabio"))


groceries = "eggs, milk, cheese"
grocery_list = groceries.split(", ")
print(grocery_list) 


numbers = list(range(1,10))
print(numbers)
print(numbers[1])
print(numbers[1:3])

colors[0] = "burgundy"
print(colors)

colors[1:3] = ["orange", "magenta"]
print(colors)

colors = ["red", "yellow", "green", "blue"]
colors[1:3] = ["orange", "magenta", "aqua"]
print(colors)

colors[1:4] = ["yellow", "green"]
print(colors)

colors.insert(1, "orange")
print(colors)

colors.insert(10, "violet")
print(colors)

colors.insert(-1, "indigo")
print(colors)

color = colors.pop(3)
print(color)
print(colors)

print(colors.pop(-1))
print(colors)
print(colors.pop())
print(colors)
colors.append("indigo")
print(colors)

colors.extend(["violet", "ultraviolet"])
print(colors)

nums = list(range(1,6))
total = 0
for number in nums:
    total += number
    
print(total)

print(sum(nums))
print(min(nums))
print(max(nums))


numbers = tuple(range(1,6))
print(numbers)

squares = [num**2 for num in numbers]
print(squares)

str_numbers = ["1.5", "2.3", "5.25"]
float_numbers = [float(value) for value in str_numbers]
print(float_numbers)

food = ["rice", "beans"]
print(food)
food.append("broccoli")
print(food)
food.extend(["bread", "pizza"])
print(food)
print(food[:2])
print(food[len(food)-1])


breakfast = "eggs, fruit, orange juice".split(", ")
print(breakfast)
print(len(breakfast) == 3)

lengths = [len(fast) for fast in breakfast]
print(lengths)
