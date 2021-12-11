from xunit import WasRun, TestCase

class TestCaseTest(TestCase):    
    def test_template_method(self):
        test = WasRun("test_method")
        test.run()
        assert(test.log == "setup test_method tear_down")

TestCaseTest("test_template_method").run()
