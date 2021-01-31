import unittest
from Search_Engine import *


class Search_Engine_Tests(unittest.TestCase):
    def test_get_class_by_crn(self):
        test_course = get_class_by_crn(8914)
        self.assertEqual(test_course.course, "COMM 415")

    def test_get_class_by_crn_invalid(self):
        funny_number = 69
        test_course = get_class_by_crn(funny_number)
        default_course = Course_Section(funny_number)
        self.assertEqual(test_course, default_course)

    def test_get_classes_by_name_chem(self):
        test_courses = ["HONR 150", "HONR 167", "HONR 280", "CHEM 420", "CHEM 420L"]
        courses = get_classes_by_name(test_courses, "CHEM 420")
        self.assertEqual(courses, ["CHEM 420", "CHEM 420L"])

    def test_get_classes_by_name_none_found(self):
        test_courses = ["HONR 150", "HONR 167", "HONR 280", "CHEM 420", "CHEM 420L"]
        courses = get_classes_by_name(test_courses, "THEA")
        self.assertEqual(courses, [])

    def test_get_classes_by_name_honors(self):
        test_courses = ["HONR 150", "HONR 167", "HONR 280", "CHEM 420", "CHEM 420L"]
        courses = get_classes_by_name(test_courses, "HONR")
        self.assertEqual(courses, ["HONR 150", "HONR 167", "HONR 280"])

    def test_get_classes_by_name_honors_100_level(self):
        test_courses = ["HONR 150", "HONR 167", "HONR 280", "CHEM 420", "CHEM 420L"]
        courses = get_classes_by_name(test_courses, "HONR 1")
        self.assertEqual(courses, ["HONR 150", "HONR 167"])

    def test_filter_classes_by_day(self):
        test_courses = [Course_Section(8013), Course_Section(8014), Course_Section(8015)]
        courses = filter_classes_by_day(test_courses, "MW")
        self.assertEqual(courses, [Course_Section(8013), Course_Section(8014)])

    def test_filter_classes_by_llc_any(self):
        test_courses = [Course_Section(8895), Course_Section(8014), Course_Section(8008)]
        courses = filter_classes_by_llc(test_courses)
        print(courses[0])
        self.assertEqual(courses, [Course_Section(8895), Course_Section(8008)])

    def test_filter_classes_by_llc_specific(self):
        test_courses = [Course_Section(8013), Course_Section(8014), Course_Section(8008)]
        courses = filter_classes_by_llc(test_courses, "LLFR")
        self.assertEqual(courses, [Course_Section(8008)])

    def test_filter_classes_by_teacher_include(self):
        test_courses = [Course_Section(8013), Course_Section(8014), Course_Section(8015)]
        courses = filter_classes_by_teacher(test_courses, "Almalag, Mohammad")
        self.assertEqual(courses, [Course_Section(8014), Course_Section(8015)])

    def test_filter_classes_by_teacher_exclude(self):
        test_courses = [Course_Section(8013), Course_Section(8014), Course_Section(8015)]
        courses = filter_classes_by_teacher(test_courses, "Almalag, Mohammad")
        self.assertEqual(courses, [Course_Section(8013)])

    def test_filter_classes_by_time(self):
        test_courses = [Course_Section(8913), Course_Section(8914), Course_Section(8915)]
        courses = filter_classes_by_time(test_courses, 1300, 1515)
        self.assertEqual(courses, [Course_Section(8915)])

    def test_filter_open_classes(self):
        test_courses = [Course_Section(8913), Course_Section(8914), Course_Section(8915)]
        expected = [Course_Section(8914), Course_Section(8915)]
        courses = filter_open_classes(test_courses)
        self.assertEqual(courses, expected)


if __name__ == '__main__':
    unittest.main()
