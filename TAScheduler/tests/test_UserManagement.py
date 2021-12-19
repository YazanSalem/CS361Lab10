from django.test import TestCase
from TAScheduler.Management.UserManagement import UserManagement
from TAScheduler.models import *


class TestMyUser(TestCase):

    def setUp(self):
        '''
        testusr0: to be empty at all times.
        testusr1: has every field filled off the bat.
        #ID, name, contact, ssn, address, password, userType (we'll use numerical flags for this)
        testusr2: to be used for all of the "set" functions.
        '''

        testusr0 = UserProfile.objects.create()
        testusr1 = UserManagement.createUser(user_id=1000, user_type="SUPERVISOR", username="mrwick123",
                                             password="password",
                                             name="John Wick", address="894 Lake Street, Milwaukee, Wisconsin 99999",
                                             phone=4142542688,
                                             email="johnwick123@uwm.edu")
        testusr2 = UserManagement.createUser(user_id=1001, user_type="INSTRUCTOR", username="mrbond123",
                                             password="password",
                                             name="James Bond", address="123 Kenwood Ave, Milwaukee, Wisconsin 99999",
                                             phone=4144567890,
                                             email="jamesbond123@uwm.edu")

        self.testUser = UserProfile.objects.get(userID=1000, userType="SUPERVISOR", username="mrwick123",
                                                password="password",
                                                name="John Wick", address="894 Lake Street, Milwaukee, Wisconsin 99999",
                                                phone=4142542688,
                                                email="johnwick123@uwm.edu")

        # Course.objects.create(courseID=1001, name="System Programming", location="EMS 180", days="T, Th",
        #                       hours="10:00 AM - 10:50 AM", instructor=self.instructor)
        # self.testCourse = Course.objects.get(courseID=1000)
        # self.testCourse = Course.objects.get(courseID=1000)

    def test_invalid_login(self):
        response = self.client.post('/', {'username': 'Superman', 'password': '24680'})
        self.assertEqual(response.url, 'invalid_login_response')
        # print(response.context['error_messages'])
        self.assertEqual(response.context['error'], 'username or password are incorrect')

    def test_valid_login(self):
        response = self.client.post('/', {'username': 'Samuel', 'password': '12345'})
        self.assertEqual(response.url, '/valid_login_response/')
        # print(response.context['error_messages'])
        self.assertEqual(response.context['Validation'], 'username or password are correct')

    def test_UserID(self):
        self.assertEqual(1000, self.testUser.userID, "User ID was not set correctly when creating a User.")

    def test_InvalidUserID(self):
        # self.assertEqual(1000, self.testUser.UserID, "User ID was not set correctly when creating a User.")
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when createUser was passed a courseID with an "
                                   "invalid type"):
            UserManagement.createUser(user_id=1001, user_type="SUPERVISOR", username="johndoe", password="john123",
                                      name="John Doe",
                                      address="3400 N Maryland Ave, Milwaukee, Wisconsin 53211",
                                      phone=4142340987, email="johndoe123@uwm.edu")

    def test_UserType(self):
        self.assertEqual("SUPERVISOR", self.testUser.userType, "User type was not set correctly when creating a User.")

    def test_InvalidUserType(self):
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when createUser was passed a user type with an "
                                   "invalid type"):
            UserManagement.createUser(user_id=1001, user_type=123, username="johndoe", password="john123",
                                      name="John Doe",
                                      address="3400 N Maryland Ave, Milwaukee, Wisconsin 53211",
                                      phone=4142340987, email="johndoe123@uwm.edu")

    def test_UserUsername(self):
        self.assertEqual("mrwick123", self.testUser.username, "User username was not set correctly when "
                                                                    "creating a User.")

    def test_InvalidUsername(self):
        # self.assertEqual("not johnwick", self.testUser.UserUsername, "User username was not set correctly when "
        #                                                              "creating a User.")
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when createUser was passed a Username with an "
                                   "invalid type"):
            UserManagement.createUser(user_id=1001, user_type="SUPERVISOR", username=123, password="john123",
                                      name="John Doe",
                                      address="3400 N Maryland Ave, Milwaukee, Wisconsin 53211",
                                      phone=4142340987, email="johndoe123@uwm.edu")

    def test_UserPassword(self):
        self.assertEqual("password", self.testUser.password, "User Password was not set correctly when creating a "
                                                                 "User.")

    def test_InvalidUserPassword(self):
        # self.assertEqual("incorrectPassword", self.testUser.UserPassword, "User Password was not set correctly when "
        #                                                                   "creating a User.")
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when createUser was passed a password with an "
                                   "invalid type"):
            UserManagement.createUser(user_id=1001, user_type="SUPERVISOR", username="johndoe", password=5432345,
                                      name="John Doe",
                                      address="3400 N Maryland Ave, Milwaukee, Wisconsin 53211",
                                      phone=4142340987, email="johndoe123@uwm.edu")

    def test_UserName(self):
        self.assertEqual("John Wick", self.testUser.name, "User Name was not set correctly when creating a User.")

    def test_InvalidUserName(self):
        # self.assertEqual("notmrwick123", self.testUser.UserName, "User Name was not set correctly when creating a
        # User.")
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when createUser was passed a Name with an "
                                   "invalid type"):
            UserManagement.createUser(user_id=1001, user_type=123, username="johndoe", password="john123",
                                      name="John Doe",
                                      address="3400 N Maryland Ave, Milwaukee, Wisconsin 53211",
                                      phone=4142340987, email="johndoe123@uwm.edu")

    def test_UserAddress(self):
        self.assertEqual("894 Lake Street, Milwaukee, Wisconsin 99999", self.testUser.address, "User Address was "
                                                                                                   "not set correctly"
                                                                                                   " when creating a "
                                                                                                   "User.")

    def test_InvalidUserAddress(self):
        # self.assertEqual("123 Kenwood Ave, Milwaukee, Wisconsin 53211", self.testUser.UserAddress, "User Address was "
        #                                                                                            "not set correctly"
        #                                                                                            " when creating a "
        #                                                                                            "User.")
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when createUser was passed an address with an "
                                   "invalid type"):
            UserManagement.createUser(user_id=1001, user_type=123, username="johndoe", password="john123",
                                      name="John Doe",
                                      address=123, phone=4142340987, email="johndoe123@uwm.edu")

    def test_UserPhone(self):
        self.assertEqual(4142542688, self.testUser.phone, "User Phone was not set correctly when creating a User.")

    def test_InvalidUserPhone(self):
        # self.assertEqual(4141245944, self.testUser.UserPhone, "User Phone was not set correctly when creating a
        # User.")
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when createUser was passed a phone number with an "
                                   "invalid type"):
            UserManagement.createUser(user_id=1001, user_type=123, username="johndoe", password="john123",
                                      name="John Doe",
                                      address="3400 N Maryland Ave, Milwaukee, Wisconsin 53211",
                                      phone="4142340987", email="johndoe123@uwm.edu")

    def test_UserEmail(self):
        self.assertEqual("johnwick123@uwm.edu", self.testUser.email, "User Email was not set correctly when "
                                                                         "creating a User.")

    def test_InvalidUserEmail(self):
        # self.assertEqual("notjohnwick123@uwm.edu", self.testUser.UserEmail, "User Email was not set correctly when "
        #                                                                     "creating a User.")
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when createUser was passed a courseID with an "
                                   "invalid type"):
            UserManagement.createUser(user_id=1001, user_type=123, username="johndoe", password="john123",
                                      name="John Doe",
                                      address="3400 N Maryland Ave, Milwaukee, Wisconsin 53211",
                                      phone=4142340987, email=123456)
