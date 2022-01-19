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

def get_cal(crns):
    columns = ["Subject", "Start date", "Start Time", "End Time", "Description", "Location"]
    main_df = pd.DataFrame(columns=columns)
    for crn in crns:
        class_dict=get_class(crn)
        exam = False
        if('exam' in class_dict):
            exam = True
            dates = get_date(class_dict["start - end"], class_dict["days"]) + get_date(class_dict["exam_start - end"], class_dict["exam_week"])
        else:
            dates = get_date(class_dict["start - end"], class_dict["days"])
        df = pd.DataFrame(columns=columns)
        df["Start date"] = dates
        df["Subject"] = class_dict["course title"]
        split_timevar = split_time(class_dict["time"])
        df["Start Time"] = split_timevar[0]
        df["End Time"] = split_timevar[1]
        df["Description"] = f"""CRN: {crn} Course #: {class_dict["course #"]} Units: {class_dict["units"]} Instructor: {class_dict["instructor"]}"""
        df["Location"] = class_dict["bldg/rm"]

        if(exam):
            df.iloc[-1, 0] = class_dict["course title"] + "-EXAM"
            split_timevar = split_time(class_dict["exam_time"])
            df.iloc[-1, 2] = split_timevar[0]
            df.iloc[-1, 3] = split_timevar[1]
            df.iloc[-1, 4] = "Good luck on your exams!"
            df.iloc[-1, 5] = class_dict["exam_bldg/rm"]
        main_df = main_df.append(df, ignore_index=True)
        
    return main_df

# crn = 15124
# class_dict = get_class(crn)
# print(class_dict)