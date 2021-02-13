let searchCourses = (query) => {
    let foundCourses = [];
    if (Number.isInteger(parseInt(query))) {
        let crn = parseInt(query);
        if (crnIsValid(crn)) {
            foundCourses.append(courseSection(crn));
        }
    } else {
        return getClassesByName(query);
    }
    return foundCourses;
}

let getClassesByName = (className) => {
    foundCourses = [];
    for (let i = 0; i < courseData.length; i++) {
        let currentCourseData = courseData[i];
        if (currentCourseData.length > 1) {
            if (currentCourseData[1].indexOf(className) !== -1) {
                let crn = parseInt(currentCourseData[0]);
                foundCourses.push(courseSection(crn));
            }
        }
    }
    return foundCourses;
}

let filterClassesByDay = (courses, dayString) => {
    filteredCourses = [];
    for (let i = 0; i < courses.length; i++) {
        let days = courses[i].days;
        for (let j = 0; j < dayString.length; j++) {
            if (days.indexOf(dayString.charAt(j)) != -1) {
                filteredCourses.push(courses[i]);
            }
        }
    }
    return filteredCourses;
}

let filterClassesByLLC = (courses, llcArea = "") => {
    filteredCourses = [];
    for (let i = 0; i < courses.length; i++) {
        let course = courses[i];
        if (llcArea !== "") {
            if (course.llc.trim() == llcArea) {
                filteredCourses.push(course);
            }
        } else {
            if (course.llc.trim() !== "") {
                filteredCourses.push(course);
            }
        }
    }
    return filteredCourses;
}

let filterOpenClasses = (courses) => {
    let filteredCourses = [];
    for (let i = 0; i < courses.length; i++) {
        let course = courses[i];
        if (course.availableSeats > 0) {
            filteredCourses.push(course);
        }
    }
    return filteredCourses;
}

let filterClassesByTeacher = (courses, teacherName, excludingTeacher = false) => {
    let filteredCourses = [];
    for (let i = 0; i < courses.length; i++) {
        let course = courses[i];
        let teacherNames = course.instructor.split(";");
        let isTeaching = false;

        for (let j = 0; j < teacherNames.length; j++) {
            if (teacherNames[j].indexOf(teacherName) != -1) {
                isTeaching = true;
            }
        }
        if (isTeaching && !excludingTeacher || !isTeaching && excludingTeacher) {
            filteredCourses.push(course);
        }
    }
    return filteredCourses;
}

/**
 * 

# Iterates through courses and returns only classes with the teacher if excluding_teacher = False.
# If excluding_teacher = True, the function filters out classes with the teacher and returns everything else.
def filter_classes_by_teacher(courses, teacher_name, excluding_teacher=False):
    filtered_courses = []
    for course in courses:
        teacher_names = course.instructor.split(";")
        is_teaching = False

        for name in teacher_names:
            if teacher_name.strip() in name.strip():
                is_teaching = True
        if is_teaching and not excluding_teacher:
            filtered_courses.append(course)
        if not is_teaching and excluding_teacher:
            filtered_courses.append(course)
    for f in filtered_courses:
        print(f)
    return filtered_courses


# Iterates through courses and returns only classes within the time range start - end.
def filter_classes_by_time(courses, start, end):
    filtered_courses = []
    for course in courses:
        start_time, end_time = course.time.split("-")
        if int(start_time) >= int(start) and int(end) >= int(end_time):
            filtered_courses.append(course)
    return filtered_courses
 */