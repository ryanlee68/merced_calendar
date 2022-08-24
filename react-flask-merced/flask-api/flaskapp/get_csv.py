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
    )
    df["Subject"] = df['course_name'].str[:22] + '-' + df['class_type']
    df["Description"] = 'CRN: ' + df.index.map(str) + " Course #: " + df["course_number"] + " Instructor(s): " + df['instructor']
    dfs = []
    for index, row in df.iterrows():
        row_df = row.to_frame().T
        row_df['Start Time'] = row['start_time'].time()
        row_df['End Time'] = row['end_time'].time()
        dates = map_dates(row) + [row['exam_time'].date()]
        new = row_df.merge(pd.DataFrame({'dates': dates}), how='cross')
        if pd.isna(row['exam_time']):
            new.iloc[-1, row_df.columns.get_loc('Start Time')] = None
            new.iloc[-1, row_df.columns.get_loc('End Time')] = None

        else:
            new.iloc[-1, row_df.columns.get_loc('Start Time')] = row['exam_time'].time()
            new.iloc[-1, row_df.columns.get_loc('End Time')] = row['exam_end_time'].time()
            new.iloc[-1, row_df.columns.get_loc('Description')] = 'Good luck 🍀 on your exams! 🙃'
        new.iloc[-1, row_df.columns.get_loc('location')] = row['exam_location']
        dfs.append(new)
    df = pd.concat(dfs, ignore_index=True).drop(
        [
            'course_number',
            'course_name',
            'class_type',
            'days',
            'instructor',
            'seats_avail',
            'start_time',
            'end_time',
            'exam_time',
            'exam_end_time',
            'exam_location',
        ],
        axis=1
    ).rename(
        {'location': 'Location', 'dates': 'Start date'},
        axis=1
    ).reindex(
        columns=[
            'Subject',
            'Start date',
            'Start Time',
            'End Time',
            'Description',
            'Location'
        ]
    )
    return df
