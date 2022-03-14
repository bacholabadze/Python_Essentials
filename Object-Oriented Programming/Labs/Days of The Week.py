class WeekDayError(Exception):
    """Exception raised when wrong type of weekday is an input.

      Attributes:
          message -- explanation of the error
    """

    def __init__(self, message="Wrong Type of Weekday, try something like 'Mon' or 'Tue' ..."):
        self.message = message
        super().__init__(self.message)


class Weeker:
    week_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day: str):
        if day not in Weeker.week_days:
            raise WeekDayError
        else:
            self.__day = day

    def __str__(self):
        return self.__day

    def add_days(self, n):
        self.__day = Weeker.week_days[(Weeker.week_days.index(self.__day) + n) % 7]

    def subtract_days(self, n):
        # print(f'Cur Week Day Index = {Weeker.week_days.index(self.__day)}')
        self.__day = Weeker.week_days[(Weeker.week_days.index(self.__day) - n) % 7]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")

# Note : Expected Result on Edube page is wrong. 15 days after Monday is Tuesday, not Thursday :)
