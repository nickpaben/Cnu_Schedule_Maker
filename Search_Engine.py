from File_Managment import *

# Returns all courses that contain the string class_name in their registration name (ABCD 123).
# For example, searching using 'CPSC 4' should return all 400-level CPSC courses.
def get_classes_by_name (courses, class_name):
    found_courses = []
    for course in courses:
        if class_name in course:
            found_courses.append(course)
    return found_courses

# Returns the registration name (ABCD 123) of the class with the CRN inputted into the function.
# If the CRN is invalid, the function returns 'NONE'.
def get_classes_by_crn (crns, courses, class_crn):
    found_course = "NONE"
    for index in range(len(crns)):
        if class_crn == int(crns[index]):
            found_course = courses[index]
    return found_course

if __name__ == "__main__":
    crns, courses, titles, credit_hours, days, times = get_data("Data/ScheduleOfClasses2020f.csv")
    print(get_classes_by_name(courses, "BIOL 4"))
    print(get_classes_by_crn(crns, courses, 8120))