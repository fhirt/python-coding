from .expression import Money


class Bank:

    @staticmethod
    def reduce(expression, currency) -> Money:
        return expression.reduce(currency)
        