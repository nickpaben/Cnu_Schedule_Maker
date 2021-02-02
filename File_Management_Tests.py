import unittest
from File_Management import *

# get_crns
# get_data - will not test because we will be removing this soon.
# get_class_data_from_crn - test isn't that great.
# get_final_time - not sure if this method will be used, so I'm holding off on creating tests for now.


class File_Management_Tests(unittest.TestCase):
    def test_crn_is_valid_1(self):
        self.assertEqual(True, crn_is_valid(8649))

    def test_crn_is_valid_2(self):
        self.assertEqual(False, crn_is_valid(5000))

    def test_get_class_data_from_crn(self):
        test_data = get_class_data_from_crn(9114)
        self.assertEqual(test_data[0], "SOCL 306")
        self.assertEqual(test_data[1], "ON1")
        self.assertEqual(test_data[2], "Social Psychology")

    def test_get_name_valid(self):
        self.assertEqual("CPSC 420", get_name(8054))

    def test_get_name_invalid(self):
        self.assertEqual("Not Found", get_name(5000))


if __name__ == '__main__':
    unittest.main()
