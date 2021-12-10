from xunit import WasRun, TestCase

class TestCaseTest(TestCase):
    def setup(self):
        self.test = WasRun("test_method")

    def test_running(self):
        self.test.run()
        assert(self.test.was_run)

    def test_setup(self):
        self.test.run()
        assert(self.test.was_setup)

TestCaseTest("test_running").run()
TestCaseTest("test_setup").run()
