from File_Management import *
import os


class Final:

    course_list_path = "ScheduleOfClasses2020f.csv"

    def __init__(self, crn, weight=1, desired_grade=1, current_grade=1, confidence=5):
        self.title, self.name, self.credit_hours, self.class_date, self.class_time = self._get_attributes(crn)
        self.crn = crn
        self.confidence = confidence
        self.combined_time = self.class_date + " " + self.class_time
        self.final_weight = weight
        self.desired_grade = desired_grade
        self.current_grade = current_grade
        self.final_position = get_final_time(self.combined_time, crn)
        self.grade_needed = (self.desired_grade - (self.current_grade * (1 - self.final_weight / 100))) / (self.final_weight / 100)
        self.num_blocks = 0
        self.home_view_coordinates = []
        self.advanced_view_coordinates = []
        self.color = ''
        self.entered_info = False

    @staticmethod
    def _get_attributes(crn):
        crn_list, course_list, title_list, credit_hours_list, days_list, time_list = get_data(os.path.join(
            'Data', "ScheduleOfClasses2020f.csv"))
        found = False
        count = 0
        while count < len(crn_list) and not found:
            if crn_list[count] == crn:
                found = True
            else:
                count += 1
        if found:
            return course_list[count], title_list[count], credit_hours_list[count], days_list[count], time_list[count]

        raise IndexError

    def __eq__(self, other):
        return self.final_position == other.final_position

    def set_final_weight(self, weight):
        self.final_weight = weight
        self.grade_needed = (self.desired_grade - (self.current_grade * (1 - self.final_weight / 100))) / (self.final_weight / 100)

    def set_final_time(self, time):
        self.final_position = time

    def set_num_blocks(self, num):
        self.num_blocks = num

    def set_color(self, hex_value):
        self.color = hex_value

    def set_desired_grade(self, desired_grade):
        self.desired_grade = desired_grade
        self.grade_needed = (self.desired_grade - (self.current_grade * (1 - self.final_weight / 100))) / (self.final_weight / 100)

    def set_current_grade(self, current_grade):
        self.current_grade = current_grade
        self.grade_needed = (self.desired_grade - (self.current_grade * (1 - self.final_weight / 100))) / (self.final_weight / 100)

    def set_confidence(self, confidence):
        self.confidence = confidence

    def set_home_view_coordinates(self, coordinates):
        self.home_view_coordinates = coordinates

    def set_advanced_view_coordinates(self, coordinates):
        self.advanced_view_coordinates = coordinates

    def set_entered_info(self, tf):
        self.entered_info = tf

    def get_entered_info(self):
        return self.entered_info

    def get_home_view_coordinates(self):
        return self.home_view_coordinates

    def get_advanced_view_coordinates(self):
        return self.advanced_view_coordinates

    def get_name(self):
        return self.name

    def get_final_weight(self):
        return self.final_weight

    def get_color(self):
        return self.color

    def get_credit_hours(self):
        return self.credit_hours

    def get_crn(self):
        return self.crn

    def get_num_blocks(self):
        return self.num_blocks

    def get_title(self):
        return self.title

    def get_class_time(self):
        return self.class_time

    def get_class_date(self):
        return self.class_date

    def get_combined_time(self):
        return self.combined_time

    def get_final_position(self):
        return self.final_position

    def get_confidence(self):
        return self.confidence

    def get_grade_needed(self):
        self.grade_needed = (self.desired_grade - (self.current_grade * (1 - self.final_weight / 100))) / (
                self.final_weight / 100)
        return self.grade_needed


