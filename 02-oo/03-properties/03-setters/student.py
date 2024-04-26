class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours
    
    @property
    def minutes(self):
        return self.__minutes
    
    @property
    def seconds(self):
        return self.__seconds
    
    @hours.setter
    def hours(self, value1):
        if value1 < 0 or value1 > 23:
            raise ValueError
        else:
            self.__hours = value1

    @minutes.setter
    def minutes(self, value2):
        if value2 < 0 or value2 > 59:
            raise ValueError
        else:
            self.__minutes = value2
    
    @seconds.setter
    def seconds(self, value3):
        if value3 < 0 or value3 > 59:
            raise ValueError
        else:
            self.__seconds = value3

    