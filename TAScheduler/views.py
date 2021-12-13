from django.shortcuts import render, redirect
from django.views import View
from .models import UserProfile, Course, Lab
from TAScheduler.Managment.UserManagement import UserManagement


# Create your views here.
# A method to check if a user is allowed to view a certain webpage based on their userType. Included a check for if
# the user is not logged in
# name: The name of the current user. Should be gotten using request.session["name"]
# valid_types: A list of all the types allowed to access the page. Should be all caps.
def userAllowed(request, valid_types):
    isValid = True
    try:
        if not (UserProfile.objects.get(userName=request.session["name"]).userType in valid_types):
            isValid = False
    except KeyError:
        isValid = False
    except UserProfile.DoesNotExist:
        isValid = False
    return isValid


class Login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        noUser = False
        incorrectPassword = False
        try:
            # checks to see if a user with the given name exists
            checkUser = UserProfile.objects.get(userName=request.POST['useraccount'])
            # if the name does exist, checks if the password is correct and sets incorrectPassword accordingly
            incorrectPassword = (checkUser.userPassword != request.POST['password'])
        except UserProfile.DoesNotExist:
            # if there is no user with the given name, an exception is thrown, in which case, noUser is set to true
            noUser = True
        if noUser:
            # if the username does not yet exist, the user is returned to the login page.
            # a message field would be a good thing to implement so the reason login was not completed is explained
            # to the user
            return render(request, "login.html")
        elif incorrectPassword:
            # if the password is incorrect for the given name, the user is returned to the login page
            # a message field would be a good thing to implement so the reason login was not completed is explained
            # to the user
            return render(request, "login.html")
        else:
            # if no issues are found, the user is redirected and the request.session["name"] field is set to the name
            # of the user
            request.session["name"] = checkUser.userName
            return redirect("/home/")


class Home(View):
    def get(self, request):
        # If the user does not have a valid name, I.E. if they try to manually enter /home in the search bar,
        # they will fail the userAllowed test and be redirected back to the login page
        # If the user is allowed then home is rendered like normal
        if userAllowed(request, ["SUPERVISOR", "INSTRUCTOR", "TA"]):
            return render(request, "home.html")
        else:
            return redirect("/../")


class CreateUser(View):
    def get(self, request):
        # If the user does not have a valid name or if they are not of the type SUPERVISOR, they will fail
        # userAllowed and will be redirected to home
        if userAllowed(request, ["SUPERVISOR"]):
            return render(request, "createuser.html", {})
        else:
            return redirect("/../home/")

    def post(self, request):
        # Takes user input of all parameters and creates a new user.
        # Need to replace this line with UserManagement.createUser once that is implemented.
        newUser = UserProfile(userID=request.POST['userID'], userType=request.POST['userType'].upper(),
                              userPassword=request.POST['userPassword'], userName=request.POST['userName'],
                              userAddress=request.POST['userAddress'], userContact=request.POST['userContact'],
                              userEmail=request.POST['userEmail'])
        newUser.save()
        return render(request, "createuser.html")


class CreateCourse(View):
    def get(self, request):
        # If the user does not have a valid name or if they are not of the type SUPERVISOR, they will fail
        # userAllowed and be redirected to home
        if userAllowed(request, ['SUPERVISOR']):
            return render(request, "createcourse.html", {})
        else:
            return redirect("/../home/")

    def post(self, request):
        # Takes user input of all parameters and creates a new course.
        # Need to replace this line with CourseManagement.createCourse once that is implemented.
        newCourse = Course(courseID=request.POST['ID'], name=request.POST['name'], location=request.POST['location'],
                           hours=request.POST['hours'], days=request.POST['days'],
                           instructor=UserProfile.objects.get(userName=request.POST['instructor']))
        newCourse.save()
        newCourse.TAs.add(UserProfile.objects.get(userName=request.POST['TAs']))
        newCourse.labs.add(Lab.objects.get(name=request.POST['labs']))
        newCourse.save()
        return render(request, "createcourse.html")


class AccountSettings(View):
    def get(self, request):
        # If the user does not have a valid name, I.E. if they try to manually enter /home in the search bar,
        # they will fail the userAllowed test and be redirected back to the login page
        # If the user is allowed then home is rendered like normal
        if userAllowed(request, ["SUPERVISOR", "INSTRUCTOR", "TA"]):
            return render(request, "accountsettings.html")
        else:
            return redirect("/../")


class EditUser(View):
    def get(self, request):
        # If the user does not have a valid name, I.E. if they try to manually enter /home in the search bar,
        # they will fail the userAllowed test and be redirected back to the login page
        # If the user is allowed then home is rendered like normal
        if userAllowed(request, ["SUPERVISOR"]):
            return render(request, "edituser.html")
        else:
            return redirect("/../home/")


class EditCourse(View):
    def get(self, request):
        # If the user does not have a valid name, I.E. if they try to manually enter /home in the search bar,
        # they will fail the userAllowed test and be redirected back to the login page
        # If the user is allowed then home is rendered like normal
        if userAllowed(request, ["SUPERVISOR"]):
            return render(request, "editcourse.html")
        else:
            return redirect("/../home/")


class CreateLab(View):
    def get(self, request):
        # If the user does not have a valid name or if they are not of the type SUPERVISOR, they will fail
        # userAllowed and be redirected to home
        if userAllowed(request, ['SUPERVISOR']):
            return render(request, "createlab.html", {})
        else:
            return redirect("/../home/")

    def post(self, request):
        # Takes user input of all parameters and creates a new lab.
        # Need to replace this line with CourseManagement.createCourse once that is implemented.
        newLab = Lab(labID=request.POST['ID'], name=request.POST['name'], location=request.POST['location'],
                     hours=request.POST['hours'], days=request.POST['days'],
                     instructor=UserProfile.objects.get(userName=request.POST['instructor']),
                     TA=UserProfile.objects.get(userName=request.POST['TA']))
        newLab.save()
        return render(request, "createlab.html")


class EditLab(View):
    def get(self, request):
        # If the user does not have a valid name, I.E. if they try to manually enter /home in the search bar,
        # they will fail the userAllowed test and be redirected back to the login page
        # If the user is allowed then home is rendered like normal
        if userAllowed(request, ["SUPERVISOR"]):
            return render(request, "editlab.html")
        else:
            return redirect("/../home/")


class ClassSchedules(View):
    pass


class UserManagement(View):
    pass


class ClassLabManagement(View):
    pass


class CourseTAAssignments(View):
    pass


class UserList(View):
    pass


class AccountCreation(View):
    pass


class ClassList(View):
    pass


class CourseCreation(View):
    pass


class LabList(View):
    pass


class CourseAssignments(View):
    pass


class TAList(View):
    pass
