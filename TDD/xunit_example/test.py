from xunit import WasRun, TestCase

class TestCaseTest(TestCase):    
    def setup(self):
        self.test = WasRun("test_method")

    def test_template_method(self):
        self.test.run()
        assert(self.test.log == "setup test_method tear_down")

    def test_result(self):
        result = self.test.run()
        assert(result.summary() == "1 run, 0 failed")

    def test_failed_result(self):
        broken_test = WasRun("broken_method")
        result = broken_test.run()
        assert(result.summary() == "1 run, 1 failed")

TestCaseTest("test_template_method").run()
TestCaseTest("test_result").run()
TestCaseTest("test_failed_result").run()
