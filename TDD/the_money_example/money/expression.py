from __future__ import annotations

class Expression:
    def reduce(self, bank: Bank, to: str) -> Money:
        raise SystemExit("needs implementation")

    def plus(self, addend: Expression) -> Expression:
        raise SystemExit("needs implementation")

    def times(self, multiplier) -> Expression:
        raise SystemExit("needs implementation")

class Sum(Expression):
    def __init__(self, augend: Expression, addend: Expression) -> None:
        self.augend = augend
        self.addend = addend

    def reduce(self, bank: Bank, to: str) -> Money:
        return Money(self.augend.reduce(bank, to).amount + self.addend.reduce(bank, to).amount, to)

    def plus(self, addend: Expression):
        return Sum(self, addend)

    def times(self, multiplier) -> Expression:
        return Sum(self.augend.times(multiplier), self.addend.times(multiplier))


class Money(Expression):
    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")

    def __init__(self, amount, currency):
        self.__currency = currency
        self.amount = amount

    def reduce(self, bank: Bank, to: str) -> Money:
        rate = bank.rate(self.currency(), to)
        return Money(self.amount / rate, to)

    def currency(self) -> str:
        return self.__currency

    def times(self, multiplier) -> Expression:
        return Money(self.amount * multiplier, self.currency())

    def plus(self, addend: Expression) -> Expression:
        return Sum(self, addend)

    def __eq__(self, other: object) -> bool:
        return self.amount == other.amount and self.currency() == other.currency()

    def __str__(self) -> str:
        return f"{self.amount} {self.currency}"

class Bank:
    def __init__(self) -> None:
        self.__exchange_rates = {}

    def reduce(self, expression, currency) -> Money:
        return expression.reduce(self, currency)
    
    def add_rate(self, curr: str, to: str, rate):
        self.__exchange_rates.update({curr+to: rate})

    def rate(self, curr: str, to: str):
        if curr == to:
            return 1
        else:
            return self.__exchange_rates[curr+to]