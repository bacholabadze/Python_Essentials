def formatTimeString(time):
    return str(time).zfill(2)


class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = formatTimeString(hours)
        self.__minutes = formatTimeString(minutes)
        self.__seconds = formatTimeString(seconds)

    def __str__(self):
        return f"{self.__hours}:{self.__minutes}:{self.__seconds}"

    def next_second(self):
        self.__seconds = formatTimeString(int(self.__seconds) + 1)
        if self.__seconds == '60':  # If seconds value reach maximum value
            self.__seconds = '00'  # Reset seconds indicator
            self.__minutes = formatTimeString(int(self.__minutes) + 1)  # Increase minutes indicator
            if self.__minutes == '60':  # If minutes value reach maximum value
                self.__minutes = '00'  # Reset minutes indicator
                self.__hours = formatTimeString(int(self.__hours) + 1)  # Increase hours indicator
                if self.__hours == '24':
                    self.__hours = '00'

    def prev_second(self):
        self.__seconds = formatTimeString(int(self.__seconds) - 1)
        if self.__seconds == '-1':  # If seconds indicator is less than minimum value
            self.__seconds = '59'  # set seconds indicator to proper value
            self.__minutes = formatTimeString(int(self.__minutes) - 1)  # Decrease minutes indicator
            if self.__minutes == '-1':  # if minutes indicator is less than minimum value (0)
                self.__minutes = '59'  # set minutes indicator to proper value
                self.__hours = formatTimeString(int(self.__hours) - 1)  # Decrease the hours indicator
                if self.__hours == '-1':  # If hours indicator is less than minimum value
                    self.__hours = '23'  # Set hours indicator value to proper value


timer = Timer(22, 58, 59)
print(timer)

timer.next_second()
print(timer)

timer.prev_second()
print(timer)
