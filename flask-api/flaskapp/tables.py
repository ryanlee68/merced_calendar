from sqlalchemy.ext.mutable import MutableList
# from sqlalchemy import Interval, PickleType
from dataclasses import dataclass, field
from datetime import datetime
from flaskapp import db
# d

# @dataclass
# class Exam:
#     exam_time: datetime
#     exam_locations: list[str] = field(default_factory=list)

class Subject(db.Model):
    crn = db.Column(db.Integer, primary_key=True)
    course_number = db.Column(db.String(120), nullable=False) #ANTH-005-01
    course_name = db.Column(db.String(120), nullable=False) #Biological Anthropology
    class_type = db.Column(db.String(120), nullable=False) #LECT
    days = db.Column(MutableList.as_mutable(db.PickleType), nullable=True) #TR(tuesday thursday)
    start_time = db.Column(db.DateTime, nullable=True)
    end_time = db.Column(db.DateTime, nullable=True)
    location = db.Column(db.String(120), nullable=True)
    instructor = db.Column(db.String(120), nullable=False)
    seats_avail = db.Column(db.Integer, nullable=False)
    # exam below
    exam_time = db.Column(db.DateTime, nullable=True)
    exam_end_time = db.Column(db.DateTime, nullable=True)
    exam_location = db.Column(db.String(120), nullable=True)
    