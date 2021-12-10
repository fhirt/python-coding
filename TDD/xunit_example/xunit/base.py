class TestCase:
    def __init__(self, name) -> None:
        self.name = name

    def setup(self):
        pass        

    def run(self):
        self.setup()
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name) -> None:
        self.was_run = False
        super().__init__(name)

    def setup(self):
        self.was_run = False
        self.was_setup = True

    def test_method(self):
        self.was_run = True
