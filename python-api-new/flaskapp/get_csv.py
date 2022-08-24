# file that takes in crn numbers and returns a csv
from flaskapp import db
import pandas as pd
from .tables import Subject
from sqlalchemy import select
from dateutil.rrule import rrule, WEEKLY
from datetime import datetime

# def get_csv(crns):
    # print(Subject.query.all())
    # print(type(Subject.query.get(31406).course_name))
    # columns = ["Subject", "Start date", "Start Time", "End Time", "Description", "Location"]
    # main_df = pd.DataFrame(columns=columns)
    # exam_description = 'Good luck with your exams!'
    # # for crn in crns:
    # subject = Subject.query.get(crn)
    # name = f"{subject.course_name[:20]}-{subject.class_type}"
    # start_time = subject.start_time
    # end_time = subject.end_time
    # days = subject.days
    # description = f"CRN: {crn} Course #: {subject.course_number} Instructor(s): {subject.instructor}"
    # exam_time = subject.exam_time
    # exam_end_time = subject.exam_end_time
    # exam_location = subject.exam_location

def map_dates(crn):
    subject = Subject.query.get(crn)
    # subject.start_time
    # TODO use rruleset to exclude holidays
    # print(f"{subject.days}")
    dates = list(rrule(
        WEEKLY,
        byweekday=(subject.days),
        dtstart=subject.start_time,
        until=subject.end_time
    ))
    return dates
    # print(dates)

def create_df(crns):
    df = pd.read_sql(
        select(Subject).where(Subject.crn.in_(crns)),
        db.engine,
        index_col='crn',
        columns=["course_name", "class_type", "course_number", "instructor", "location"]
    )
    df["Subject"] = df['course_name'].str[:22] + '-' + df['class_type']
    df["Description"] = 'CRN: ' + df.index.map(str) + " Course #: " + df["course_number"] + " Instructor(s): " + df['instructor']
    # print(df.loc[31406])
    print(df.index.map(map_dates))
    return df