import re
# create a python file: config.py to store email & pw
import config
from robobrowser import RoboBrowser

br = RoboBrowser()
br.open("https://datacoup.com/signin")

# Note that this website only has 1 form, if there are more than 2 forms, specifies args
form = br.get_form()
form['email'] = "FILL_USERNAME_IN" # or config.DATACOUP_USERNAME
form['password'] = "FILL_PASSWORD_IN" # or config.DATACOUP_PW
br.submit_form(form)

# this retunrs the string of html of the page we're currently on
src = str(br.parsed())

start = '<li class="header-bal">Earned: '
end = '</li>'

result = re.search('%s(.*)%s' % (start, end), src).group(1)

print(result)
