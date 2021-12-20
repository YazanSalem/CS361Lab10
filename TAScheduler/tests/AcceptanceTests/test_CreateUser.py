from django.test import TestCase, Client
from TAScheduler.models import *
from TAScheduler.Management.UserManagement import UserManagement


class TestCreate(TestCase):
    def setUp(self):
        self.admin = UserProfile.objects.create(userID=1, userType="SUPERVISOR", username="admin",
                                                password="admin", name="Admin", address="address",
                                                phone=1234567890, email="a@a.com")
        self.client = Client()
        print(self.testSupervisor)
        r = self.client.post("/create_user/", {"edit": self.userToEdit.userID}, follow=True)

    def test_create(self):
        self.client.post("/create_user/",
                         {"user_id": 2, "user_type": "SUPERVISOR", "username": "supervisorTest",
                          "password": "supervisorTest",
                          "name": "Test Supervisor", "address": "address",
                          "phone": 1234567891,
                          "email": "s@s.com"}, follow=True)

        self.assertEqual(UserProfile.objects.get(userID=2).userType, "INSTRUCTOR",
                         "Edit User did not set userType correctly")
