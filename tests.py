import unittest
from string_helpers import String_helper

class StringHelpersTest(unittest.TestCase):

    def test_array_to_string(self):
        sh = String_helper()
        r = sh.array_to_string()
        a = self.assertEquals(r, True)
        print(self.assertEqual(r,True))
               
if __name__ == "__main__":
    unittest.main()

