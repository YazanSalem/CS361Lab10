from django.test import TestCase, Client
from TAScheduler.models import *


class TestCreateLab(TestCase):
    dummyClient = None
    TA = None
    instructor = None
    admin = None
    course = None
    lab = None

    def setUp(self):
        self.dummyClient = Client()
        self.TA = UserProfile.objects.create(userID=1, userType="TA", username="TA1"
                                             , password="TA123", name="TA Dummy", address="TA Address",
                                             phone=3234457876, email="TAEmail@email.com")

        self.instructor = UserProfile.objects.create(userID=2, userType="INSTRUCTOR", username="Instructor1"
                                                     , password="Instructor123", name="Instructor Dummy",
                                                     address="Instructor Address", phone=3234457176,
                                                     email="InstructorEmail@email.com")

        self.admin = UserProfile.objects.create(userID=3, userType="SUPERVISOR", username="Admin1"
                                                , password="Admin123", name="Admin Dummy", address="Admin Address",
                                                phone=3234452176, email="AdminEmail@email.com")

        self.course = Course.objects.create(courseID=1, name="Software Engineering",
                                            location="EMS 180", hours="12:00PM - 01:00PM", days="M, W",
                                            instructor=self.instructor)
        self.course.TAs.add(self.TA)
        # self.lab = Lab.objects.create(labID=1, name="Lab", location="EMS 280",
        #                               hours="03:00PM - 04:00PM", days="M, W", course=self.course, TA=self.TA)

        self.dummyClient.post("/", {"useraccount": self.admin.username, "password": self.admin.password})

    def createLab(self):
        r = self.dummyClient.post('/create_lab/', {"labID": 1, "name": "Lab", "location": "EMS 280",
                                                   "hours": "03:00PM - 04:00PM", "days": "M, W",
                                                   "course": self.course, "TA": self.TA})
        self.assertEqual(Course.objects.get(labID=1).name, "Lab", "Lab was created successfully")
