from login_new_user import generating_user, generating_new_graph, generating_a_pixel
from datetime import date
from managing_graph import ManagingData

USER_NAME = "viviane69"
USER_TOKEN = "duiashdiuashduis"
GRAPH_ID = 'cyclingcycle69'
GRAPH_NAME = 'CyclingCycle'
# First part is made in a simple way, updating later already has integrated class and other calls,
# all for learning experience of both ways

# Call the first time to create from scratch
# user_data = generating_user(user_name=user_name, token=user_token)
# new_graph = generating_new_graph(username=user_name, token=user_token, graph_name=graph_name, graph_id=graph_id)

def add():
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

        current_date = date.today().strftime("%Y%m%d")
    else:
        year = input("Please write the year. ")
        month = check_month(input("Please write the month. "))
        day = check_day(input("Please write the day. "))
        current_date = f"{year}{month}{day}"
    print(current_date)

    amount = input("Please write the kilometers cycled.")

    generating_a_pixel(username=USER_NAME, token=USER_TOKEN, graph_id=GRAPH_ID, date=current_date, quantity=amount)


def update():
    # Calling and changing for a class for learning experience
    update_request = ManagingData(USER_NAME=USER_NAME, USER_TOKEN=USER_TOKEN, GRAPH_ID=GRAPH_ID)
    update_request.updating_graph()



initial_choice = input("Choose a option:\n1.Add\n2.Update\n3.Delete\n").lower()
if initial_choice == "1" or initial_choice == "add":
    add()
if initial_choice == "2" or initial_choice == "update":
    update()
if initial_choice == "3" or initial_choice == "delete":
    managing_data = ManagingData(USER_NAME=USER_NAME, USER_TOKEN=USER_TOKEN, GRAPH_ID=GRAPH_ID)
    managing_data.delete_graph()