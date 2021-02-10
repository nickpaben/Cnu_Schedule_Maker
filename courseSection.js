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

let courseSection = (CRN) => {
    let course = {
        crn : 0000,
        course : "ABCD 123",
        section : 1,
        title : "Default Course",
        hours : 3,
        llc : "",
        days : "MWF",
        startTime : 8,
        lengthMinutes: 50,
        endTime : this.startTime + (this.lengthMinutes / 60),
        location : "LUTR 101",
        instructor : "Someone",
        availableSeats : 24,
        timeString : function(time) {
            let minutes = (time % 1) * 60;
            return Math.floor(time) + ":" + ("00" + Math.floor(minutes)).slice(-2);
        },
        toString : function() {
            return this.course + "-" + this.section + " - " + this.days + " " + this.timeString(this.startTime) + " - " 
                + this.timeString(this.endTime);
        },
        equals : function(otherCourse) {
            return (this.crn === otherCourse.crn);
        },
        setTime : function(time) {
            let timeString = time.split("-");
            this.startTime = Math.floor(parseInt(timeString[0]) / 100) + (parseInt(timeString[0]) % 100) / 60;
            this.endTime = Math.floor(parseInt(timeString[1]) / 100) + (parseInt(timeString[1]) % 100) / 60;
            this.lengthMinutes = (this.endTime - this.startTime) * 60;
        }
    };
    if (crnIsValid(CRN)) {
        let data = getClassDataFromCRN(CRN);
        course.crn = CRN;
        course.course = data.course;
        course.section = data.section;
        course.title = data.title;
        course.hours = data.hours;
        course.llc = data.llc;
        course.days = data.days;        
        course.setTime(data.time);
        course.location = data.location;
        course.instructor = data.instructor;
        course.availableSeats = data.availableSeats;
    }
    return course;
}