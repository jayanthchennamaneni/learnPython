class Clock(object):
    """
    A class representing a simple clock with hours, minutes, and seconds.
    """

    def __init__(self, hour, minute, second):
        """
        Initializes a Clock instance with the provided hour, minute, and second.
        """
        self.set_clock(hour, minute, second)

    def set_clock(self, hour, minute, second):
        """
        Sets the clock with the provided hour, minute, and second.
        """
        if isinstance(hour, int) and 0 <= hour < 24:
            self.__hour = hour
        else:
            raise ValueError("Hours have to be integers between 0 and 23")

        if isinstance(minute, int) and 0 <= minute < 60:
            self.__minute = minute
        else:
            raise ValueError("Minutes have to be integers between 0 and 59")

        if isinstance(second, int) and 0 <= second < 60:
            self.__second = second
        else:
            raise ValueError("Seconds have to be integers between 0 and 59")

    def tick(self):
        """
        Simulates the ticking of the clock, updating the time accordingly.
        """
        if self.__second == 59:
            self.__second = 0
            if self.__minute == 59:
                self.__minute = 0
                if self.__hour == 23:
                    self.__hour = 0
                else:
                    self.__hour += 1
            else:
                self.__minute += 1
        else:
            self.__second += 1
    
    def __str__(self):
        """
        Returns the string representation of the time in the format "HH:MM:SS".
        """
        return f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}"
    
if __name__ == "__main__":
    x = Clock(0, 59, 59)
    print(x)
    x.tick()
    print(x)

