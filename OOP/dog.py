class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed="poodle", coat_color="black") -> None:
        self.name = name
        self.age = age
        self.coat_color = coat_color
        self.breed = breed

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


a = Dog("fido", 10)
b = Dog("bobo", 7)
print(a)
print(b)
print(a.speak("wöff"))

philo = Dog("Philo", 5, "brown")
print(f"{philo.name}'s coat is {philo.coat_color}.")


class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)


class Dachshund(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)


class Bulldog(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)


miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

print(type(miles))
print(miles.speak())


class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)


mimi = GoldenRetriever("Mimi", 5)
print(mimi.speak())


class Rectangle:
    def __init__(self, length, width) -> None:
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)


rect = Rectangle(2, 3)
print(rect.area())
square = Square(5)
print(square.area())



