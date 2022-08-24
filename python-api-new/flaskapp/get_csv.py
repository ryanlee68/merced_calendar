# file that takes in crn numbers and returns a csv
from dateutil.rrule import rrule, WEEKLY
from sqlalchemy import select
from .tables import Subject
from flaskapp import db
import pandas as pd

def map_dates(series: pd.Series):
    dates = list(rrule(
        WEEKLY,
        byweekday=(series['days']),
        dtstart=series['start_time'].date(),
        until=series['end_time'].date()
    ))
    return dates

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
