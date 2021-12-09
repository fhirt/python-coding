from __future__ import annotations
import abc

class Expression(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'reduce') and
        callable(subclass.reduce))


class Sum(Expression):
    def __init__(self, augend, addend) -> None:
        self.augend = augend
        self.addend = addend

    def reduce(self, currency: str) -> Money:
        return Money(self.augend.amount + self.addend.amount, currency)


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

    def currency(self) -> str:
        return self.__currency

    def times(self, multiplier) -> Money:
        return Money(self.amount * multiplier, self.currency())

    def plus(self, addend: Money) -> Expression:
        return Sum(self, addend)

    def __eq__(self, other: object) -> bool:
        return self.amount == other.amount and self.currency() == other.currency()

    def __str__(self) -> str:
        return f"{self.amount} {self.currency}"