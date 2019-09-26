import unittest
import foo

# class TestStringMethods(unittest.TestCase):
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')
# 
#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())
# 
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)

#https://www.qa-knowhow.com/?p=1927
class TestFoo(unittest.TestCase):
    def setUp(self):
        print('In setUp()')


    def tearDown(self):
        print('In tearDown()')
        
    def test_add_two_int(self):
        print('in test_add_two_int()')
        result = foo.add_int(1,2)
        #print(result)
        self.assertEqual(result, 3)

    def test_add2_two_int(self):
        print('in test_add2_two_int()')
        result = foo.add_int(3,2)
        #print(result)
        self.assertEqual(result, 5)

class TestMathFunc(unittest.TestCase):
    def test_add(self):
        """Test method add(a, b)"""
        self.assertEqual(3, foo.add(1, 2))
        self.assertNotEqual(3, foo.add(2, 2))

    def test_minus(self):
        """Test method minus(a, b)"""
        self.assertEqual(1, foo.minus(3, 2))

    def test_multi(self):
        """Test method multi(a, b)"""
        self.assertEqual(6, foo.multi(2, 3))

    def test_divide(self):
        """Test method divide(a, b)"""
        self.assertEqual(2, foo.divide(6, 3))
        self.assertEqual(2.5, foo.divide(5, 2))


if __name__ == '__main__':
    unittest.main(verbosity=2)