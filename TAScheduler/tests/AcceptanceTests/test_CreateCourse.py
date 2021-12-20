from django.test import TestCase, Client
from TAScheduler.models import *


class TestCreateCourse(TestCase):
    dummyClient = None
    TA = None
    instructor = None
    admin = None
    course = None

    def setUp(self):
        self.dummyClient = Client()
        self.TA = UserProfile.objects.create(userID=1, userTyoe="TA", username="TA1"
                                             , password="TA123", name="TA Dummy", address="TA Address",
                                             phone=3234457876, email="TAEmail@email.com")

        self.instructor = UserProfile.objects.create(userID=2, userTyoe="INSTRUCTOR", username="Instructor1"
                                                     , password="Instructor123", name="Instructor Dummy",
                                                     address="Instructor Address", phone=3234457176,
                                                     email="InstructorEmail@email.com")

        self.admin = UserProfile.objects.create(userID=3, userTyoe="SUPERVISOR", username="Admin1"
                                                , password="Admin123", name="Admin Dummy", address="Admin Address",
                                                phone=3234452176, email="AdminEmail@email.com")
        self.dummyClient.post("/", {"useraccount": self.admin.username, "password": self.admin.password})

    def createCourse(self):
        r = self.dummyClient.post('/create_course/', {"courseID": 1, "name": "Software Engineering",
                                                      "location": "EMS 180", "hours": "12:00PM - 01:00PM",
                                                      "days": "M, W", "instructor": self.instructor})

        self.assertEqual(Course.objects.get(courseID=1).name, "Software Engineering", "Course was created successfully")

    def createCourse2(self):
        r = self.dummyClient.post('/create_course/', {"courseID": 2, "name": "Systems Programming",
                                                      "location": "EMS 180", "hours": "12:00PM - 01:00PM",
                                                      "days": "M, W", "instructor": self.instructor})

        self.assertEqual(Course.objects.get(courseID=2).name, "Systems Programming", "Course was created successfully")
        course = Course.objects.get(courseID=2)
        course.TAs.add(self.TA)
        course.save()
        self.assertEqual(Course.objects.get(courseID=2).TAs[0], self.TA)
