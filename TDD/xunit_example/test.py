from xunit import WasRun, TestCase

class TestCaseTest(TestCase):
    def test_running(self):
        test = WasRun("test_method")
        assert(not test.was_run)
        test.run()
        assert(test.was_run)

TestCaseTest("test_running").run()
