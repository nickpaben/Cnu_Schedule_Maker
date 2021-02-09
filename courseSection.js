/** from File_Management import *


class Course_Section:
    # Constructor for Course_Section with CRN input - if the CRN is valid, the function sets the rest of
    # the class's information based on the CRN.
    def __init__(self, crn):
        if crn_is_valid(crn):
            self.crn = crn
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

    # Compares this object to another course; returns True if CRNs are equal
    def __eq__(self, other):
        return self.crn == other.crn


if __name__ == "__main__":
    course = Course_Section(8750)
    print(course.__str__())
**/

let courseSection = () => {
    let defaultCourse = {
        crn : 0000,
        course : "ABCD 123",
        section : 1,
        title : "Default Course",
        hours : 3,
        llc : "",
        days : "MWF",
        time : "0800-0850",
        location : "LUTR 101",
        instructor : "Someone",
        available_seats : 24,
        toString : function() {
            return this.course + "-" + this.section + " - " + this.title;
        },
        equals : function(otherCourse) {
            return (this.crn === otherCourse.crn);
        }
    };
    return defaultCourse;
}