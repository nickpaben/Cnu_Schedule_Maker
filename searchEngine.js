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
    filteredCourses = []
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

/**
 * 
# Iterates through courses provided and returns only the courses containing days in day_string.
# day_string is a string containing all of the days to filter in - an example would be 'MTWF'.
# Using this string, the program should return all of the classes provided except for ones only on Thursday (R).
def filter_classes_by_day(courses, day_string):
    filtered_courses = []
    for course in courses:
        for day in day_string:
            if day in course.days:
                filtered_courses.append(course)
                break
    return filtered_courses


# Iterates through courses and returns only classes that satisfy an LLC.
# If llc_area is specified, the function will return only courses with that specific LLC (ex. AINW).
def filter_classes_by_llc(courses, llc_area=""):
    filtered_courses = []
    for course in courses:
        if llc_area != "":
            if course.llc.strip() == llc_area.strip():
                filtered_courses.append(course)
        else:
            if course.llc.strip() != "":
                filtered_courses.append(course)

    return filtered_courses


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


# Iterates through courses and returns only classes with open slots left.
def filter_open_classes(courses):
    filtered_courses = []
    for course in courses:
        if int(course.available_seats) > 0:
            filtered_courses.append(course)
    return filtered_courses

 */