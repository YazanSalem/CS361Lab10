from django.test import TestCase, Client
from TAScheduler.models import UserProfile


class TestViewUsersSupervisor(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = UserProfile.objects.create(userID=1, userType="INSTRUCTOR", username="Samuel",
                                                password="Samuel12345", name='Samuel', address="Address1",
                                                phone=9876543212, email="sam@uwm.edu")
        self.user2 = UserProfile.objects.create(userID=2, userType="TA", username="John", password="John12345",
                                                name="John", address="Address2", phone=1234567890, email="john@uwm.edu")
        self.supervisor = UserProfile.objects.create(userID=3, userType="SUPERVISOR", username="supervisor",
                                                     password="password", name="SupervisorGuy",
                                                     address="123 Street Street", phone=3211234567,
                                                     email="supervisor@supervisor.gov")
        self.client.post("/", {"useraccount": self.supervisor.username, "password": self.supervisor.password})
        self.resp = self.client.get("/view_users/")

    def test_userID(self):
        for user in self.resp.context["user_list"]:
            self.assertIn(str(user.userID), str(self.resp.content))

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
        TestViewUsersSupervisor.setUp(self)

    def test_userID(self):
        # for user in self.resp.context["user_list"]:
        pass

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
