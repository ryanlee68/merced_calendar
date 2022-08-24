from flaskapp import app, db
from flask import Flask, render_template, url_for, request, redirect, send_file
from .tables import Subject
from datetime import datetime, timedelta
from .data import get_data, get_cookies
from .parser import parse_json
from .get_csv import create_df
from calendar import (
    MONDAY,
    TUESDAY,
    WEDNESDAY,
    THURSDAY,
    FRIDAY,
    SATURDAY,
    SUNDAY
)

@app.route("/test", methods=['POST', 'GET'])
def test():
    if request.method == 'GET':
        Subject.query.delete()
        classes = get_data(get_cookies())
        subject_obj = parse_json(classes)
        # exam_obj = Exam(datetime(2022, 8, 22, 15, 30), ['COB 210'])
        # subject_obj = Subject(
        #     crn=36566,
        #     course_number = 'ANTH-005-01',
        #     course_name = 'Biological Anthropology',
        #     class_type = 'LECT',
        #     days = [TUESDAY, THURSDAY],
        #     start_time = datetime(2022, 8, 22, 15, 30),
        #     time_delta = timedelta(hours=1, minutes=15),
        #     location = 'CLSSRM 102',
        #     end_date = datetime(2022, 12, 22),
        #     instructor = 'Wooding, Stephen',
        #     seats_avail = 0,
        #     exam = exam_obj,
        # )
        db.session.add_all(subject_obj)
        db.session.commit()

@app.route("/getcsv", methods=['GET'])
def getcsv():
    if request.method == 'GET':
        crns = ['31406', '31407', '30033', '30036', '33957', '30139', '30141', '30248', '30588']
        df = create_df(crns)
        print(df)
        return df.to_html()
        # df = create_df()
        # print(df['Subject'])