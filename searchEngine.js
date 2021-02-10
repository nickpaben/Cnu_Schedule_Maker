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