from flaskapp import app, db
from flask import make_response, request
from .tables import Subject
from datetime import datetime, timedelta
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

@app.route('/')
def index():
    return app.send_static_file('index.html')

# @app.route("/api/test", methods=['POST', 'GET'])
# def test():
#     if request.method == 'GET':
#         Subject.query.delete()
#         classes = get_data(get_cookies())
#         subject_obj = parse_json(classes)
#         db.session.add_all(subject_obj)
#         db.session.commit()

#         # resp = jsonify(success=True)
#         return 'success'

#         # parse_json()



@app.route("/api/getcsv", methods=['POST'])
def getcsv():
    if request.method == 'POST':
        # print(request.data)
        crns = set(request.json['crns'])
        # print(crns)
        # crns = ['31406', '31407', '30033', '30036', '33957', '30139', '30141', '30248', '30588']
        df_csv = create_df(crns).to_csv(index=False)
        # return send_file(df_csv, mimetype='text/csv',as_attachment=True)
        response = make_response(df_csv)
        response.headers['Content-Disposition'] = 'attachment; filename=classes.csv'
        response.mimetype = 'text/csv'
        # return the Response object
        return response
        # return df.to_html()
        # df = create_df()
        # print(df['Subject'])
