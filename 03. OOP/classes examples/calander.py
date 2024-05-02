class Calendar(object):
    months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # Number of days in each month
    date_style = "British"  # Default date style

    @staticmethod
    def leap_year(year):
        """
        Checks if a given year is a leap year.
        """
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def __init__(self, day, month, year):
        """
        Initializes a Calendar instance with the provided day, month, and year.
        """
        self.set_calendar(day, month, year)

    def set_calendar(self, day, month, year):
        """
        Sets the calendar with the provided day, month, and year.
        """
        if isinstance(day, int) and isinstance(month, int) and isinstance(year, int):
            self.__days = day
            self.__months = month
            self.__years = year
        else:
            raise ValueError("day, month, year have to be integers")

    def __str__(self):
        """
        Returns the date in the specified date style.
        """
        if Calendar.date_style == "British":
            return f"{self.__days:02d}/{self.__months:02d}/{self.__years:4d}"
        else:
            return f"{self.__months:02d}/{self.__days:02d}/{self.__years:4d}"

    def advance(self):
        """
        Advances the date by one day, accounting for leap years.
        """
        max_days = Calendar.months[self.__months - 1]
        if self.__months == 2 and Calendar.leap_year(self.__years):
            max_days += 1
        if self.__days == max_days:
            self.__days = 1
            if self.__months == 12:
                self.__months = 1
                self.__years += 1
            else:
                self.__months += 1
        else:
            self.__days += 1


if __name__ == "__main__":
    x = Calendar(28, 2, 2012)
    print(x, end=" ")
    x.advance()
    print("after applying advance: ", x)
    print(f'It is a leap year')
    x = Calendar(28, 2, 2013)
    print(x, end=" ")
    x.advance()
    print("after applying advance: ", x)
    x = Calendar(28, 2, 2000)
    print(x, end=" ")
    x.advance()
    print("after applying advance: ", x)
    print(f'It is a leap year')
    print("Switching to American date style: ")
    Calendar.date_style = "American"
    print("after applying advance: ", x)
