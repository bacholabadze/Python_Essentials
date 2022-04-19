""" Introduction to the calendar module """

""" In addition to the datetime and time modules, the Python standard library provides a module called calendar which, 
    as the name suggests, offers calendar-related functions."""

""" It's important that the days of the week are displayed from Monday to Sunday, and each day of the week has its 
    representation in the form of an integer:

Day of the week	  Integer value	  Constant
Monday	          0	              calendar.MONDAY
Tuesday	          1	              calendar.TUESDAY
Wednesday	      2	              calendar.WEDNESDAY
Thursday	      3	              calendar.THURSDAY
Friday	          4	              calendar.FRIDAY
Saturday	      5	              calendar.SATURDAY
Sunday	          6	              calendar.SUNDAY """

# For months, integer values are indexed from 1, i.e., January is represented by 1, and December by 12.
# Unfortunately, there aren't constants that express the months.

# ---------------------------------------------- Your first calendar ---------------------------------------------------

print("Your first calendar".center(72, '-'))

""" You will start your adventure with the calendar module with a simple function called calendar, 
    which allows you to display the calendar for the whole year. Let's look at how to use it to 
    display the calendar for 2022."""

import calendar
print(calendar.calendar(2022))

""" The result displayed is similar to the result of the cal command available in Unix. 
    If you want to change the default calendar formatting, you can use the following parameters:

        w – date column width (default 2)
        l – number of lines per week (default 1)
        c – number of spaces between month columns (default 6)
        m – number of columns (default 3)   """


""" A good alternative to the above function is the function called prcal, which also takes the same 
    parameters as the calendar function, but doesn't require the use of the print function to display 
    the calendar. Its use looks like this:"""

print("calendar.prcal".center(72, '_'))

import calendar
calendar.prcal(2022)

# ---------------------------------------------------------------------------------------------------------------------


# ----------------------------------------- Calendar for a specific month ----------------------------------------------

print("Calendar for a specific month".center(72, '-'))

""" The calendar module has a function called month, which allows you to display a calendar for a specific month. 
Its use is really simple, you just need to specify the year and month """

import calendar
print(calendar.month(2022, 8))

""" you can change the default formatting using the following parameters:

        w – date column width (default 2)
        l – number of lines per week (default 1)    """


# Note: You can also use the prmonth function, which has the same parameters as the month function,
# but doesn't require you to use the print function to display the calendar.

# ---------------------------------------------------------------------------------------------------------------------


# ----------------------------------------- The setfirstweekday() function ---------------------------------------------

print("The setfirstweekday() function".center(72, '-'))

""" As you already know, by default in the calendar module, the first day of the week is Monday. 
    However, you can change this behavior using a function called setfirstweekday."""

# setfirstweekday method requires a parameter expressing the day of the week in the form of an integer value

import calendar

calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2022, 12)

""" The example uses the calendar.SUNDAY constant, which contains a value of 6. Of course, 
    you could pass this value directly to the setfirstweekday function, 
    but the version with a constant is more elegant. """

# ---------------------------------------------------------------------------------------------------------------------


# --------------------------------------------- The weekday() function -------------------------------------------------

print("The weekday() function".center(72, '-'))

""" Another useful function provided by the calendar module is the function called weekday, 
    which returns the day of the week as an integer value for the given year, month, and day."""

import calendar
print(calendar.weekday(2022, 8, 18))  # The function returns 3, which means that August 18, 2022 is a Thursday.

# ---------------------------------------------------------------------------------------------------------------------


# -------------------------------------------- The weekheader() function -----------------------------------------------

print("The weekheader() function".center(72, '-'))

""" You've probably noticed that the calendar contains weekly headers in a shortened form. 
    If needed, you can get short weekday names using the weekheader method. """

""" The weekheader method requires you to specify the width in characters for one day of the week. 
    If the width you provide is greater than 3, you'll still get the abbreviated 
    weekday names consisting of three characters.   """

import calendar
print(calendar.weekheader(2))

# Note: If you change the first day of the week, e.g., using the setfirstweekday function,
# it'll affect the result of the weekheader function.

# ---------------------------------------------------------------------------------------------------------------------


# ------------------------------------ How do we check if a year is a leap year? ---------------------------------------

print("How do we check if a year is a leap year?".center(72, '-'))

# The calendar module provides two useful functions to check whether years are leap years.

""" The first one, called isleap, returns True if the passed year is leap, or False otherwise. 
    The second one, called leapdays, returns the number of leap years in the given range of years."""

import calendar

print(calendar.isleap(2020))
print(calendar.leapdays(2010, 2025))  # Up to but not including 2021.

# ---------------------------------------------------------------------------------------------------------------------


# ----------------------------------------- Classes for creating calendars --------------------------------------------


""" The presented functions aren't everything the calendar module offers. In addition to them, 
    we can use the following classes:
    
    calendar.Calendar – provides methods to prepare calendar data for formatting;
    
    calendar.TextCalendar – is used to create regular text calendars;
    
    calendar.HTMLCalendar – is used to create HTML calendars;
    
    calendar.LocalTextCalendar – is a subclass of the calendar.TextCalendar class. The constructor of this class takes 
    the locale parameter, which is used to return the appropriate months and weekday names.
    
    calendar.LocalHTMLCalendar – is a subclass of the calendar.HTMLCalendar class. The constructor of this class takes 
    the locale parameter, which is used to return the appropriate months and weekday names."""

# ---------------------------------------------------------------------------------------------------------------------


# -------------------------------------------- Creating a Calendar object ----------------------------------------------

print("Creating a Calendar object".center(72, '-'))

# The Calendar class constructor takes one optional parameter named firstweekday, by default equal to 0 (Monday).

