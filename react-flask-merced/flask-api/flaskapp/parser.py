# parsing for script.py
from .data import get_data, get_cookies
from datetime import datetime
from .tables import Subject
from flaskapp import db

import calendar

# import json

# with open('sample.json', 'w') as file:
#     json.dump(get_data(get_cookies()), file, indent=4)

# classes = get_data(get_cookies())
def parse_json(classes:list[dict]) -> list[Subject]:
    subjects = []
    for class_ in classes:
        subject_dict = {}
        # exam_dict = {}

        for meeting in class_['meetingsFaculty']:
            print(class_['courseReferenceNumber'])
            if meeting['meetingTime']['meetingType'] != 'EXAM':
                subject_dict['class_type'] = meeting['meetingTime']['meetingType']
                subject_dict['location'] = f"{meeting['meetingTime']['building']} {meeting['meetingTime']['room']}"
                if meeting['meetingTime']['beginTime'] == None:
                    subject_dict['start_time'] = None
                    subject_dict['end_time'] = None
                else:
                    begin_time = meeting['meetingTime']['beginTime']
                    final_time = meeting['meetingTime']['endTime']

                    subject_dict['start_time']=datetime.strptime(meeting['meetingTime']['startDate'], '%m/%d/%Y').replace(hour=int(begin_time[:2]), minute=int(begin_time[2:]))

                    subject_dict['end_time']=datetime.strptime(meeting['meetingTime']['endDate'], '%m/%d/%Y').replace(hour=int(final_time[:2]), minute=int(final_time[2:]))

                    days = []
                    for day in [
                        'monday', 
                        'tuesday', 
                        'wednesday', 
                        'thursday',
                        'friday',
                        'saturday',
                        'sunday'
                    ]:
                        if meeting['meetingTime'][day]:
                            # days.append(day)
                            days.append(getattr(calendar, day.upper()))
                    subject_dict['days'] = days
            else:
                if meeting['meetingTime']['beginTime'] == None:
                    subject_dict['exam_time'] = None
                    subject_dict['exam_end_time'] = None
                    subject_dict['exam_location'] = f"{meeting['meetingTime']['building']} {meeting['meetingTime']['room']}"
                else:
                    exam_begin_time = meeting['meetingTime']['beginTime']
                    exam_final_time = meeting['meetingTime']['endTime']
                    # print(f"{exam_begin_time=}")
                    subject_dict['exam_time'] = datetime.strptime(meeting['meetingTime']['startDate'], '%m/%d/%Y').replace(hour=int(exam_begin_time[:2]), minute=int(exam_begin_time[2:]))
                    subject_dict['exam_end_time'] = datetime.strptime(meeting['meetingTime']['endDate'], '%m/%d/%Y').replace(hour=int(exam_final_time[:2]), minute=int(exam_final_time[2:]))
                    subject_dict['exam_location'] = f"{meeting['meetingTime']['building']} {meeting['meetingTime']['room']}"

            


        # if class_['meetingsFaculty'][0]['meetingtime']['beginTime'] is None:
        #     start_time=None
        #     end_time=None
        #     days = None
        # for meeting in class_['meetingsFaculty']:
        #     if meeting['meetingtime']['meetingType'] != 'EXAM':


        # elif len(class_['meetingsFaculty']) > 1:
        #     if class_['meetingsFaculty'][1]['meetingTime']['beginTime'] == None:
        #         exam_dict['exam_time'] = None
        #         exam_dict['exam_end_time'] = None
        #         exam_dict['exam_location'] = f"{class_['meetingsFaculty'][1]['meetingTime']['building']} {class_['meetingsFaculty'][1]['meetingTime']['room']}"
        #     else:
        #         exam_begin_time = class_['meetingsFaculty'][1]['meetingTime']['beginTime']
        #         exam_final_time = class_['meetingsFaculty'][1]['meetingTime']['endTime']
        #         # print(f"{exam_begin_time=}")
        #         exam_dict['exam_time'] = datetime.strptime(class_['meetingsFaculty'][1]['meetingTime']['startDate'], '%m/%d/%Y').replace(hour=int(exam_begin_time[:2]), minute=int(exam_begin_time[2:]))
        #         exam_dict['exam_end_time'] = datetime.strptime(class_['meetingsFaculty'][1]['meetingTime']['endDate'], '%m/%d/%Y').replace(hour=int(exam_final_time[:2]), minute=int(exam_final_time[2:]))
        #         exam_dict['exam_location'] = f"{class_['meetingsFaculty'][1]['meetingTime']['building']} {class_['meetingsFaculty'][1]['meetingTime']['room']}"
        # else:

        #     begin_time = class_['meetingsFaculty'][0]['meetingTime']['beginTime']
        #     final_time = class_['meetingsFaculty'][0]['meetingTime']['endTime']

        #     start_time=datetime.strptime(class_['meetingsFaculty'][0]['meetingTime']['startDate'], '%m/%d/%Y').replace(hour=int(begin_time[:2]), minute=int(begin_time[2:]))

        #     end_time=datetime.strptime(class_['meetingsFaculty'][0]['meetingTime']['endDate'], '%m/%d/%Y').replace(hour=int(final_time[:2]), minute=int(final_time[2:]))

        #     days = []
        #     for day in [
        #         'monday', 
        #         'tuesday', 
        #         'wednesday', 
        #         'thursday',
        #         'friday',
        #         'saturday',
        #         'sunday'
        #     ]:
        #         if class_['meetingsFaculty'][0]['meetingTime'][day]:
        #             # days.append(day)
        #             days.append(getattr(calendar, day.upper()))
        
        
        # if class_['meetingsFaculty'][0]['meetingTime']['beginTime'] is None and class_['meetingsFaculty'][0]['meetingTime']['building'] is None:
        #     start_time=None
        #     end_time=None
        #     days = None

        # elif class_['meetingsFaculty'][0]['meetingTime']['beginTime'] is None:
        #     start_time=datetime.strptime(class_['meetingsFaculty'][0]['meetingTime']['startDate'], '%m/%d/%Y')
        #     end_time=datetime.strptime(class_['meetingsFaculty'][0]['meetingTime']['startDate'], '%m/%d/%Y')
        #     days = None
            
        # else:
        #     # begin_time = 1130
        #     # final_time = 1430


        #     begin_time = class_['meetingsFaculty'][0]['meetingTime']['beginTime']
        #     final_time = class_['meetingsFaculty'][0]['meetingTime']['endTime']

        #     start_time=datetime.strptime(class_['meetingsFaculty'][0]['meetingTime']['startDate'], '%m/%d/%Y').replace(hour=int(begin_time[:2]), minute=int(begin_time[2:]))

        #     end_time=datetime.strptime(class_['meetingsFaculty'][0]['meetingTime']['endDate'], '%m/%d/%Y').replace(hour=int(final_time[:2]), minute=int(final_time[2:]))

        #     days = []
        #     for day in [
        #         'monday', 
        #         'tuesday', 
        #         'wednesday', 
        #         'thursday',
        #         'friday',
        #         'saturday',
        #         'sunday'
        #     ]:
        #         if class_['meetingsFaculty'][0]['meetingTime'][day]:
        #             # days.append(day)
        #             days.append(getattr(calendar, day.upper()))

        # getting  list of teachers
        teachers = ''
        for teachers in class_['faculty']:
            teachers = f"{teachers['displayName']} {teachers['emailAddress']} / "
        subject_dict['instructor'] = teachers
        
        subject_dict['crn']=class_['courseReferenceNumber']
        subject_dict['course_name']=class_['courseTitle']
        subject_dict['course_number']=f"{class_['subject']}-{class_['courseNumber']}-{class_['sequenceNumber']}"
        subject_dict['seats_avail']=class_['seatsAvailable']

        # subject_dict['class_type']=class_['meetingsFaculty'][0]['meetingTime']['meetingType']

        # exam_dict = {}
        # if len(class_['meetingsFaculty']) > 1:
        #     if class_['meetingsFaculty'][1]['meetingTime']['beginTime'] == None:
        #         exam_dict['exam_time'] = None
        #         exam_dict['exam_end_time'] = None
        #         exam_dict['exam_location'] = f"{class_['meetingsFaculty'][1]['meetingTime']['building']} {class_['meetingsFaculty'][1]['meetingTime']['room']}"
        #     else:
        #         exam_begin_time = class_['meetingsFaculty'][1]['meetingTime']['beginTime']
        #         exam_final_time = class_['meetingsFaculty'][1]['meetingTime']['endTime']
        #         # print(f"{exam_begin_time=}")
        #         exam_dict['exam_time'] = datetime.strptime(class_['meetingsFaculty'][1]['meetingTime']['startDate'], '%m/%d/%Y').replace(hour=int(exam_begin_time[:2]), minute=int(exam_begin_time[2:]))
        #         exam_dict['exam_end_time'] = datetime.strptime(class_['meetingsFaculty'][1]['meetingTime']['endDate'], '%m/%d/%Y').replace(hour=int(exam_final_time[:2]), minute=int(exam_final_time[2:]))
        #         exam_dict['exam_location'] = f"{class_['meetingsFaculty'][1]['meetingTime']['building']} {class_['meetingsFaculty'][1]['meetingTime']['room']}"

        subjects.append(
            Subject(
                # crn=class_['courseReferenceNumber'],
                # course_number=f"{class_['subject']}-{class_['courseNumber']}-{class_['sequenceNumber']}",
                # course_name=class_['courseTitle'],
                # class_type=class_['meetingsFaculty'][0]['meetingTime']['meetingType'],
                # # days=days,
                # # "beginTime": "1500",
                # # "startDate": "08/24/2022",
                # # start_time=start_time,
                # # end_time=end_time,
                # # location=f"{class_['meetingsFaculty'][0]['meetingTime']['building']} {class_['meetingsFaculty'][0]['meetingTime']['room']}",
                # # instructor=teachers,
                # seats_avail=class_['seatsAvailable'],
                **subject_dict
            )
        )
    return subjects