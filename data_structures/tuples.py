my_tuple= (1,2,3)
print(type(my_tuple))
empty_tuple = ()

print(type((1)))

x = (1,)
print(type(x))

print(tuple("Python"))

numbers = (1,2,3)
print(len(numbers))

coordinates = 3, 8
print(type(coordinates))
print(coordinates)

x, y = coordinates

print(x)
print(y)

name, age, occupation = "David", 34, "programmer"

print(name, age, occupation)


cardinal_numbers = "first", "second", "third"
print(cardinal_numbers[1])

position1, position2, position3 = cardinal_numbers

print(position1)
print(position2)
print(position3)

my_name = tuple("Fabio")

print(my_name)
print("x" in my_name)
print(my_name[1:])

