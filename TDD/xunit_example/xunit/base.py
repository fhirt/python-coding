class TestCase:
    def __init__(self, name) -> None:
        self.name = name

    def run(self):
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name) -> None:
        self.was_run = False
        super().__init__(name)

    def test_method(self):
        self.was_run = True
