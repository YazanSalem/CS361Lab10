from django.shortcuts import render, redirect
from django.views import View
from .models import UserProfile, Course, Lab
from TAScheduler.Managment import UserManagement,LabManagement,CourseManagement
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
          

class ClassSchedules(View):
    pass

class DeleteLab(View):
    def get(request):
        # If the user does not have a valid name, I.E. if they try to manually enter /home in the search bar,
        # they will fail the userAllowed test and be redirected back to the login page
        # If the user is allowed then home is rendered like normal
        if userAllowed(request, ["SUPERVISOR"]):
            return render(request, "deletelab.html", {"lab_list":Lab.objects.all()})
        else:
            return redirect("/../home/")

    def post(request):
        delete = True
        try:
            delete_or_submit = int(request.POST["delete"])
        except MultiValueDictKeyError:
            delete_or_submit = int(request.POST["submit"])
            delete = False
        if delete:
            deleted_lab = Lab.objects.get(labID = delete_or_submit)
            Lab.objects.delete(labID=delete_or_submit)
            return render(request, "deletelab.html", {"lab_list":Lab.objects.all(), "deleted_lab": deleted_lab})
        else:
            return render(request, "deletelab.html", {"lab_list": Lab.objects.all()})

class DeleteCourse(View):
    def get(request):
        # If the user does not have a valid name, I.E. if they try to manually enter /home in the search bar,
        # they will fail the userAllowed test and be redirected back to the login page
        # If the user is allowed then home is rendered like normal
        if userAllowed(request, ["SUPERVISOR"]):
            return render(request, "deletecourse.html", {"course_list":Course.objects.all()})
        else:
            return redirect("/../home/")

    def post(request):
        delete = True
        try:
            delete_or_submit = int(request.POST["delete"])
        except MultiValueDictKeyError:
            delete_or_submit = int(request.POST["submit"])
            delete = False
        if delete:
            deleted_course = Course.objects.get(courseID = delete_or_submit)
            Course.objects.delete(courseID=delete_or_submit)
            return render(request, "deletecourse.html", {"course_list":Course.objects.all(), "deleted_course": deleted_course})
        else:
            return render(request, "deletecourse.html", {"course_list": Course.objects.all()})

class DeleteUser(View):
    def get(request):
        # If the user does not have a valid name, I.E. if they try to manually enter /home in the search bar,
        # they will fail the userAllowed test and be redirected back to the login page
        # If the user is allowed then home is rendered like normal
        if userAllowed(request, ["SUPERVISOR"]):
            return render(request, "deleteuser.html", {"user_list":UserProfile.objects.all()})
        else:
            return redirect("/../home/")

    def post(request):
        delete = True
        try:
            delete_or_submit = int(request.POST["delete"])
        except MultiValueDictKeyError:
            delete_or_submit = int(request.POST["submit"])
            delete = False
        if delete:
            UserProfile.objects.delete(userID=delete_or_submit)
            deleted_user= UserProfile.objects.get(courseID = delete_or_submit)
            return render(request, "deleteuser.html", {"user_list":UserProfile.objects.all(), "deleted_user": deleted_user})
        else:
            return render(request, "deleteuser.html", {"user_list": UserProfile.objects.all()})

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
