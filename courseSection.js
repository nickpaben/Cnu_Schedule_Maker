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