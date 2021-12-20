from django.test import TestCase, Client
from TAScheduler.models import *


# Delete User Cases: Successful Delete,
# If a user deletes himself sent back to login
# Cannot delete Instructor if assigned to course
# Cannot delete User TA if assigned to lab
class SuccessfulDeleteUser(TestCase):
    dummyClient = None
    TA = None
    instructor = None
    admin = None

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

    def test_deleteUser(self):
        resp = self.dummyClient.post('/delete_user/', {'userID': 1}, follow=True)
        var = UserProfile.objects.count()
        self.assertEquals(var, 2)
        allUsers = list(UserProfile.objects.filter(userID=1))
        self.assertEquals(allUsers, [self.instructor, self.admin])


class DeleteYourself(TestCase):
    dummyClient = None
    admin = None

    def setUp(self):
        self.dummyClient = Client()

        self.admin = UserProfile.objects.create(userID=3, userTyoe="SUPERVISOR", username="Admin1"
                                                , password="Admin123", name="Admin Dummy", address="Admin Address",
                                                phone=3234452176, email="AdminEmail@email.com")

    def test_deleteYourself(self):
        pass


class DeleteInstructorAssignedToCourse(TestCase):
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

        self.course = Course.objects.create(courseID=1, name="Software Engineering",
                                            location="EMS 180", hours="12:00PM - 01:00PM", days="M, W",
                                            instructor=self.instructor,
                                            TAs=[self.TA])

    def test_deleteInstructorAssignedToCourse(self):
        pass


class DeleteTAAssignedToLab(TestCase):
    dummyClient = None
    TA = None
    instructor = None
    admin = None
    course = None
    lab = None

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

        self.course = Course.objects.create(courseID=1, name="Software Engineering",
                                            location="EMS 180", hours="12:00PM - 01:00PM", days="M, W",
                                            instructor=self.instructor,
                                            TAs=[self.TA])

        self.lab = Lab.objects.create(labID=1, name="Lab", location="EMS 280",
                                      hours="03:00PM - 04:00PM", days="M, W", course=self.course, TA=self.TA)

    def test_deleteTAAssignedToLab(self):
        pass