class ManualFinal:

    def __int__(self, final_time, class_title, crn=0, name="", class_date="", class_time="", final_weight=1, confidence=5, current_grade=1, desired_grade=1, credit_hours=1):
        try:
            self.class_title, self.name, self.credit_hours, self.class_date, self.class_time = self._get_attributes(crn)
        except IndexError:
            self.credit_hours = credit_hours
            self.class_title = class_title
            self.class_time = class_time
            self.class_date = class_date
            pass

        self.final_position = final_time
        self.combined_time = class_time + " " + class_date
        self.crn = crn
        self.grade_needed = (desired_grade - (current_grade * (1 - final_weight / 100))) / (final_weight / 100)
        self.final_weight = final_weight
        self.desired_grade = desired_grade
        self.confidence = confidence
        self.current_grade = current_grade
        self.num_blocks = 0
        self.home_view_coordinates = []
        self.advanced_view_coordinates = []
        self.color = ''
        self.entered_info = False

    def __eq__(self, other):
        return self.get_final_time() == other.get_final_time()

    @staticmethod
    def _get_attributes(crn):
        crn_list, course_list, title_list, credit_hours_list, days_list, time_list = get_data(os.path.join(
            'Data', 'ScheduleOfClasses2020f.csv'))
        found = False
        count = 0
        while count < len(crn_list) and not found:
            if crn_list[count] == crn:
                found = True
            else:
                count += 1
        if found:
            return course_list[count], title_list[count], credit_hours_list[count], days_list[count], time_list[count]

        raise IndexError

    def set_final_weight(self, weight):
        self.final_weight = weight
        self.grade_needed = (self.desired_grade - (self.current_grade * (1 - self.final_weight / 100))) / (
                self.final_weight / 100)

    def set_final_place(self, time):
        self.final_place = time

    def set_color(self, hex_value):
        self.color = hex_value

    def set_class_time(self, time):
        self.class_time = time
        self.combined_time = self.class_time + " " + self.class_date

    def set_class_date(self, date):
        self.class_date = date
        self.combined_time = self.class_time + " " + self.class_date

    def set_class_title(self, title):
        self.class_title = title

    def set_desired_grade(self, desired_grade):
        self.desired_grade = desired_grade
        self.grade_needed = (self.desired_grade - (self.current_grade * (1 - self.final_weight / 100))) / (
                    self.final_weight / 100)

    def set_current_grade(self, current_grade):
        self.current_grade = current_grade
        self.grade_needed = (self.desired_grade - (self.current_grade * (1 - self.final_weight / 100))) / (
                    self.final_weight / 100)

    def set_confidence(self, confidence):
        self.confidence = confidence

    def set_credit_hours(self, hours):
        self.credit_hours = hours

    def set_num_blocks(self, num):
        self.num_blocks = num

    def set_home_view_coordinates(self, coordinates):
        self.home_view_coordinates = coordinates

    def set_advanced_view_coordinates(self, coordinates):
        self.advanced_view_coordinates = coordinates

    def set_entered_info(self, tf):
        self.entered_info = tf

    def get_entered_info(self):
        return self.entered_info

    def get_home_view_coordinates(self):
        return self.home_view_coordinates

    def get_advanced_view_coordinates(self):
        return self.advanced_view_coordinates

    def get_credit_hours(self):
        return self.credit_hours

    def get_crn(self):
        return self.crn

    def get_title(self):
        return self.class_title

    def get_color(self):
        return self.color

    def get_class_time(self):
        return self.class_time

    def get_class_date(self):
        return self.class_date

    def get_combined_time(self):
        return self.combined_time

    def get_final_position(self):
        return self.final_position

    def get_confidence(self):
        return self.confidence

    def get_final_time(self):
        return self.final_position

    def get_num_blocks(self):
        return self.num_blocks

    def get_grade_needed(self):
        self.grade_needed = (self.desired_grade - (self.current_grade * (1 - self.final_weight / 100))) / (
                self.final_weight / 100)
        return self.grade_needed


if __name__ == "__main__":
    test_crns, test_courses, test_titles, test_credit_hours, test_days, test_times = get_data(os.path.join('Data', "ScheduleOfClasses2020f.csv"))
    Final('9001')
