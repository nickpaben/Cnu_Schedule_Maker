from File_Managment import *


# Returns all courses that contain the string class_name in their registration name (ABCD 123).
# For example, searching using 'CPSC 4' should return all 400-level CPSC courses.
def get_classes_by_name(courses, class_name):
    found_courses = []
    for course in courses:
        if class_name in course:
            found_courses.append(course)
    return found_courses


# Returns the registration name (ABCD 123) of the class with the CRN inputted into the function.
# If the CRN is invalid, the function returns 'NONE'.
def get_classes_by_crn(crns, courses, class_crn):
    found_course = "NONE"
    for index in range(len(crns)):
        if class_crn == int(crns[index]):
            found_course = courses[index]
    return found_course


# Iterates through courses provided and returns only the courses containing days in day_string.
# day_string is a string containing all of the days to filter in - an example would be 'MTWF'.
# Using this string, the program should return all of the classes provided except for ones on Thursday (R).
# courses and days must be the same length for now - there's probably a better fix, but I'm not sure what
# that is yet.
# With the current way this is set up, searching 'MW' will also include 'MWF' classes - I need to fix that.
def filter_classes_by_day (courses, days, day_string):
    filtered_courses = []
    for index in range(len(courses)):
        for day in day_string:
            if day in days[index]:
                filtered_courses.append(courses[index])
                break
    return filtered_courses


# Iterates through courses and returns only classes that satisfy an LLC.
# If llc_area is specified, the function will return only courses with that specific LLC (ex. AINW).
def filter_by_llc(courses, llc_area=''):
    pass


# Iterates through courses and returns only classes with the teacher if exclude = False.
# If exclude = True, the function filters out classes with the teacher and returns everything else.
def filter_by_teacher(courses, teacher_name, exclude=False):
    pass


# Iterates through courses and returns only classes within the time range start - end.
def filter_by_time(courses, start, end):
    pass


# Iterates through courses and returns only classes with open slots left.
def filter_open_classes(courses):
    pass


if __name__ == "__main__":
    crns, courses, titles, credit_hours, days, times = get_data("Data/ScheduleOfClasses2020f.csv")
    print(get_classes_by_name(courses, "BIOL 4"))
    print(get_classes_by_crn(crns, courses, 8120))
    print(filter_classes_by_day(courses, days, 'MTWF'))
