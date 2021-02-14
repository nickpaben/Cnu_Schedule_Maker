let searchCourses = (query) => {
    let foundCourses = [];
    if (Number.isInteger(parseInt(query))) {
        let crn = parseInt(query);
        if (crnIsValid(crn)) {
            foundCourses.append(courseSection(crn));
        }
    } else {
        if (query.indexOf(";") === -1) {
            return getClassesByName(query);
        } else {
            let subqueries = query.split(";");
            for (let i = 0; i < subqueries.length; i++) {
                subqueries[i] = subqueries[i].trim();
                console.log(subqueries[i] + " " + i);
                foundCourses = foundCourses.concat(getClassesByName(subqueries[i]));
            }
        }
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
                j = dayString.length;
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
        let teacherNames = course.instructors.split(";");
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