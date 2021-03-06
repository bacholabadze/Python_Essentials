""" Estimated time
30-60 minutes

Level of difficulty
Easy

Objectives
Improving the student's skills in using the Calendar class.
Scenario
During this course, we looked at the Calendar class a bit. Your task is to extend its functionality with a new method
called count_weekday_in_year, which takes a year and a weekday as parameters, and then returns the number of
occurrences of a specific weekday in the year.

Use the following tips:

Create a class called MyCalendar that extends the Calendar class;
create the count_weekday_in_year method with the year and weekday parameters. The weekday parameter should be a
value between 0-6, where 0 is Monday and 6 is Sunday. The method should return the number of days as an integer;
in your implementation, use the monthdays2calendar method of the Calendar class.
The following are the expected results:

Sample arguments

year=2019, weekday=0

Expected output

52


Sample arguments

year=2000, weekday=6

Expected output

53 """

from calendar import Calendar


class MyCalendar(Calendar):
    def __init__(self):
        super().__init__()

    def count_weekday_in_year(self, year, weekday):
        if 0 > weekday > 6:
            raise ValueError
        c = Calendar()
        count = 0
        for month_ix in range(1, 13):
            for week in c.monthdays2calendar(year, month_ix):
                if week[weekday][0] != 0:
                    count += 1
        print(count)
        return count


myc = MyCalendar()
myc.count_weekday_in_year(2000, 6)
