class TestCase:
    def __init__(self, name) -> None:
        self.name = name

    def setup(self):
        """
        optional setup before each test method
        """       

    def run(self):
        self.setup()
        method = getattr(self, self.name)
        method()
        self.tear_down()

    def tear_down(self):
        """
        optional tear down after each test method
        """

class WasRun(TestCase):
    def __init__(self, name) -> None:
        super().__init__(name)

    def setup(self):
        self.log = "setup "

    def test_method(self):
        self.log = self.log + "test_method "

    def tear_down(self):
        self.log = self.log + "tear_down"