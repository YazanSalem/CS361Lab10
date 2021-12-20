from django.test import TestCase, Client
from TAScheduler.Management.UserManagement import UserManagement
from TAScheduler.models import UserProfile


class TestViewLabs(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = UserProfile.objects.create(username='Samuel', password='Samuel12345')
        self.user2 = UserProfile.objects.create(username='John', password='John12345')

    # check to account settings
    def test_viewInstructorTA_to_accountsettings(self):
        response = self.client.post("/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/home/", msg="Valid login redirects to home")

        response = self.client.post("/account_settings/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/account_settings/", msg="Moves to account settings page")

    # check to home
    def test_view_InstructorTA_to_home(self):
        response = self.client.post("/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/home/", msg="Valid login redirects to home")

        response = self.client.post("/home/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/home", msg="Moves to account settings page")

        # check to logout
    def test_view_InstructorTA_to_logout(self):
        response = self.client.post("/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/home/", msg="Valid login redirects to home")

        response = self.client.post("/home/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/home/", msg="Moves to account settings page")


