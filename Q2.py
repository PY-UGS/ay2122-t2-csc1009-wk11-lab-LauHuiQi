from audioop import mul
from lib2to3.pgen2.token import MINUS


class clockTime:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds  = seconds

    ## setter for hours
    def setHours(self, hours):
        self.hours = hours  

    ## setter for minutes
    def setMinutes(self, minutes):
        self.minutes = minutes

    ## setter for seconds
    def setSeconds(self, seconds):
        self.seconds = seconds

    ## to print time
    def showTime(self):
        print(self.hours + ':' + self.minutes + ':' + self.seconds)

clock = clockTime()
print("Enter the hours: ")
clock.setHours(input())
print("Enter the minutes: ")
clock.setMinutes(input())
print("Enter the seconds: ")
clock.setSeconds(input())

print("\nThe new time is:")
clock.showTime()