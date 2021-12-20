from django.test import TestCase, Client
from TAScheduler.Management.UserManagement import UserManagement
from TAScheduler.models import UserProfile


class TestViewCourseInstructor(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = UserProfile.objects.create(name='Samuel', password='Samuel12345')
        self.user2 = UserProfile.objects.create(name='John', password='John12345')

    # check to account settings
    def test_viewInstructorTA_to_accountsettings(self):
        response = self.client.post("/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/home/", msg="Valid login redirects to home")

        response = self.client.post("account_settings/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/account_settings", msg="Moves to account settings page")

    # check to home
    def test_view_InstructorTA_to_home(self):
        response = self.client.post("/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/home/", msg="Valid login redirects to home")

        response = self.client.post("home/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/account_settings", msg="Moves to account settings page")

        # check to logout

    def test_view_InstructorTA_to_logout(self):
        response = self.client.post("/", {"useraccount": "Samuel", "password": "Samuel12345"})
        print()
        self.assertEqual(response.url, "/home/", msg="Valid login redirects to home")

        response = self.client.post("account_settings/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/account_settings", msg="Moves to account settings page")


class TestViewCourseSupervisor(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = UserProfile.objects.create(name='Samuel', password='Samuel12345')
        self.user2 = UserProfile.objects.create(name='John', password='John12345')

        # check for CreateUser

    def test_view_Supervisor_to_createUser(self):
        response = self.client.post("/", {"useraccount": "Samuel", "password": "Samuel12345"})
        print()
        self.assertEqual(response.url, "/home/", msg="Valid login redirects to home")

        response = self.client.post("account_settings/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/account_settings", msg="Moves to account settings page")

        # check for EditUser
        
    def test_view_Supervisor_to_editUser(self):
        response = self.client.post("/", {"useraccount": "Samuel", "password": "Samuel12345"})
        print()
        self.assertEqual(response.url, "/home/", msg="Valid login redirects to home")

        response = self.client.post("account_settings/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/account_settings", msg="Moves to account settings page")

        # check for deleteUser

    def test_view_Supervisor_to_deleteUser(self):
        response = self.client.post("/", {"useraccount": "Samuel", "password": "Samuel12345"})
        print()
        self.assertEqual(response.url, "/home/", msg="Valid login redirects to home")

        response = self.client.post("account_settings/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/account_settings", msg="Moves to account settings page")

        # check for account settings

    def test_view_Supervisor_to_accountsettings(self):
        response = self.client.post("/", {"useraccount": "Samuel", "password": "Samuel12345"})
        print()
        self.assertEqual(response.url, "/home/", msg="Valid login redirects to home")

        response = self.client.post("account_settings/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/account_settings", msg="Moves to account settings page")

        # check for home

    def test_view_Supervisor_to_home(self):
        response = self.client.post("/", {"useraccount": "Samuel", "password": "Samuel12345"})
        print()
        self.assertEqual(response.url, "/home/", msg="Valid login redirects to home")

        response = self.client.post("account_settings/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/account_settings", msg="Moves to account settings page")

        # check for logout

    def test_view_Supervisor_to_logout(self):
        response = self.client.post("/", {"useraccount": "Samuel", "password": "Samuel12345"})
        print()
        self.assertEqual(response.url, "/home/", msg="Valid login redirects to home")
        response = self.client.post("account_settings/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/account_settings", msg="Moves to account settings page")