from django.test import TestCase, Client
from TAScheduler.models import *
from TAScheduler.Management.UserManagement import UserManagement


class test_editSupervisor(TestCase):
    def setUp(self):
        self.client = Client()
        self.testSupervisor = UserProfile.objects.create(userID=1, userType="SUPERVISOR", username="Tester",
                                                         password="test", name="tester", address="test",
                                                         phone=1234567890, email="test@test.com")
        print(self.testSupervisor)
        self.userToEdit = UserProfile.objects.create(userID=2, userType="SUPERVISOR", username="supervisor1",
                                                     password="password", name="Ted Supervisor",
                                                     address="345 Street Street", phone=1234567890,
                                                     email="email@email.com")
        r = self.client.post("/edit_user/", {"edit": self.userToEdit.userID}, follow=True)

    def test_editUsertype(self):
        self.client.post("/edit_user/",
                         {"type": "INSTRUCTOR", "username": self.userToEdit.username, "name": self.userToEdit.name,
                          "address": self.userToEdit.address, "phone": self.userToEdit.phone,
                          "email": self.userToEdit.email, "submit": self.userToEdit.userID}, follow=True)
        self.assertEqual(UserProfile.objects.get(userID=2).userType, "INSTRUCTOR",
                         "Edit User did not set userType correctly")

    def test_editUsername(self):
        self.client.post("/edit_user/",
                         {"type": self.userToEdit.userType, "username": "new username", "name": self.userToEdit.name,
                          "address": self.userToEdit.address, "phone": self.userToEdit.phone,
                          "email": self.userToEdit.email, "submit": self.userToEdit.userID}, follow=True)
        self.assertEqual(UserProfile.objects.get(userID=2).username, "new username",
                         "Edit dser did not set username correctly")

    def test_editBlankUsername(self):
        resp = self.client.post("/edit_user/",
                                {"type": self.userToEdit.userType, "username": "", "name": self.userToEdit.name,
                                 "address": self.userToEdit.address, "phone": self.userToEdit.phone,
                                 "email": self.userToEdit.email, "submit": self.userToEdit.userID}, follow=True)
        self.assertEqual(resp.context["error"], "User was not changed. Username should not be left blank",
                         "An error message was not displayed when username was left blank")

    def test_editName(self):
        self.client.post("/edit_user/",
                         {"type": self.userToEdit.userType, "username": self.userToEdit.username, "name": "new name",
                          "address": self.userToEdit.address, "phone": self.userToEdit.phone,
                          "email": self.userToEdit.email, "submit": self.userToEdit.userID}, follow=True)
        self.assertEqual(UserProfile.objects.get(userID=2).name, "new name", "Edit User did not set name correctly")

    def test_editBlankName(self):
        self.client.post("/edit_user/",
                         {"type": self.userToEdit.userType, "username": self.userToEdit.username, "name": "new name",
                          "address": self.userToEdit.address, "phone": self.userToEdit.phone,
                          "email": self.userToEdit.email, "submit": self.userToEdit.userID}, follow=True)
        self.assertEqual(UserProfile.objects.get(userID=2).name, "new name", "Edit User did not set name correctly")

    def test_editAddress(self):
        self.client.post("/edit_user/",
                         {"type": self.userToEdit.userType, "username": self.userToEdit.username,
                          "name": self.userToEdit.name,
                          "address": "new address", "phone": self.userToEdit.phone,
                          "email": self.userToEdit.email, "submit": self.userToEdit.userID}, follow=True)
        self.assertEqual(UserProfile.objects.get(userID=2).address, "new address",
                         "Edit User did not set address correctly")

    def test_editPhone(self):
        self.client.post("/edit_user/",
                         {"type": self.userToEdit.userType, "username": self.userToEdit.username,
                          "name": self.userToEdit.name,
                          "address": self.userToEdit.address, "phone": 9876543212,
                          "email": self.userToEdit.email, "submit": self.userToEdit.userID}, follow=True)
        self.assertEqual(UserProfile.objects.get(userID=2).phone, 9876543212, "Edit User did not set phone correctly")

    def test_editEmail(self):
        self.client.post("/edit_user/",
                         {"type": self.userToEdit.userType, "username": self.userToEdit.username,
                          "name": self.userToEdit.name,
                          "address": self.userToEdit.address, "phone": self.userToEdit.phone,
                          "email": "newemail@newemail.com", "submit": self.userToEdit.userID}, follow=True)
        self.assertEqual(UserProfile.objects.get(userID=2).email, "newemail@newemail.com",
                         "Edit User did not set email correctly")

    def test_editEmail(self):
        self.client.post("/edit_user/",
                         {"type": self.userToEdit.userType, "username": self.userToEdit.username,
                          "name": self.userToEdit.name,
                          "address": self.userToEdit.address, "phone": self.userToEdit.phone,
                          "email": "newemail@newemail.com", "submit": self.userToEdit.userID}, follow=True)
        self.assertEqual(UserProfile.objects.get(userID=2).email, "newemail@newemail.com",
                         "Edit User did not set email correctly")
