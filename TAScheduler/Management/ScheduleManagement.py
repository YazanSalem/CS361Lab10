from typing import Type
from TAScheduler.models import *


class ScheduleManagement(object):

    def __init__(self, username):
        self.user = UserProfile.objects.get(username = username)

    def addToSchedule(self,name,days,hours,location):
        ScheduleManagement.inputErrorChecker(user = self.user, name =name, location = location,  days = days, hours = hours)
        Schedule.objects.create(user = self.user, name = name, days = days, hours = hours, location = location )

    def getSchedule(self):
        if(self.user.userType == "INSTRUCTOR"):
            UserSchedule = Course.objects.filter(instructor = self.user)
        else:
            UserSchedule = Lab.objects.filter(TA = self.user)

        for scheduleItem in UserSchedule:
            ScheduleManagement.addToSchedule(self, scheduleItem.name, scheduleItem.days, scheduleItem.hours, scheduleItem.location)

    def inputErrorChecker(user = None, name="", location="", days="", hours=""):
        if not (user is None):
            if not(isinstance(user, UserProfile)):
                raise TypeError("Schedule's user is not of type UserProfile")
            if user.userType == "SUPERVISOR":
                raise TypeError("Supervisors do not have schedules")
        if not (isinstance(name, str)):
            raise TypeError("Schedule course/lab name entered is not of type str")
        if not (isinstance(location, str)):
            raise TypeError("Schedule course/lab location entered is not of type str")
        if not (isinstance(days, str)):
            raise TypeError("Schedule course/lab days entered is not of type str")
        if not (isinstance(hours, str)):
            raise TypeError("Schedule course/lab hours entered is not of type str")
