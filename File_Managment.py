import csv
import os

final_schedule = {'MWF 0800-0850': 'M1', 'MTWRF 0800-0850': 'M1', 'M 0800-0850': 'M1',
                  'MW; F 0800-0915; 0800-0850': 'M1', 'MW 0800-1020': 'M1', 'W 0800-1045': 'M1',
                  'MTWRF 0800-1550': 'M1', 'MWF 1000-1050': 'M2', 'M 1000-1050': 'M2',
                  'MW; F 1000-1115; 1000-1050': 'M2', 'W 1000-1050': 'M2', 'F 1000-1050': 'M2',
                  'M 1000-1145': 'M2', 'MW 1030-1250': 'M2', 'MWF 1200-1250': 'M3', 'MW 1200-1250': 'M3',
                  'MF 1200-1250': 'M3', 'M 1200-1250': 'M3', 'W 1200-1250': 'M3', 'F 1200-1250': 'M3',
                  'MW 1200-1315': 'M3', 'W 1200-1345': 'M3', 'F 1200-1345': 'M3', 'M 1200-1350': 'M3',
                  'W 1200-1350': 'M3', 'MWF 1400-1450': 'M4', 'MW 1400-1450': 'M4', 'M 1400-1450': 'M4',
                  'W 1400-1450': 'M4', 'F 1400-1450': 'M4', 'MW; F 1400-1515; 1400-1450': 'M4',
                  'M 1400-1550': 'M4', 'MW 1400-1620': 'M4', 'M 1400-1645': 'M4', 'F 1400-1700': 'M4',
                  'MW 1430-1545': 'M4', 'TR 0800-0915': 'T1', 'TR 0800-1020': 'T1', 'TR 0800-1030': 'T1',
                  'T 0830-1220': 'T1', 'R 0830-1220': 'T1', 'TR 1100-1215': 'T2', 'R 1100-1215': 'T2',
                  'TR 1230-1320': 'T2', 'TR 1400-1620': 'T3', 'TR 1500-1615': 'T3', 'TR 1800-1915': 'T4',
                  'T 1800-1945': 'T4', 'R 1800-1945': 'T4', 'T 1800-1950': 'T4', 'R 1800-1950': 'T4',
                  'T 1800-2000': 'T4', 'R 1800-2000': 'T4', 'T 1800-2045': 'T4', 'R 1800-2045': 'T4',
                  'T 1800-2100': 'T4', 'R 1800-2100': 'T4', 'T 1800-2150': 'T4', 'R 1800-2150': 'T4',
                  'TR 1830-1945': 'T4', 'TR 0930-1045': 'R1', 'R 0930-1215': 'R1', 'TR 1030-1250': 'R1',
                  'TR 1330-1420': 'R2', 'TR 1330-1445': 'R2', 'T 1330-1515': 'R2', 'R 1330-1515': 'R2',
                  'R 1330-1600': 'R2', 'T 1330-1615': 'R2', 'R 1330-1615': 'R2', 'T 1330-1720': 'R2',
                  'R 1330-1720': 'R2', 'T 1600-1900': 'R3', 'R 1600-1900': 'R3', 'TR 1630-1745': 'R3',
                  'TR 1630-1820': 'R3', 'T 1630-1915': 'R3', 'R 1630-1915': 'R3', 'T 1730-2020': 'R3',
                  'MWF 1500-1550': 'R4', 'MTWRF 1500-1550': 'R4', 'MW 1500-1550': 'R4', 'M 1500-1550': 'R4'
                  , 'W 1500-1550': 'R4', 'W 1500-1615': 'R4', 'W 1500-1715': 'R4', 'M 1500-1745': 'R4',
                  'MWF 0900-0950': 'F1', 'M 0900-0950': 'R1', 'W 0900-0950': 'R1', 'F 0900-0950': 'R1',
                  'M 0900-1145': 'F1', 'W 0900-1250': 'F1', 'R 0900-1250': 'F1', 'MW 0930-1045': 'F1',
                  'MWF 1100-1150': 'F2', 'MW 1100-1150': 'F2', 'M 1100-1150': 'F2', 'W 1100-1150': 'F2',
                  'F 1100-1150': 'F2', 'MTWRF 1100-1150': 'F2', 'M 1100-1215': 'F2', 'MW 1100-1215': 'F2',
                  'MWF 1300-1350': 'F3', 'MW 1300-1415': 'F3', 'MW 1300-1430': 'F3', 'M 1300-1545': 'F3',
                  'W 1300-1545': 'F3', 'M 1300-1650': 'F3', 'W 1300-1650': 'F3', 'F 1300-1650': 'F3',
                  'W 1330-1720': 'F3', 'MW 1600-1650': 'F4', 'W 1600-1650': 'F4', 'MW 1600-1715': 'F4',
                  'W 1600-1745': 'F4', 'M 1600-1750': 'F4', 'F 1600-1750': 'F4', 'MW 1600-1750': 'F4',
                  'W 1600-1800': 'F4', 'M 1600-1845': 'F4', 'W 1600-1845': 'F4', 'MW 1600-1900': 'F4',
                  'W 1700-1750': 'F4', 'W 1700-1945': 'F4', 'M 1730-2020': 'S1', 'MW 1800-1915': 'S1',
                  'M 1800-1950': 'S1', 'M 1800-2000': 'S1', 'M 1800-2045': 'S1', 'W 1800-2045': 'S1',
                  'M 1800-2100': 'S1', 'W 1800-2100': 'S1', 'M 1800-2150': 'S1', 'W 1800-2150': 'S1',
                  'TR 1930-2045': 'S2', 'T 1930-2130': 'S2', 'T 1930-2215': 'S2', 'R 1930-2215': 'S2',
                  'T 2000-2200': 'S2', 'R 2000-2200': 'S2', 'TR 2100-2215': 'S2', 'MW 1930-2045': 'S3',
                  'W 1930-2115': 'S3', 'M 1930-2215': 'S3', 'M 2000-2150': 'S3', 'W 2000-2200': 'S3',
                  'MW 2100-2215': 'S3'}

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


def get_name(crn):
    crn_list, course, title, credit_hours, days, time = get_data(os.path.join("Data", course_list))
    index = -1
    for crns in range(len(crn_list)):
        if int(crn_list[crns]) == crn:
            index = crns
            print(index)
    return course[index]


def check_crn_valid(crn):  # input crn as a string
    crn_list, course, title, credit_hours, days, time = get_data(os.path.join("Data", course_list))
    for classes in crn_list:
        if classes == crn:
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

