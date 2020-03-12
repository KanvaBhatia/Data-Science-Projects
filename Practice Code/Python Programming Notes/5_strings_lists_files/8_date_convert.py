"""
    # 8_date_convert.py
    # Converts a date in form "mm./dd/yyyy" to "month day, year"
    Created by: temikelani on: 1/28/20
"""


# d
#
def main():
    # get the date
    dateStr = input("Enter a date (mm/dd/yyyy) : ")

    # split into components
    monthStr, day, year = dateStr.split("/")

    # convert monthStr to the month name
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
              "October", "November", "December"]

    monthStr = months[int(monthStr) - 1]

    # output result in month day, year format
    print("The converted date is:", monthStr, day + ",", year)


main()
