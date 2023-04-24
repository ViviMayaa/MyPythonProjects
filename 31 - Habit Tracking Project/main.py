from login_new_user import generating_user, generating_new_graph, generating_a_pixel
from datetime import date

user_name = "viviane69"
user_token = "duiashdiuashduis"
graph_id = 'cyclingcycle69'
graph_name = 'CyclingCycle'


# Call the first time to create from scratch
# user_data = generating_user(user_name=user_name, token=user_token)
# new_graph = generating_new_graph(username=user_name, token=user_token, graph_name=graph_name, graph_id=graph_id)

# Adding information to the table
def check_month(month_check):
    if len(str(month_check)) == 1:
        return f"0{month_check}"
    else:
        return month_check


def check_day(day_check):
    if len(str(day_check)) == 1:
        return f"0{day_check}"
    else:
        return day_check


date_today = input("Do you want to add for today? ").lower()
if date_today == "yes" or date_today == "y":
    # date_not_formatted = (date.today())
    # year = date_not_formatted.year
    # month = check_month(date_not_formatted.month)
    # day = check_day(date_not_formatted.day)
    date = date.today().strftime("%Y%m%d")

else:
    year = input("Please write the year. ")
    month = check_month(input("Please write the month. "))
    day = check_day(input("Please write the day. "))
    date = f"{year}{month}{day}"
print(date)

amount = input("Right the amount cycled in kilometers ")

generating_a_pixel(username=user_name, token=user_token, graph_id=graph_id, date=date, quantity=amount)
