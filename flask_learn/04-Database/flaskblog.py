from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# below can be replace by a postgresql relative path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# the great thing about SQLAlchemy is that we can represent our data struct in a class (a model)
# It's a good practice to put all these db classes into a separate file ==> `PACKAGE STRUCTURE`


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # we are gonna hash these images file into 20 char string so they will be all unique
    # Since all users start with a default profile pic (default.jpg) so they wont be unique ==> `unique=False`
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    # ******** THIS IS WHERE WE CONSTRUCT RELATIONSHIP *********
    # this 1 author has 1+ posts but 1 post can only has 1 author
    # `backref` is like adding a col to this `User` database (but we dont see it?!)
    # moreover, when a post is create, we can use `backref` in the `posts` attribute to get
    # the author who created the post
    # lazy=True: 'SQLAlchemy' load the data in in 1 go
    # **NOTE**
    posts = db.relationship('Post', backref='author', lazy=True)

    # this is a function triggers when we do `print()` in python
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
"""
**NOTE**: in `User` class we reference the entire 'Post' class
    - posts = db.relationship('Post', backref='author', lazy=True)

but in the `Post` class, we only reference `user.id` as <table_name.column_name>
"""

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    # If no date time input was given, the default will be the current time `datetime.utcnow`
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    # ******** THIS IS WHERE WE CONSTRUCT RELATIONSHIP *********
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


posts = [
    {
        'author': 'Author 1',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2021'
    },
    {
        'author': 'Author 2',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2021'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
