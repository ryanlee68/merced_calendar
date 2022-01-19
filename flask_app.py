# made by ryan lee
from distutils.log import debug
from importlib.resources import path
from operator import methodcaller
from flask import Flask, render_template, url_for, request, redirect, send_file
from merced_calendar import get_cal


app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        crn_content = request.form['content']
        try:
            get_cal(crn_content.split(" "))
            path = "classes.csv"
            return send_file(path, as_attachment=True)
            return redirect(url_for('/index.html'))
        except Exception as e:
            return redirect(url_for('index_error.html'))
            return "Either you misstyped your crns, or theres a problem on my end, contact nayr#8772 on discord or email ryanlee619@gmail.com for and problems or questions" + str(e)
        
        return render_template('index.html')
    else:

        return render_template('index.html')
    
# @app.route('/download')
# def download_file():
#     path = "classes.csv"
#     return send_file(path, as_attachment=True)

# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update(id):
#     if request.method == 'POST':
#         pass
#     else:
#         return

if __name__ == "__main__":
    app.run(port=6000, debug=False)