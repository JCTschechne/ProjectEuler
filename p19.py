problem = """
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""


def is_leap(year):
    return year % 4 == 0 and not (year % 100 == 0 and not year % 400 == 0)


def next_day(year, month, day):
    days_in_month = 0
    day += 1
    match month:
        case 8 | 3 | 5 | 10:  # september, april, june, november 30 days
            days_in_month = 30
        case 0 | 2 | 4 | 6 | 7 | 9 | 11:  # rest 31 days
            days_in_month = 31
        case 1:  # except February
            if is_leap(year):
                days_in_month = 29
            else:
                days_in_month = 28
        case _:
            raise Exception
    if day >= days_in_month:
        day = 0
        if month == 11:
            month = 0
            year += 1
        else:
            month += 1
    return year, month, day


def solve():
    # start at the 1 Jan 1901
    year = 1901
    month = 0
    day = 0
    # first day in 1901 was a thursday
    weekday = 1

    count = 0

    # break once we reach the 21th century
    while year != 2001:
        if weekday == 6 and day == 0:
            count += 1
        year, month, day = next_day(year, month, day)
        weekday = (weekday + 1) % 7
        # print(year, month, day ,weekday)
    return count


if __name__ == "__main__":
    print(problem, "\nSolution: ", solve())
