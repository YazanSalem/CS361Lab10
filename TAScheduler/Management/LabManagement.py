from TAScheduler.models import *


class LabManagement(object):

    # class Lab(models.Model):
    #    labID = models.IntegerField()
    #    name = models.CharField(max_length=20)
    #    location = models.CharField(max_length=20)
    #    hours = models.CharField(max_length=20)
    #    days = models.CharField(max_length=20)
    #    course = models.ForeignKey(Course, on_delete=models.CASCADE
    #    TA = models.ForeignKey(UserProfile, on_delete=models.PROTECT, related_name="TAToLab")

    # Preconditions: The user has to have been instantiated.
    # Postconditions: The lab is now created
    # Side-effects: Lab is created and added inside the database
    # lab_id(in) - Id of the lab
    # lab_name(in) - Name of the lab
    # lab_location(in) - Location of the lab
    # lab_hours(in) - Hours of the lab
    # lab_days(in) - Days of the lab
    # course(in) - Instructor of the lab
    # ta(in) -TA of the lab
    @staticmethod
    def createLab(lab_id, lab_name, lab_location, lab_hours, lab_days, course, ta):
        LabManagement.__inputErrorCheck(lab_id, lab_name, lab_hours, lab_location, lab_days, course, ta)
        Lab.objects.create(labID=lab_id, name=lab_name, location=lab_location, hours=lab_hours, days=lab_days, course=course, TA=ta)

        return "Lab was created"
    
    # Preconditions: Both the lab and the TA must exist in the database
    # Postconditions: The TA for the lab is updated to the given TA
    # Lab id(in) - ID of the lab
    # Lab ta(in) - Profile of the TA to be assigned to the lab
    @staticmethod
    def addTA(lab_id, lab_ta):
        LabManagement.__inputErrorCheck(lab_id,"", "", "", "", None, lab_ta)
        if not (Lab.objects.filter(labID=lab_id).exists()):
            raise TypeError("This Lab does not exist")

        lab = Lab.objects.get(labID=lab_id)
        lab.TA = lab_ta

        return "TA was assigned to the lab"

    # Preconditions: The user has to have been instantiated.
    # Postconditions: The lab is now edited
    # Side-effects: Lab is edited inside the database
    # lab_id(in) - Id of the lab
    # lab_name(in) - Name of the lab
    # lab_hours(in) - Hours of the lab
    # lab_location(in) - Location of the lab
    # lab_days(in) - Days of the lab
    # course(in) - course of the lab
    # ta(in) -TA of the lab
    @staticmethod
    def editLab(lab_id, lab_name, lab_hours, lab_location, lab_days, course, ta):
        LabManagement.__inputErrorCheck(lab_id, lab_name, lab_hours, lab_location, lab_days, course, ta)
        if not (Lab.objects.filter(labID=lab_id).exists()):
            raise TypeError("This Lab does not exist")

        editedLab = Lab.objects.get(labID=lab_id)

        editedLab.name = lab_name
        editedLab.location = lab_location
        editedLab.hours = lab_hours
        editedLab.days = lab_days
        editedLab.course = course
        editedLab.TA = ta
        editedLab.save()

        return "The lab was successfully edited"

    # Preconditions: The user has to have been instantiated.
    # The user must be of type administrator
    # Postconditions:Deletes a lab
    # Side-effects: Lab is deleted and removed from the database
    # Lab Name(in) - Name of the course
    @staticmethod
    def deleteLab(lab_id):
        if not (isinstance(lab_id, int)):
            raise TypeError("lab_id entered is not of type int")

        retMsg = "Lab has been successfully deleted"
        if not (Lab.objects.filter(labID=lab_id).exists()):
            retMsg = "This lab being deleted does not exist"
        else:
            Lab.objects.get(labID=lab_id).delete()

        return retMsg

    # Preconditions: The user has to have been instantiated
    # The LabID is an existing lab_id 
    # Postconditions: Lab assignments are populated
    # Side-effects: None
    # Lab Id(in): Lab Id you are searching for
    @staticmethod
    def populateSearchLab(lab_id):
        if not (isinstance(lab_id, int)):
            raise TypeError("lab_id entered is not of type int")

        if not (Lab.objects.filter(labID=lab_id).exists()):
            retMsg = "This lab being deleted does not exist"
        else:
            retMsg = {
                'Found Lab': Lab.objects.get(labID=lab_id)
            }

        return retMsg

    # Preconditions: The user has to have been instantiated
    # There are labs to display
    # Postconditions: All labs are displayed
    # Side-effects: None
    @staticmethod
    def displayAllLabs():
        return Lab.objects.all()

    @staticmethod
    def __inputErrorCheck(lab_id=0, lab_name="", lab_location="", lab_hours="", lab_days="", course=None, ta=None):
        if not (isinstance(lab_id, int)):
            raise TypeError("lab_id entered is not of type int")
        if not (isinstance(lab_name, str)):
            raise TypeError("Lab Name entered is not of type str")
        if not (isinstance(lab_location, str)):
            raise TypeError("Lab Location entered is not of type str")
        if not (isinstance(lab_hours, str)):
            raise TypeError("Lab Hours entered is not of type str")
        if not (isinstance(lab_days, str)):
            raise TypeError("Lab Days entered is not of type str")
        if not(isinstance(course, Course)):
            raise TypeError("Course entered is not of type course")
        if not(ta is None):
            if not (isinstance(ta, UserProfile)):
                raise TypeError("Lab TA entered is not of type User")
            if ta.userType != "TA":
                raise TypeError("Lab TA's type is not of type TA")
