from django.test import TestCase
from TAScheduler.Management.CourseManagement import CourseManagement
from TAScheduler.models import *


# createCourse(courseName, courseTime, courseDays, courseHours, courseInstructor, courseTA)
# editCourse(courseName, courseTime, courseDays, courseHours, courseInstructor, courseTA)
# deleteCourse(courseName)
# populateSearchClass(searchPromp)  should change class to course
# displayAllCourse()

class TestCreateCourse(TestCase):

    def setUp(self):
        UserProfile(userID=1, userType="INSTRUCTOR", username="instructor", password="password",
                    name="Professor Layton", address="3400 N Maryland Ave", phone="6085555432",
                    email="layton@gmail.com").save()
        self.instructor = UserProfile.objects.get(userID=1)
        UserProfile(userID=2, userType="TA", username="ta", password="password", name="Luke",
                    address="2400 S Maryland Ave", phone="4145543212", email="luke@gmail.com").save()
        self.TA = UserProfile.objects.get(userID=2)

        CourseManagement.createCourse(course_id=1000, name="Computer Programming", location="EMS E240", days="M, W, F",
                                      hours="12:00 PM - 12:50 PM", instructor=self.instructor, tas=[self.TA])

        self.testCourse = Course.objects.get(courseID=1000)

    def test_courseID(self):
        self.assertEqual(1000, self.testCourse.courseID, "Course ID was not set correctly when creating course.")

    def test_courseName(self):
        self.assertEqual("Computer Programming", self.testCourse.name,
                         "Course name was not set correctly when creating course.")

    def test_courseLocation(self):
        self.assertEqual("EMS E240", self.testCourse.location,
                         "Course location was not set correctly when creating course.")

    def test_courseDays(self):
        self.assertEqual("M, W, F", self.testCourse.days, "Course days were not set correctly when creating course.")

    def test_invalidDays(self):
        with self.assertRaises(ValueError,
                               msg="An exception was not raised when createCourse was passed invalid days."):
            CourseManagement.createCourse(course_id=11, name="Course", location="location", days="invalid input",
                                          hours="1:00 PM - 8:00 PM", instructor=self.instructor)

    def test_invalidDaysType(self):
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when createCourse was passed invalid type for days."):
            CourseManagement.createCourse(course_id=12, name="Course", location="location", days=20,
                                          hours="1:00 PM - 8:00 PM", instructor=self.instructor)

    def test_courseHours(self):
        self.assertEqual("12:00 PM - 12:50 PM", self.testCourse.hours,
                         "Course hours were not set correctly when creating course.")

    def test_invalidHours(self):
        with self.assertRaises(ValueError,
                               msg="An exception was not raised when createCourse was passed invalid hours."):
            CourseManagement.createCourse(course_id=13, name="Course", location="location", days="M, W, F",
                                          hours="invalid", instructor=self.instructor)

    def test_invalidHoursType(self):
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when createCourse was passed invalid hours type."):
            CourseManagement.createCourse(course_id=14, name="Course", location="location", days="M, W, F", hours=10,
                                          instructor=self.instructor)

    def test_instructor(self):
        self.assertEqual(self.instructor, self.testCourse.instructor,
                         "Course instructor was not set correctly when creating course.")

    def test_invalidInstructor(self):
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when createCourse was passed an instructor of a type "
                                   "other than UserProfile."):
            CourseManagement.createCourse(course_id=15, name="Course", location="location", days="M, W, F", hours=10,
                                          instructor=10)

    def test_invalidInstructor2(self):
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when createCourse was passed a UserProfile of a type "
                                   "other than INSTRUCTOR."):
            CourseManagement.createCourse(course_id=16, name="Course", location="location", days="M, W, F", hours=10,
                                          instructor=self.TA)
            Course.objects.get()

    def test_TA(self):
        self.assertEqual(self.TA, self.testCourse.TAs.all()[0],
                         msg="Course TA was not set correctly when creating course.")

    def test_invalidTA(self):
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when createCourse was passed an invalid TA."):
            CourseManagement.createCourse(course_id=11, name="Course", location="location", days="M, W, F", hours=10,
                                          instructor=self.TA, tas=10)

    def test_invalidTA2(self):
        with self.assertRaises(TypeError, msg="An exception was not raised when createCourse was passed an "
                                              "UserProfile of type other than TA."):
            CourseManagement.createCourse(course_id=11, name="Course", location="location", days="M, W, F", hours=10,
                                          instructor=self.TA, tas=[self.instructor])


class TestEditCourse(TestCase):

    def setUp(self):
        UserProfile(userID=1, userType="INSTRUCTOR", username="instructor", password="password",
                    name="Professor Layton", address="3400 N Maryland Ave", phone="6085555432",
                    email="layton@gmail.com").save()
        UserProfile(userID=99, userType="INSTRUCTOR", username="professor", password="password",
                    name="Phoenix Wright", address="221B Baker Street", phone="6085555432",
                    email="wright@gmail.com").save()
        self.instructor = UserProfile.objects.get(userID=1)
        self.instructor2 = UserProfile.objects.get(userID=99)
        UserProfile(userID=2, userType="TA", username="ta1", password="password", name="Luke",
                    address="2400 S Maryland Ave", phone="4145543212", email="luke@gmail.com").save()
        UserProfile(userID=3, userType="TA", username="ta2", password="password", name="Maya",
                    address="Address", phone="4145543212", email="maya@gmail.com").save()
        self.TA1 = UserProfile.objects.get(userID=2)
        self.TA2 = UserProfile.objects.get(userID=3)

        Course.objects.create(courseID=10, name="Chemistry", location="Location", hours="12:00 PM - 12:50 PM",
                              days="M, W, F", instructor=self.instructor)
        Course.objects.get(courseID=10).TAs.add(self.TA1)
        self.testCourse = Course.objects.get(courseID=10)

    def test_editName(self):
        CourseManagement.editCourse(course_id=self.testCourse.courseID, name="Trigonometry")
        self.assertEqual("Trigonometry", Course.objects.get(courseID=10).name, "Name was not edited correctly.")

    def test_editDays(self):
        CourseManagement.editCourse(course_id=self.testCourse.courseID, days="T, Th")
        self.assertEqual("T, Th", Course.objects.get(courseID=10).days, "Days were not edited correctly.")

    def test_editInstructor(self):
        CourseManagement.editCourse(course_id=10, instructor=self.instructor2)
        self.assertEqual(self.instructor2, Course.objects.get(courseID=10).instructor, "Instructor was not edited correctly.")

    def test_editTA(self):
        CourseManagement.editCourse(course_id=10, tas=[self.TA2])
        print(Course.objects.get(courseID=10).TAs.all())
        self.assertEqual(self.TA2, Course.objects.get(courseID=10).TAs.all()[0], "TA was not edited correctly.")


class TestDeleteCourse(TestCase):
    def setUp(self):
        UserProfile(userID=1, userType="INSTRUCTOR", username="instructor", password="password",
                    name="Professor Layton", address="3400 N Maryland Ave", phone="6085555432",
                    email="layton@gmail.com").save()
        self.instructor = UserProfile.objects.get(userID=1)
        Course.objects.create(courseID=10, name="Chemistry", location="Location", hours="12:00 PM - 12:50 PM",
                              days="M, W, F", instructor=self.instructor)

    def test_delete(self):
        CourseManagement.deleteCourse(course_id=10)
        with self.assertRaises(Course.DoesNotExist, msg="An exception was not raised when createCourse was passed an "
                                                        "invalid TA."):
            Course.objects.get(courseID=10)
