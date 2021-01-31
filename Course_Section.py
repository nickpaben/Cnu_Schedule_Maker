from File_Management import *


class Course_Section:
    # Constructor for Course_Section with CRN input - if the CRN is valid, the function sets the rest of
    # the class's information based on the CRN.
    def __init__(self, crn):
        if crn_is_valid(crn):
            self.course, self.section, self.title, self.hours, self.llc, self.days, \
                self.time, self.location, self.instructor, self.available_seats = get_class_data_from_crn(crn)
        else:
            self.__set_defaults__()

    # Set default course information when there is no valid CRN to go off of.
    def __set_defaults__(self):
        self.crn = 0000
        self.course = "ABCD 123"
        self.section = 1
        self.title = "Default Course"
        self.hours = 3
        self.llc = ""
        self.days = "MWF"
        self.time = "0000-0050"
        self.location = "LUTR 101"
        self.instructor = "Someone"
        self.available_seats = 24

    # Returns the Course_Section object as a string.
    # Format: course-section - title
    # Example: CPSC255-1 - Programming for Applications
    def __str__(self):
        return self.course + "-" + str(self.section) + " - " + self.title


if __name__ == "__main__":
    course = Course_Section(8750)
    print(course.__str__())
