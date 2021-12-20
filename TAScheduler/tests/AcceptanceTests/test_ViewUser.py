from django.test import TestCase, Client
from TAScheduler.models import UserProfile


class TestViewSupervisorUsers(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = UserProfile.objects.create(name='Samuel', password='Samuel12345')
        self.user2 = UserProfile.objects.create(name='John', password='John12345')
        self.supervisor = UserProfile.objects.create(userID=1, userType="SUPERVISOR", username="supervisor", password="password")
        self.client.post("/", {"useraccount": self.supervisor.username, "password": self.supervisor.password})
        self.resp = self.client.get("/view_users/")


    def test_userID(self):
        for user in self.resp.context["user_list"]:


    def test_userType(self):
        pass

    def test_username(self):
        pass

    def test_password(self):
        # Should assert false
        pass

    def test_name(self):
        pass

    def test_address(self):
        # Should assert false
        pass

    def test_phone(self):
        # Should assert false
        pass

    def test_email(self):
        pass

class TestViewUsersInstructor(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = UserProfile.objects.create(name='Samuel', password='Samuel12345')
        self.user2 = UserProfile.objects.create(name='John', password='John12345')
        self.supervisor = UserProfile.objects.create(userID=1, userType="INSTRUCTOR", username="instructor", password="password")
        self.client.post("/", {"useraccount": self.supervisor.username, "password": self.supervisor.password})
        self.resp = self.client.get("/view_users/")

    def test_userID(self):
        for user in self.resp.context["user_list"]:

    def test_userType(self):
        pass

    def test_username(self):
        pass

    def test_password(self):
        # Should assert false
        pass

    def test_name(self):
        pass

    def test_address(self):
        pass

    def test_phone(self):
        pass

    def test_email(self):
        pass