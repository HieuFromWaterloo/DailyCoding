from flask import Flask, render_template, url_for, flash, redirect
# import the FORMS that we created in forms.py
# we need to create some routes for these forms
from forms import RegistrationForm, LoginForm

"""
Note:

- When using these forms, we need to a `secret key` for our application. This prevent cookies modification and cross-site request forgery attacks
    - ADD THIS KEY TO `flaskblog.py`

- ideally, we want our secret key to be randomized chars. Done using python:
    import secrets
    # gen 16 random chars
    secrets.token_hex(16) # ==> 5791628bb0b13ce0c676dfde280ba245
"""

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

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
    # title = name of the tab
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


"""
For each newly create route, we also need to create their corresponding templates to be rendered
"""


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    # form.validate_on_submit()
    # this will validate the form when it is submitted
    # before redering back to the register route
    if form.validate_on_submit():
        # flash(<alert_str>, category_of_alert) is an ez way to send 1 time alert
        # 'success' = style of alert
        """
        NOTE:
        - we need to update this flash format in the `layout.html` so that it can display the alrt
        """
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # below is dummy variable to simulate shit
        if form.email.data == 'hnguyen@blocklabs.ca' and form.password.data == 'asdfasdfsdrfgjksdhfgkl':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
