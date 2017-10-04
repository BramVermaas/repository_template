from unittest import TestCase
import repository_template

class TestCore(TestCase):
    def test_is_string(self):
        s = repository_template.my_function()
        self.assertTrue(isinstance(s, basestring))