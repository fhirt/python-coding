class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier) :
        return Dollar(self.amount * multiplier)

    def __eq__(self, other: object) -> bool:
        if(isinstance(other, Dollar)):
            return self.amount == other.amount
        return False