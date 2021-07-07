from flask import Flask

# instantiate Flask instance
app = Flask(__name__)

# Set some important evn variables: (windows: set = linux: export)
# set FLASK_APP=flaskblog.py
# set FLASK_DEBUG=1

# use route to route to different pages

# we can also use multi routes as follow


@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"


@app.route("/about")
def about():
    return "<h1>About Page</h1>"


if __name__  '__main__':
    # do this so we can eitther:
    # `flask run` OR `python flaskblog.py`
    app.run(debug=True)
