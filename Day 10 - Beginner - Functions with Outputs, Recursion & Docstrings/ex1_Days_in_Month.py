# Day 10 - Exercise 1 - Expanding leap year program from day 3 Exercise 3 - Leap Year:
def is_leap(year):
    """Returns True if its a leap year, otherwise returns False"""
    is_leap = True
    if (year % 4 == 0):
        if year % 100 == 0:

            if year % 400 != 0:
                is_leap = False
    else:
        is_leap = False
    
    return is_leap

def days_in_month(year, month):
    """Calculates how many days in requested month. It also takes leap years into account."""
    if is_leap(year) and month == 2:
        return 29

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    return (month_days[month-1])
  
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
