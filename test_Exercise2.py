import unittest
from Exercise2 import Restaurant
rs = Restaurant("taste of rome", "italian")
class TestCases(unittest.TestCase):
    def test_set_number_served_values(self):
        self.assertRaises(ValueError, rs.set_number_served, -2)
        
    def test_set_number_served_types(self):
        self.assertRaises(TypeError, rs.set_number_served, "i")
        self.assertRaises(TypeError, rs.set_number_served, True)

    def test_increment_number_served_values(self):
        self.assertRaises(ValueError, rs.increment_number_served, -2)
    
    def test_set_number_served_types(self):
        self.assertRaises(TypeError, rs.increment_number_served, "i")
        self.assertRaises(TypeError, rs.increment_number_served, True)


if __name__ == '__main__':
    unittest.main()