import os
from Course_Section import Course_Section


# Returns all courses that contain the string class_name in their registration name (ABCD 123).
# For example, searching using 'CPSC 4' should return all 400-level CPSC courses.
def get_classes_by_name(courses, crns, class_name):
    found_courses = []
    for index in range(len(courses)):
        course = courses[index]
        if class_name in course:
            crn = crns[index]
            found_courses.append(Course_Section(crn))
    return found_courses


# Returns a course object of the class with the CRN inputted into the function.
def get_class_by_crn(class_crn):
    return Course_Section(class_crn)


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


if __name__ == "__main__":
    pass
