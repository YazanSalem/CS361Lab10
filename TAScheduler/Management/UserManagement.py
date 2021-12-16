from TAScheduler.models import UserProfile

#test
class UserManagement(object):

    # Preconditions: The user has to have been instantiated.
    # The user must be of type administrator
    # Postconditions: Creates a user
    # Side-effects: User is created and added into the database
    # UserId(in) - Id of the user
    # User Name(in) - Name of the user
    # User Contact(in) - Contact of the user
    # User Type(in) - Type of the user
    @staticmethod
    def createUser(user_id, user_type, username, password, name, address, phone, email):
        UserManagement.__inputErrorCheck(user_id, user_type, username, password, name, address, phone, email)

        try:
            UserManagement.findUser(user_id)
        except TypeError:
            UserProfile.objects.create(
                userID=user_id,
                userType=user_type,
                username=username,
                password=password,
                name=name,
                address=address,
                phone=phone,
                email=email
            )
            return

        raise TypeError("This user already exists: ")

    # Preconditions: The user has to have been instantiated.
    # The user must be of type administrator
    # Postconditions: Edits a user
    # Side-effects: User is edited inside the database
    # UserId(in) - Id of the user
    # User Name(in) - Name of the user
    # User Contact(in) - Contact of the user

    # User Type(in) - Type of the user
    @staticmethod
    def editUser(user_id, user_type, username, password, name, address, phone, email):
        UserManagement.__inputErrorCheck(user_id, user_type, username, password, name, address, phone, email)

        try:
            change_user = UserManagement.findUser(user_id)
        except TypeError:
            raise TypeError("This user does not exist (editUser): ")
        change_user.userID = user_id
        change_user.userType = user_type
        change_user.username = username
        change_user.password = password
        change_user.name = name
        change_user.address = address
        change_user.phone = phone
        change_user.email = email
        change_user.save()

    # Preconditions: The user has to have been instantiated
    # There are accounts to display
    # Postconditions: Displays the user
    # Side-effects: None
    # UserId(in) - Id of the user
    @staticmethod
    def findUser(user_id=0, username=""):
        if not (user_id == 0):
            UserManagement.__inputErrorCheck(user_id=user_id, username=username)
            try:
                profile = UserProfile.objects.get(userID=user_id)
            except UserProfile.DoesNotExist:
                profile = None

            if profile is None:
                raise TypeError("This ID does not exist")
        elif not (username == ""):
            try:
                profile = UserProfile.objects.get(username=username)
            except UserProfile.DoesNotExist:
                profile = None

            if profile is None:
                raise TypeError("This username does not exist")
        else:
            raise TypeError("Unknown error")
            profile = None
        return profile

    # Preconditions: The user has to have been instantiated
    # The user must be of type administrator
    # Postconditions: User is deleted
    # Side-effects: User is deleted so it is removed from the database
    # UserId(in) - Id of the user
    @staticmethod
    def deleteUser(user_id):
        UserManagement.findUser(user_id).delete()

    # Preconditions: The user has to have been instantiated
    # There are accounts to display
    # Postconditions: All accounts are displayed
    # Side-effects: None
    @staticmethod
    def populateList():
        pass

    @staticmethod
    def __inputErrorCheck(user_id=0, user_type="TA", username="", password="", name="", address="", phone=0, email=""):
        if not (isinstance(int(user_id), int)):
            raise TypeError("Id entered is not of type int")
        if not (isinstance(user_type, str)):
            raise TypeError("userType entered is not of type str")
        if not (user_type in ["SUPERVISOR", "INSTRUCTOR", "TA"]):
            raise ValueError("userType entered is not a valid userType")
        if not (isinstance(username, str)):
            raise TypeError("Username entered is not of type str")
        if not (isinstance(password, str)):
            raise TypeError("Password entered is not of type str")
        if not (isinstance(name, str)):
            raise TypeError("Name entered is not of type str")
        if not (isinstance(address, str)):
            raise TypeError("Address entered is not of type str")
        if not (isinstance(int(phone), int)):
            raise TypeError("Contact entered is not of type str")
        if not (isinstance(email, str)):
            raise TypeError("Email entered is not of type str")
