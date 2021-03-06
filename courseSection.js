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
        arranged : false,
        location : "LUTR 101",
        instructors : "Someone",
        availableSeats : 24,
        timeString : function(time) {
            let minutes = (time % 1) * 60;
            return Math.floor(time) + ":" + ("00" + Math.floor(minutes)).slice(-2);
        },
        toString : function() {
            if (this.arranged) {
                return this.course + "-" + this.section + " (Arranged)";
            } else {
                return this.course + "-" + this.section + " - " + this.days + " " + this.timeString(this.startTime) + " - " 
                    + this.timeString(this.endTime);
            }
            
        },
        equals : function(otherCourse) {
            return (this.crn === otherCourse.crn);
        },
        setTime : function(time) {
            let timeString = time.split("-");
            if (Number.isInteger(parseInt(timeString[0]))) {
                this.startTime = Math.floor(parseInt(timeString[0]) / 100) + (parseInt(timeString[0]) % 100) / 60;
                this.endTime = Math.floor(parseInt(timeString[1]) / 100) + (parseInt(timeString[1]) % 100) / 60;
                this.lengthMinutes = (this.endTime - this.startTime) * 60;
            } else {
                this.arranged = true;
            }
            
        },
        getSubject : function() {
            return this.course.substring(0, 4);
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
        course.instructors = data.instructors;
        course.availableSeats = data.availableSeats;
    }
    return course;
}