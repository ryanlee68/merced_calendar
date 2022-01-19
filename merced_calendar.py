import pandas as pd
from merced import get_class
import collections
from datetime import datetime

def split_time(time):
    time = time.split("-")
    if(time[1][-2:] == "am"):
        if(int(time[1][:-5]) == 12):
            time[0] += " pm"
            time[1] = time[1][:-2] + " am"
        else:
            time[0] += " am"
            time[1] = time[1][:-2] + " am"
    else:
        time[1] = time[1][:-2]
        first = int(time[0][:-3])
        last = int(time[1][:-3])
        if(last < first and first != 12):
            time[0] += " am"
            time[1] += " pm"
        elif(first < last and last != 12):
            time[0] += " pm"
            time[1] += " pm"
        elif(last < first and first == 12):
            time[0] += " pm"
            time[1] += " pm"
        else:
            time[0] += " am"
            time[1] += " pm"
    return time

months = {
    "jan":1,
    "feb":2,
    "mar":3,
    "apr":4,
    "may":5,
    "june":6,
    "july":7,
    "aug":8,
    "sept":9,
    "oct":10,
    "nov":11,
    "dec":12
}
days = {
    "M": "MON",
    "T": "TUE",
    "W": "WED",
    "R": "THU",
    "F": "FRI",
    "S": "SAT"

}

def get_date(sten, day):
    sten = sten.split(" ")
    start = sten[0].lower().split("-")
    end = sten[1].lower().split("-")
    start = datetime(2022, months[start[1]], int(start[0])).strftime("%m/%d/2022")
    end = datetime(2022, months[end[1]], int(end[0])).strftime("%m/%d/2022")
    gibbo = []
    day.split()
    for i in day:
        gibbo.extend(pd.date_range(start=start, end=end, 
                            freq=f'W-{days[i]}').strftime('%m/%d/2022').tolist())
    return gibbo

def get_cal(crn):
    a_dict = collections.defaultdict(list)
    for num in crn:
        class_dict = get_class(num)
        for day in get_date(class_dict["start - end"], class_dict["days"]):
            # columns = ["Subject", "Start date", "Start Time", "End Time", "Description", "Location"]
            a_dict["Subject"].append(class_dict["course title"] + "-" + class_dict["actv"])
            a_dict["Start Date"].append(day)
            split_timevar = split_time(class_dict["time"])
            a_dict["Start Time"].append(split_timevar[0])
            a_dict["End Time"].append(split_timevar[1])
            a_dict["Description"].append(f"""CRN: {num} Course #: {class_dict["course #"]} Units: {class_dict["units"]} Instructor: {class_dict["instructor"]}""")
            a_dict["Location"].append(class_dict["bldg/rm"])
        if('exam' in class_dict.keys()):
            a_dict["Subject"].append(class_dict["course title"] + "-EXAM")
            a_dict["Start Date"].append(get_date(class_dict["exam_start - end"], class_dict["exam_week"])[0])
            split_timevar = split_time(class_dict["exam_time"])
            a_dict["Start Time"].append(split_timevar[0])
            a_dict["End Time"].append(split_timevar[1])
            a_dict["Description"].append("Exam")
            a_dict["Location"].append(class_dict["exam_bldg/rm"])
    df = pd.DataFrame(data = a_dict)
    df.to_csv("classes.csv", index=False)
    return df

# get_cal([15124, 15159, 15163, 16414, 16416, 17105, 15593, 15594])