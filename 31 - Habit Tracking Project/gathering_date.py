from datetime import date

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

def question_date():
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
    return current_date


def question_kilom():
    return input("Please write the kilometers cycled.")