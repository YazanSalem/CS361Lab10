from django.test import TestCase, Client
from TAScheduler.Management.UserManagement import UserManagement
from TAScheduler.models import UserProfile


class TestViewSupervisorUsers(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = UserProfile.objects.create(name='Samuel', password='Samuel12345')
        self.user2 = UserProfile.objects.create(name='John', password='John12345')

    # check to account settings
    def test_viewInstructorTA_to_accountsettings(self):
        response = self.client.post("/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/home/", msg="Valid login redirects to home")

<<<<<<< Updated upstream
        response = self.client.post("account_settings/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/account_settings", msg="Moves to account settings page")

    # check to home
    def test_view_InstructorTA_to_home(self):
        response = self.client.post("/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/home/", msg="Valid login redirects to home")
=======
    def test_userType(self):
        for user in self.resp.context["user_list"]:
            self.assertIn(str(user.userType), str(self.resp.content))
        pass

    def test_username(self):
        for user in self.resp.context["user_list"]:
            self.assertIn(str(user.username), str(self.resp.content))
        pass
>>>>>>> Stashed changes

        response = self.client.post("home/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/home", msg="Moves to Home page")

        # check to logout
    def test_view_InstructorTA_to_logout(self):
        response = self.client.post("/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/home/", msg="Valid login redirects to home")

        response = self.client.post("/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/", msg="Moves to account settings page")


class TestViewInstructorAndTAUsers(TestCase):
    def setUp(self):
<<<<<<< Updated upstream
        self.client = Client()
        self.user1 = UserProfile.objects.create(name='Samuel', password='Samuel12345')
        self.user2 = UserProfile.objects.create(name='John', password='John12345')

        # check for CreateUser

    def test_view_Supervisor_to_createUser(self):
        response = self.client.post("/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/home/", msg="Valid login redirects to home")

        response = self.client.post("Create_User/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/Create_User", msg="Moves to Create User page")

        # check for EditUser

    def test_view_Supervisor_to_editUser(self):
        response = self.client.post("/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/home/", msg="Valid login redirects to home")

        response = self.client.post("edit_User/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/edit_User", msg="Moves to Edit User page")

        # check for deleteUser

    def test_view_Supervisor_to_deleteUser(self):
        response = self.client.post("/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/home/", msg="Valid login redirects to home")

        response = self.client.post("delete_User/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/account_User", msg="Moves to Delete User page")

        # check for account settings

    def test_view_Supervisor_to_accountsettings(self):
        response = self.client.post("/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/home/", msg="Valid login redirects to home")

        response = self.client.post("account_settings/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/account_settings", msg="Moves to account settings page")

        # check for home

    def test_view_Supervisor_to_home(self):
        response = self.client.post("/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/home/", msg="Valid login redirects to home")

        response = self.client.post("home/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/home", msg="Moves to Home page")

        # check for logout

    def test_view_Supervisor_to_logout(self):
        response = self.client.post("/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/home/", msg="Valid login redirects to home")
        response = self.client.post("/", {"useraccount": "Samuel", "password": "Samuel12345"})
        self.assertEqual(response.url, "/", msg="Moves to logout page")
        # response = self.client.get("account_settings/", follow=True)
        # testAdminID = UserProfile.objects.filter(userID=1000)
        # pageID = response.client.get('user')
        # self.assertTrue(pageID, "1000")

        # ** *Test Cases ** *
        #
        # User can create an account and log in
        #     Create Valid User fred P4ssw0rd
        #     Attempt to Login with Credentials    fred    P4ssw0rd
        #     Status Should Be Logged In
        #
        # User cannot log in with bad password
        #     Create Valid User betty P4ssw0rd
        #     Attempt to Login with Credentials    betty    wrong
        #     Status Should Be Access Denied
        # add an item
        # response = self.client.post('/', {'username': 'Samuel', 'password': '12345'})
        # self.assertEqual(response.url, '/things/')
        # response = self.client.get('/things/', {'name': self.user1.name})  # we are trying to retreive something from the database
        # post is when we want to do something in the database, need some validation, creation, updating from the database
        # # print(response.context['things'])
        # self.assertEqual(response.context['things'], [self.stuff1.name, self.stuff2.name])
=======
        TestViewUsersSupervisor.setUp(self)
        response = self.client.get("/view_users/")

    def test_userID(self):
        # for user in self.resp.context["user_list"]:
        for user in self.resp.context["user_list"]:
            self.assertIn(str(user.userID), str(self.resp.content), "User " + user.username + " 's userID did not display")

    def test_userType(self):
        for user in self.resp.context["user_list"]:
            self.assertIn(str(user.userType), str(self.resp.content), "User " + user.username + " 's userType did not display")

    def test_username(self):
        for user in self.resp.context["user_list"]:
            self.assertIn(str(user.username), str(self.resp.content), "User " + user.username + " 's username did not display")

    def test_password(self):
        # Should assert false
        for user in self.resp.context["user_list"]:
            if str(self.resp.content).find(user.password) == -1:
                self.assertNotIn(str(user.password), str(self.resp.content), "User " + user.username + " 's password did not display")

    def test_name(self):
        for user in self.resp.context["user_list"]:
            self.assertIn(str(user.name), str(self.resp.content), "User " + user.username + " 's name did not display")

    def test_address(self):
        for user in self.resp.context["user_list"]:
            self.assertIn(str(user.address), str(self.resp.content), "User " + user.username + " 's address did not display")

    def test_phone(self):
        for user in self.resp.context["user_list"]:
            self.assertIn(str(user.phone), str(self.resp.content), "User " + user.username + " 's phone did not display")

    def test_email(self):
        for user in self.resp.context["user_list"]:
            self.assertIn(str(user.email), str(self.resp.content), "User " + user.username + " 's email did not display")
>>>>>>> Stashed changes
