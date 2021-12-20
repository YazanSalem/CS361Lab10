from django.test import TestCase, Client
from TAScheduler.models import *
from TAScheduler.Management.UserManagement import UserManagement


class TestCreateUser(TestCase):
    def setUp(self):
        self.admin = UserProfile.objects.create(userID=1, userType="SUPERVISOR", username="admin",
                                                password="admin", name="Admin", address="address",
                                                phone=1234567890, email="a@a.com")
        self.client = Client()
        self.client.post("/", {"useraccount": self.admin.username, "password": self.admin.password})

    def test_createSupervisor(self):
        r = self.client.post("/create_user/",
                             {"userID": 2, "userType": "SUPERVISOR", "username": "supervisorTest",
                              "password": "supervisorTest",
                              "name": "Test Supervisor", "address": "address",
                              "phone": 1234567891,
                              "email": "s@s.com"}, follow=True)

        self.assertEqual(UserProfile.objects.get(userID=2).userType, "SUPERVISOR",
                         "Supervisor was created successfully")

    def test_createInstructor(self):
        r = self.client.post("/create_user/",
                             {"userID": 3, "userType": "INSTRUCTOR", "username": "InstructorTest",
                              "password": "InstructorTest",
                              "name": "Test Instructor", "address": "address",
                              "phone": 1234567891,
                              "email": "i@i.com"}, follow=True)

        self.assertEqual(UserProfile.objects.get(userID=3).userType, "INSTRUCTOR",
                         "INSTRUCTOR was created successfully")

    def test_createTA(self):
        r = self.client.post("/create_user/",
                             {"userID": 4, "userType": "TA", "username": "taTest",
                              "password": "taTest",
                              "name": "Test Ta", "address": "address",
                              "phone": 1234567891,
                              "email": "t@t.com"}, follow=True)

        self.assertEqual(UserProfile.objects.get(userID=4).userType, "TA", "TA was created successfully")
