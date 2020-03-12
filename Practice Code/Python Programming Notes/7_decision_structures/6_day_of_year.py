"""
    # 6_day_of_year.py
    # Program determine if a date is valid and then tells what day on the year it is from (1 - 365/366)
    Created by: temikelani on: 2/3/20
"""


# program check if month(1-12) and date(1-29/30/31) entered are valid. and returns valid month and date
def valid_date(month, day, year):
    if 1 <= month <= 12:
        if month == 2:
            # check for leap year
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                if 1 <= day <= 29:
                    return month, day
                else:
                    print("day is invalid")
            else:
                if 1 <= day <= 28:
                    return month, day
                else:
                    print("day is invalid")
        elif month == 4 or month == 6 or month == 9 or month == 11:
            if 1 <= day <= 30:
                return month, day
        else:
            if 1 <= day <= 29:
                return month, day
    else:
        print("invalid month")


def day_of_year(month, day, year):
    day_number = 31 * (month - 1) + day
    if month <= 2:
        return day_number
    # if the year is a leap year and after Feb 29
    elif month > 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        return day_number - ((4 * month + 23) // 10) + 1
    # after February
    else:
        if month > 2:
            return day_number - ((4 * month + 23) // 10)


def main():
    print("this program tells you the number of a day in a year from 1-365\n")
    date = input("Enter date in mm/dd/yyyy format, separated by '/': ")
    month, day, year = date.split("/")

    # month and day after validation
    v_month, v_day = valid_date(int(month), int(day), int(year))

    # obtain day of year
    print(date + " is the", day_of_year(v_month, v_day, int(year)), "day of that year")


main()