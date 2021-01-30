from File_Managment import *


def get_classes_by_name (courses, class_name):
    found_courses = []
    for course in courses:
        if course == class_name:
            found_courses.append(course)
    return found_courses


if __name__ == "__main__":
    crns, courses, titles, credit_hours, days, times = get_data("Data/ScheduleOfClasses2020f.csv")
    print(get_classes_by_name(courses, "BIOL 211"))