# The firstweekday parameter must be an integer between 0-6.
# For this purpose, we can use the already-known constants

import calendar

c = calendar.Calendar(calendar.SUNDAY)

for weekday in c.iterweekdays():
    print(weekday, end=" ")

print()

# ---------------------------------------------------------------------------------------------------------------------


# -------------------------------------------- The itermonthdates() method ---------------------------------------------

print("The itermonthdates() method".center(72, '-'))

""" The Calendar class has several methods that return an iterator. One of them is the itermonthdates method, 
    which requires specifying the year and month.
    
    As a result, all days in the specified month and year are returned, as well as all days before the 
    beginning of the month or the end of the month that are necessary to get a complete week.

    Each day is represented by a datetime.date object."""

import calendar

c = calendar.Calendar()

for date in c.itermonthdates(2019, 11):
    print(date, end=" ")

""" The code displays all days in November 2019. Because the first day of November 2019 was a Friday, 
    the following days are also returned to get the complete week: 10/28/2019 (Monday) 
    10/29/2019 (Tuesday) 10/30/2019 (Wednesday) 10/31/2019 (Thursday).

    The last day of November 2019 was a Saturday, so in order to keep the complete week, 
    one more day is returned 12/01/2019 (Friday).   """

# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------- Other methods that return iterators -----------------------------------------

print("Other methods that return iterators".center(72, '-'))

""" Another useful method in the Calendar class is the method called itermonthdates, 
    which takes year and month as parameters, 
    and then returns the iterator to the days of the week represented by numbers."""

import calendar

c = calendar.Calendar()

for iter in c.itermonthdays(2019, 11):
    print(iter, end=" ")

print()
""" You’ll have certainly noticed the large number of 0s returned as a result of the example code. 
    These are days outside the specified month range that are added to keep the complete week. """

""" The first four zeros represent 10/28/2019 (Monday) 10/29/2019 (Tuesday) 10/30/2019 (Wednesday) 
    10/31/2019 (Thursday). The remaining numbers are days in the month, except the last value of 0, 
    which replaces the date 12/01/2019 (Sunday)."""


""" There are four other similar methods in the Calendar class that differ in data returned:

    itermonthdates2 – returns days in the form of tuples consisting of a day of the month number and a week day number;

    itermonthdates3 – returns days in the form of tuples consisting of a year, a month, and a day of the month numbers. 
    This method has been available since version 3.7;

    itermonthdates4 – returns days in the form of tuples consisting of a year, a month, a day of the month, and a day 
    of the week numbers. This method has been available since Python version 3.7.   """

# ---------------------------------------------------------------------------------------------------------------------


# ------------------------------------------ The monthdays2calendar() method -------------------------------------------

print("The monthdays2calendar() method".center(72, '-'))

""" The Calendar class has several other useful methods that you can learn more about in the documentation 
    (https://docs.python.org/3/library/calendar.html)."""


""" One of them is the monthdays2calendar method, which takes the year and month, and then returns a list of weeks in 
    a specific month. Each week is a tuple consisting of day numbers and weekday numbers. """

# Note that the days numbers outside the month are represented by 0,
# while the weekday numbers are a number from 0-6, where 0 is Monday and 6 is Sunday.

import calendar

c = calendar.Calendar()

for data in c.monthdays2calendar(2020, 12):
    print(data)

# ---------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------- Key takeaways ----------------------------------------------------

print("Key takeaways".center(72, '-'))

""" 1. In the calendar module, the days of the week are displayed from Monday to Sunday. 
    Each day of the week has its representation in the form of an integer, where the first day of the week (Monday) 
    is represented by the value 0, while the last day of the week (Sunday) is represented by the value 6. """


""" 2. To display a calendar for any year, call the calendar function with the year passed as its argument, e.g.: """

import calendar
print(calendar.calendar(2020))

# Note: A good alternative to the above function is the function called prcal, which also takes the same parameters
# as the calendar function, but doesn't require the use of the print function to display the calendar.


""" 3. To display a calendar for any month of the year, call the month function, passing year and month to it. """

import calendar
print(calendar.month(2020, 9))

# Note: You can also use the prmonth function, which has the same parameters as the month function,
# but doesn't require the use of the print function to display the calendar.


""" 4. The setfirstweekday function allows you to change the first day of the week. It takes a value from 0 to 6, 
    where 0 is Sunday and 6 is Saturday."""


""" 5. The result of the weekday function is a day of the week as an integer value for a given year, month, and day: """

import calendar
print(calendar.weekday(2020, 9, 29)) # This displays 1, which means Tuesday.


""" 6. The weekheader function returns the weekday names in a shortened form. The weekheader method requires you to 
    specify the width in characters for one day of the week. If the width you provide is greater than 3, you'll still 
    get the abbreviated weekday names consisting of only three characters. For example: """

import calendar
print(calendar.weekheader(2)) # This display: Mo Tu We Th Fr Sa Su


""" 7. A very useful function available in the calendar module is the function called isleap, which, as the name 
    suggests, allows you to check whether the year is a leap year or not:"""

import calendar
print(calendar.isleap(2020)) # This displays: True


""" 8. You can create a calendar object yourself using the Calendar class, which, when creating its object, 
    allows you to change the first day of the week with the optional firstweekday parameter, e.g.:"""

import calendar

c = calendar.Calendar(2)

for weekday in c.iterweekdays():
    print(weekday, end=" ")
# Result: 2 3 4 5 6 0 1

# The iterweekdays returns an iterator for weekday numbers. The first value returned is always equal to the
# value of the firstweekday property.

# ---------------------------------------------------------------------------------------------------------------------
