import csv
import os

course_list = 'ScheduleOfClasses2020f.csv'


def get_data(path):
    crn = []
    course = []
    title = []
    credit_hours = []
    days = []
    time = []
    with open(path, 'rt') as file:
        data = csv.reader(file)
        for line in data:
            if line[0] != 'CRN':
                crn.append(line[0])
                course.append(line[1])
                title.append(line[3])
                credit_hours.append(line[4])
                days.append(line[7])
                time.append(line[8])
    i = 0
    while i < len(crn):
        # if (days[i] + " " + time[i]).find(";") != -1:
        #     print(crn[i], "  ", title[i], "  ", course[i], " ", days[i], time[i])
        # if course[i] == 'HIST 312':
        #     print(crn[i], '\t', title[i])
        if days[i] == '' or time[i] == '':
            # print(crn[i], "  ", title[i], "  ", course[i])
            crn.pop(i)
            course.pop(i)
            title.pop(i)
            credit_hours.pop(i)
            days.pop(i)
            time.pop(i)
            i -= 1
        else:
            i += 1

    return crn, course, title, credit_hours, days, time


# Returns all data of a class with the CRN from the CSV file.
def get_class_data_from_crn(input_crn):
    with open("Data/ScheduleOfClasses2020f.csv", 'rt') as file:
        data = csv.reader(file)
        for line in data:
            if line[0] != 'CRN':
                crn = line[0]
                if input_crn == int(crn):
                    course = line[1]
                    section = line[2]
                    title = line[3]
                    credit_hours = line[4]
                    llc_area = line[5]
                    days = line[7]
                    time = line[8]
                    location = line[9]
                    instructor = line[10]
                    available_seats = line[11]
                    return course, section, title, credit_hours, llc_area, days, \
                           time, location, instructor, available_seats


def get_name(crn):
    crn_list, course, title, credit_hours, days, time = get_data(os.path.join("Data", course_list))
    index = -1
    for crns in range(len(crn_list)):
        if int(crn_list[crns]) == crn:
            index = crns
    return course[index]


def crn_is_valid(crn):
    crn_list, course, title, credit_hours, days, time = get_data(os.path.join("Data", course_list))
    for classes in crn_list:
        if int(classes) == crn:
            return True
    return False


def get_final_time(class_time, crn):

    # these first crns catch the edge cases to assure correct final time

    # if crn == 8268:
    #     final_time = 'M3'
    #
    # elif crn == 8492:
    #     final_time = 'T5'
    #
    # elif crn == 8013:
    #     final_time = "S4"
    #
    # elif crn == 8269:
    #     final_time = 'M4'
    #
    # elif crn == 8246:
    #     final_time = 'F1'
    #
    # elif crn == 8247:
    #     final_time = 'F3'
    #
    # elif crn == 8266:
    #     final_time = 'M1'
    #
    # elif crn == 8267:
    #     final_time = 'M2'

    if class_time.find("0800") != -1 and class_time[:2] != "TR":
        final_time = "M1"

    elif class_time[:7] == "TR 0800" or class_time == "T 0830-1220" or class_time == "R 0830-1220":
        final_time = "T1"

    elif class_time.find("1000") != -1 or class_time == "MW 1030-1250":
        final_time = "M2"

    elif class_time == "TR 1100-1215" or class_time == "R 1100-1215" or class_time == "TR 1230-1320":
        final_time = "T2"

    elif class_time.find("1200") != -1:
        final_time = "M3"

    elif class_time == "TR 1400-1620" or class_time == "TR 1500-1615":
        final_time = "T3"

    elif class_time.find("1400") != -1 or class_time == "MW 1430-1545":
        final_time = "M4"

    elif class_time[:7] == "TR 1800" or class_time[:6] == "T 1800" or class_time[:6] == "R 1800" or class_time == "TR 1830-1945":
        final_time = "T4"

    elif class_time == "TR 0930-1045" or class_time == "R 0930-1215" or class_time == "TR 1030-1250":
        final_time = "R1"

    elif class_time.find("1300") != -1 or class_time == "W 1330-1720":
        final_time = "F3"

    elif class_time.find("1330") != -1 and class_time != "W 1330-1720":
        final_time = "R2"

    elif class_time.find("1630") != -1 or class_time == "T 1730-2020" or class_time.find("1600-1900") != -1:
        final_time = "R3"

    elif class_time.find("1500") != -1:
        final_time = "R4"

    elif class_time.find("0900") != -1 or class_time == "MW 0930-1045":
        final_time = "F1"

    elif class_time.find("1100") != -1:
        final_time = "F2"

    elif class_time.find("1600") != -1 or class_time.find("W 1700") != -1:
        final_time = "F4"

    elif class_time.find("1800") != -1 or class_time == "M 1730-2020":
        final_time = "S1"

    elif class_time == "TR 1930-2045" or class_time[:6] == "T 1930" or class_time[:6] == "T 2000" or class_time[:6] == "R 2000" or class_time == "TR 2100-2215":
        final_time = "S2"

    elif class_time == "MW 1930-2045" or class_time[:6] == "W 1930" or class_time[:6] == "M 1930" or class_time[:6] == "M 2000" or class_time[:6] == "W 2000" or class_time[:7] == "MW 2100-2215":
        final_time = "S3"

    else:
        final_time = "Error"

    return final_time


if __name__ == "__main__":
    print(get_final_time("M 2000", 8016))
    # get_data("Data/ScheduleOfClasses2020f.csv")
    print(get_name(8781))
    get_class_data_from_crn(8781)

