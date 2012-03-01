"""
A simple Flask application
http://flask.pocoo.org/docs/quickstart/
"""
from flask import *
app = Flask(__name__)

class Person(object):
    def __init__(self, username, firstname, lastname):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname

@app.route("/")
def index():
    return 'Hello World!'

@app.route("/<username>/<firstname>/<lastname>")
def profile(username, firstname, lastname):
    person = Person(username, firstname, lastname)
    return render_template('profile.html', person=person)

if __name__ == "__main__":
    app.debug = True
    app.run()
