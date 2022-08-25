# going to import app from __init__.py
from flaskapp import app

if __name__ == '__main__':
    app.run(debug=False)