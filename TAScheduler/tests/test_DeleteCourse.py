from django.test import TestCase, Client
from TAScheduler.models import *

# Delete Course Cases: Succesful Deletion, Cannot Delete a Course if Labs are attached to course

class SuccessfulDeleteCourse(TestCase):

    dummyClient= None
    TA = None
    instructor = None
    admin = None
    course = None

    def setUp(self):
        self.dummyClient = Client()
        self.TA = UserProfile.objects.create(userID = 1, userTyoe = "TA", username = "TA1"
        , password = "TA123", name = "TA Dummy", address = "TA Address", phone = 3234457876, email ="TAEmail@email.com")
        
        self.instructor = UserProfile.objects.create(userID = 2, userTyoe = "INSTRUCTOR", username = "Instructor1"
        , password = "Instructor123", name = "Instructor Dummy", address = "Instructor Address", phone = 3234457176, email ="InstructorEmail@email.com")

        self.admin = UserProfile.objects.create(userID = 3, userTyoe = "SUPERVISOR", username = "Admin1"
        , password = "Admin123", name = "Admin Dummy", address = "Admin Address", phone = 3234452176, email ="AdminEmail@email.com")

        self.course = Course.objects.create(courseID = 1, name = "Software Engineering",
        location="EMS 180", hours = "12:00PM - 01:00PM", days ="M, W", instructor = self.instructor,
         TAs = [self.TA])

    def test_deleteCourse(self):
        resp = self.dummyClient.post('/delete_course/', {'courseID' : 1}, follow= True)
        var = Course.objects.count()
        self.assertEquals(var, 0)
        allCourses = list(Course.objects.filter(courseID = 1))
        self.assertEquals(allCourses, [])

class DeleteCourseHasLab(TestCase):
    
    dummyClient= None
    TA = None
    instructor = None
    admin = None
    course = None
    lab = None

    def setUp(self):
        self.dummyClient = Client()
        self.TA = UserProfile.objects.create(userID = 1, userTyoe = "TA", username = "TA1"
        , password = "TA123", name = "TA Dummy", address = "TA Address", phone = 3234457876, email ="TAEmail@email.com")
        
        self.instructor = UserProfile.objects.create(userID = 2, userTyoe = "INSTRUCTOR", username = "Instructor1"
        , password = "Instructor123", name = "Instructor Dummy", address = "Instructor Address", phone = 3234457176, email ="InstructorEmail@email.com")

        self.admin = UserProfile.objects.create(userID = 3, userTyoe = "SUPERVISOR", username = "Admin1"
        , password = "Admin123", name = "Admin Dummy", address = "Admin Address", phone = 3234452176, email ="AdminEmail@email.com")

        self.course = Course.objects.create(courseID = 1, name = "Software Engineering",
        location="EMS 180", hours = "12:00PM - 01:00PM", days ="M, W", instructor = self.instructor,
         TAs = [self.TA])

        self.lab = Lab.objects.create(labID = 1, name = "Lab", location ="EMS 280",
            hours = "03:00PM - 04:00PM", days="M, W", course = self.course, TA = self.TA)
        
        def test_deleteCourseHasLab(self):
            pass