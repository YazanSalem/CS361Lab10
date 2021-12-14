from TAScheduler.models import Lab
from TAScheduler.models import UserProfile


class LabManagement(object):

    # class Lab(models.Model):
    #    labID = models.IntegerField(default=0)
    #    name = models.CharField(max_length=20)
    #    location = models.CharField(max_length=20)
    #    hours = models.CharField(max_length=20)
    #    days = models.CharField(max_length=20)
    #    instructor = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    #    TA = models.ForeignKey(UserProfile, on_delete=models.PROTECT, related_name="TAToLab")

    # Preconditions: The user has to have been instantiated.
    # Postconditions: The lab is now created
    # Side-effects: Lab is created and added inside the database
    # Lab ID(in) - Id of the lab
    # Lab Name(in) - Name of the lab
    # Lab Hours(in) - Hours of the lab
    # Lab Location(in) - Location of the lab
    # Lab Days(in) - Days of the lab
    # Lab Instructor(in) - Instructor of the lab
    # Lab TA(in) -TA of the lab
    @staticmethod
    def createLab(lab_id, lab_name, lab_location, lab_hours, lab_days, lab_instructor, lab_ta):
        LabManagement.__inputErrorCheck(lab_id, lab_name, lab_hours, lab_location, lab_days, lab_instructor, lab_ta)
        Lab.objects.create(labID=lab_id, name=lab_name, location=lab_location,
                           hours=lab_hours, days=lab_days, instructor=lab_instructor, TA=lab_ta)

        return "Lab was created"

    # Preconditions: The user has to have been instantiated.
    # Postconditions: The lab is now edited
    # Side-effects: Lab is edited inside the database
    # Lab ID(in) - Id of the lab
    # Lab Name(in) - Name of the lab
    # Lab Hours(in) - Hours of the lab
    # Lab Location(in) - Location of the lab
    # Lab Days(in) - Days of the lab
    # Lab Instructor(in) - Instructor of the lab
    # Lab TA(in) -TA of the lab
    @staticmethod
    def editLab(lab_id, lab_name, lab_hours, lab_location, lab_days, lab_instructor, lab_ta):
        LabManagement.__inputErrorCheck(lab_id, lab_name, lab_hours, lab_location, lab_days, lab_instructor, lab_ta)
        if not (Lab.objects.filter(labID=lab_id).exists()):
            raise TypeError("This Lab does not exist")

        editedLab = Lab.objects.get(labID=lab_id)

        editedLab.name = lab_name
        editedLab.location = lab_location
        editedLab.hours = lab_hours
        editedLab.days = lab_days
        editedLab.instructor = lab_instructor
        editedLab.TA = lab_ta
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
            Lab.objects.filter(labID=lab_id).delete()

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
    def __inputErrorCheck(lab_id=0, lab_name="", lab_location="", lab_hours="", lab_days="", lab_instructor=None,
                          lab_ta=None):
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
        if not (isinstance(lab_instructor, UserProfile)):
            raise TypeError("Lab Instructor entered is not of type User")
        if lab_instructor.userType != "INSTRUCTOR":
            raise TypeError("Lab Instructor's type is not of type INSTRUCTOR")
        if not (isinstance(lab_ta, UserProfile)):
            raise TypeError("Lab TA entered is not of type User")
        if lab_ta.userType != "TA":
            raise TypeError("Lab TA's type is not of type TA")
