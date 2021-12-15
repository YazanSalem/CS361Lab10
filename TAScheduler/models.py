from django.db import models


# Create your models here.


# UserProfile acts as the class that will be used for all users with the userType variable determining whether they
# are an instructor, TA, or Administrator
class UserProfile(models.Model):
    userID = models.IntegerField(default=0)
    userType = models.CharField(max_length=20,
                                choices=[('SUPERVISOR', 'Supervisor'), ('INSTRUCTOR', 'Instructor'), ('TA', 'TA')])
    username = models.CharField(max_length=20, default="")
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    phone = models.IntegerField(default=0)
    email = models.EmailField(max_length=30)


# The Lab class keeps track of the information for a particular lab section and references the instructor of the course
# to keep track of which course it relates to.
class Lab(models.Model):
    labID = models.IntegerField(default=0)
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    hours = models.CharField(max_length=20)
    days = models.CharField(max_length=20)
    instructor = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    TA = models.ForeignKey(UserProfile, on_delete=models.PROTECT, related_name="TAToLab")


# The Course class keeps track of lecture sections and stores the TAs, instructors, and labs associated with it.
class Course(models.Model):
    courseID = models.IntegerField()
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    hours = models.TimeField()
    days = models.CharField(max_length=20)
    instructor = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    TAs = models.ManyToManyField(UserProfile, related_name="TAToCourse")
    labs = models.ManyToManyField(Lab)

    # class Meta:
    #     db_table = "CourseList"


# Schedule is a tool to be used by users to display the events they have going on in a week, be that Labs or courses.
class Schedule(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)
    labs = models.ManyToManyField(Lab)
