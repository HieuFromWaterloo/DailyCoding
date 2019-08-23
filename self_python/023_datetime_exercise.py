import datetime
from datetime import timedelta
import calendar

"""
Calculate Number of Days, Weeks, or Months to Reach Specific Goals

Pay off credit card while interest rate is going up
"""

balance = 5000
interest = 13 * 0.01
monthly_payment = 1000

today = datetime.date.today()  # 2019-08-23
# print(today.day) # 23
# print(today.year) # 23
# print(today.month)  # 23


# how do we know which date are we in (mon, tues, wed, etc) and how many days in a given month?
day_in_current_month = calendar.monthrange(today.year, today.month)[1]  # get num days in a month
# print(calendar.monthrange(today.year, today.month))
"""
returns (3, 31) equivalent to:
- the first date of the month (3:Thurs)
- number of days in the month: 31 days in August
"""

# ====
"""
Next, the idea is to try to make the payment at the beginning of every month
"""

# we need to calculate how many day left in a month
day_till_end_month = day_in_current_month - today.day
# print(day_till_end_month)  # 8 days left in this month
# print(type(day_till_end_month))  # int

# we wanna ensure that the date we make the payment is 1st day of every month
start_date = today + timedelta(days=day_till_end_month + 1)
# print(start_date) # 2019-09-01

# ====
# Now we start paying off the balance

end_date = start_date

while balance > 0:
    print("\nStart Making Payments...")
    interest_charge = balance * (interest / 12)
    balance += interest_charge
    balance -= monthly_payment

    # rounding
    balance = round(balance, 2)
    if balance < 0:
        balance = 0

    print(end_date, balance)

    # get num of days in month after the payment
    day_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
    # since we're already in the 1st of the month, no need to add 1 to day_in_current_month
    end_date = end_date + timedelta(days=day_in_current_month)

# Number of days
print(end_date - start_date)  # it takes 91 days to pay off the debt
# print(type(end_date - start_date)) # <type 'datetime.timedelta'>

# Print numbers of weeks
print((end_date - start_date).days // 7)  # it takes 13 weeks
