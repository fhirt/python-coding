class TestCase:
    def __init__(self, name) -> None:
        self.name = name

    def setup(self):
        """
        optional setup before each test method
        """       

    def run(self) -> "TestResult":
        test_result = TestResult()
        test_result.test_started()
        self.setup()
        method = getattr(self, self.name)
        method()
        self.tear_down()
        return test_result

    def tear_down(self):
        """
        optional tear down after each test method
        """

class TestResult:
    def __init__(self) -> None:
        self.run_count = 0

    def test_started(self):
        self.run_count += 1

    def summary(self) -> str:
        return f"{self.run_count} run, 0 failed"

class WasRun(TestCase):
    def __init__(self, name) -> None:
        super().__init__(name)

    def setup(self):
        self.log = "setup "

    def test_method(self):
        self.log = self.log + "test_method "

    def tear_down(self):
        self.log = self.log + "tear_down"

    def broken_method(self):
        raise Exception