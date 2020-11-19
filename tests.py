import unittest
from string_helpers import String_helper

class StringHelpersTest(unittest.TestCase):

    def test_array_to_string(self):
        sh = String_helper()
        ia = [7,1,0,1,4]
        r = sh.integer_array_to_string(ia)
        print(r)
        self.assertEqual(r, '71014')

    def test_string_to_array(self):
        sh = String_helper()
        s = 'Fortuna'
        r = sh.string_to_array(s)
        print(r)
        self.assertEqual(r,['F','o','r','t','u','n','a'])
               
if __name__ == "__main__":
    unittest.main()

