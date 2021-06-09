import unittest
import functions


class TestAdd(unittest.TestCase):
        def test_equal(self):  # test method names begin with 'test'
            self.assertEqual((2+2),4)
        

        def test_false(self):
            self.assertNotEqual((2+2),8)
            
        def test_type(self):
            self.assertEqual(type,type)

if __name__ == '__main__':
        unittest.main() 
