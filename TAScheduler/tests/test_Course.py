from django.test import TestCase
from django.test import Client
from TAScheduler.NonDjangoClasses.course_lab_management.CourseManagement import CourseManagement
from TAScheduler.models import Course
from TAScheduler.models import UserProfile


# createCourse(courseName, courseTime, courseDays, courseHours, courseInstructor, courseTA)
# editCourse(courseName, courseTime, courseDays, courseHours, courseInstructor, courseTA)
# deleteCourse(courseName)
# populateSearchClass(searchPromp)  should change class to course
# displayAllCourse()

class TestCreateCourse(TestCase):

    def setUp(self):
        self.instructor = UserProfile
        self.TA = UserProfile
        CourseManagement.createCourse("001", "Calculus", "Physics 137", "M, W, F", "12:00 PM - 12:50 PM",
                                      self.instructor, self.TA, "Section 800")
        self.testCourse = Course.objects.get(courseName="Calculus")

    #     don't have the course location or a course ID when course is created.
    # course time at 12:00pm is in the wrong spot, no lab is assigned to the course

    def test_courseID(self):
        self.assertEqual("001", self.testCourse.getCourseID(), "Course ID was not set correctly when creating course.")

    def test_invalidCourseID(self):
        with self.assertRaises(ValueError,
                               msg="An exception was not raised when courseID passed invalid ID."):
            CourseManagement.createCourse("001", "Calculus", "Physics 137", "M, W, F", "12:00 PM - 12:50 PM",
                                          self.instructor, self.TA, "Section 800")

    def test_courseName(self):
        self.assertEqual("Calculus", self.testCourse.getCourseName(), "Course name was not set correctly when "
                                                                      "creating course.")

    def test_invalidCourseName(self):
        with self.assertRaises(ValueError,
                               msg="An exception was not raised when createCourse passed an invalid Course Name."):
            CourseManagement.createCourse("001", "Calculus", "Physics 137", "M, W, F", "12:00 PM - 12:50 PM",
                                          self.instructor, self.TA, "Section 800")

    def test_courseLocation(self):
        self.assertEqual("Physics 137", self.testCourse.getCourseLocation(),
                         "Course location was not set correctly when "
                         "creating the course")

    def test_invalidCourseLocation(self):
        with self.assertRaises(ValueError,
                               msg="An exception was not raised when createCourse passed an invalid Course Location."):
            CourseManagement.createCourse("001", "Calculus", "Physics 137", "M, W, F", "12:00 PM - 12:50 PM",
                                          self.instructor, self.TA, "Section 800")

    def test_courseDays(self):
        self.assertEqual("M, W, F", self.testCourse.getCourseDays(), "Course days were not set correctly when "
                                                                     "creating course.")

    def test_invalidDays(self):
        with self.assertRaises(ValueError,
                               msg="An exception was not raised when createCourse was passed invalid days."):
            CourseManagement.createCourse("001", "Calculus", "Physics 137", "M, W, F", "12:00 PM - 12:50 PM",
                                          self.instructor, self.TA, "Section 800")

    def test_courseHours(self):
        self.assertEqual("12:00 PM - 12:50 PM", self.testCourse.getCourseHours(), "Course hours were not set "
                                                                                  "correctly when creating course.")

    def test_invalidHours(self):
        with self.assertRaises(ValueError,
                               msg="An exception was not raised when createCourse was passed invalid hours."):
            CourseManagement.createCourse("001", "Calculus", "Physics 137", "M, W, F", "12:00 PM - 12:50 PM",
                                          self.instructor, self.TA, "Section 800")

    def test_instructor(self):
        self.assertEqual(self.instructor, self.testCourse.getCourseInstructor(), "Course instructor was not set "
                                                                                 "correctly when creating course.")

    def test_invalidInstructor(self):
        with self.assertRaises(TypeError, msg="An exception was not raised when createCourse was passed an "
                                              "invalid instructor"):
            CourseManagement.createCourse("001", "Calculus", "Physics 137", "M, W, F", "12:00 PM - 12:50 PM",
                                          self.instructor, self.TA, "Section 800")

    def test_TA(self):
        self.assertEqual(self.TA, self.testCourse.getCourseTa(),
                         "Course TA was not set correctly when creating course.")

    def test_invalidTA(self):
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when createCourse was passed an invalid TA."):
            CourseManagement.createCourse("001", "Calculus", "Physics 137", "M, W, F", "12:00 PM - 12:50 PM",
                                          self.instructor, self.TA, "Section 800")

    def test_Labs(self):
        self.assertEqual(self.Labs, self.testCourse.getCourseLabs(),
                         "Course Labs were not set correctly when creating course.")

    def test_invalidLabs(self):
        with self.assertRaises(TypeError,
                               msg="An exception was not raised when createCourse was passed an invalid Lab."):
            CourseManagement.createCourse("001", "Calculus", "Physics 137", "M, W, F", "12:00 PM - 12:50 PM",
                                          self.instructor, self.TA, "Section 800")


class TestEditCourse(TestCase):

    def setUp(self):
        self.instructor = UserProfile
        self.instructor2 = UserProfile
        self.TA = UserProfile
        self.TA2 = UserProfile
        # Course for invalid inputs
        Course(courseID="001", courseName="Calculus", courseLocation="Physics 137", courseDays="M, W, F",
               courseHours="12:00 PM - 12:50 PM",
               courseInstructor=self.instructor, courseTA=self.TA, courseLabs="Section 800").save()
        # Course for editName
        Course(courseID="002", courseName="Computer Programming", courseLocation="Physics 135", courseDays="T, Th",
               courseHours="1:00 PM - 1:50 PM",
               courseInstructor=self.instructor2, courseTA=self.TA2, courseLabs="Section 801").save()
        # Course for everything else
        Course(courseID="003", courseName="History", courseLocation="Physics 133", courseDays="M, T, W",
               courseHours="2:00 PM - 2:50 PM",
               courseInstructor=self.instructor, courseTA=self.TA, courseLabs="Section 803").save()

    def test_editID(self):
        historyCourse = Course.objects.get(courseName="History")
        CourseManagement.editCourse(historyCourse, courseID="003")
        self.assertEqual("003", historyCourse.courseID, "ID was not edited correctly.")

    def test_invalidID(self):
        mathCourse = Course.objects.get(courseName="Calculus")
        with self.assertRaises(ValueError,
                               msg="An exception was not raises when editCourse was passed an invalid ID."):
            CourseManagement.editCourse(mathCourse, courseID="Invalid")
        self.assertEqual("001", mathCourse.courseID, "editCourse changed courseID when it shouldn't have.")

    def test_editName(self):
        computerCourse = Course.objects.get(courseName="Computer Programming")
        CourseManagement.editCourse(computerCourse, courseName="Computer Programming")
        self.assertEqual("Computer Programming", computerCourse.name, "Name was not edited correctly.")

    def test_invalidName(self):
        mathCourse = Course.objects.get(courseName="Calculus")
        with self.assertRaises(ValueError,
                               msg="An exception was not raises when editCourse was passed an invalid Name."):
            CourseManagement.editCourse(mathCourse, courseName="Invalid")
        self.assertEqual("Calculus", mathCourse.name, "editCourse changed courseName when it shouldn't have.")

    def test_editLocation(self):
        historyCourse = Course.objects.get(courseName="History")
        CourseManagement.editCourse(historyCourse, courseLocation="Physics 101")
        self.assertEqual("Physics 101", historyCourse.courseLocation, "Location was not edited correctly.")

    def test_invalidLocation(self):
        mathCourse = Course.objects.get(courseName="Calculus")
        with self.assertRaises(ValueError,
                               msg="An exception was not raises when editCourse was passed an invalid location."):
            CourseManagement.editCourse(mathCourse, courseLocation="Invalid")
        self.assertEqual("Physics 137", mathCourse.courseLocation, "editCourse changed courseLocation"
                                                                   " when it shouldn't have.")

    def test_editDays(self):
        historyCourse = Course.objects.get(courseName="History")
        CourseManagement.editCourse(historyCourse, courseDays="S, Su")
        self.assertEqual("S, Su", historyCourse.courseDays, "Days were not edited correctly.")

    def test_invalidDays(self):
        mathCourse = Course.objects.get(courseName="Calculus")
        with self.assertRaises(ValueError, msg="An exception was not raised when editCourse was passed bad days."):
            CourseManagement.editCourse(mathCourse, courseDays="Invalid")
        self.assertEqual("M, W, F", mathCourse.courseDays, "editCourse changed courseDays when they shouldn't have.")

    def test_editHours(self):
        historyCourse = Course.objects.get(courseName="History")
        CourseManagement.editCourse(historyCourse, courseHours="3:00 - 3:50 PM")
        self.assertEqual("3:00 - 3:50 PM", historyCourse.courseHours, "Hours were not edited correctly.")

    def test_invalidHours(self):
        mathCourse = Course.objects.get(courseName="Calculus")
        with self.assertRaises(ValueError, msg="An exception was not raised when editCourse was passed bad hours."):
            CourseManagement.editCourse(mathCourse, courseHours="Invalid")
        self.assertEqual("12:00 PM - 12:50 PM", mathCourse.courseDays, "editCourse changed courseHours when they "
                                                                       "shouldn't have.")

    def test_editInstructor(self):
        historyCourse = Course.objects.get(courseName="History")
        CourseManagement.editCourse(historyCourse, courseInstructor=self.instructor2)
        self.assertEqual(self.instructor2, historyCourse.courseInstructor, "Instructor was not edited correctly.")

    def test_invalidInstructor(self):
        mathCourse = Course.objects.get(courseName="Calculus")
        with self.assertRaises(TypeError, msg="A TypeError was not raised when editCourse was passed an invalid type "
                                              "for courseInstructor."):
            CourseManagement.editCourse(mathCourse, courseInstructor="TotallyAnInstructorIPromise")
        self.assertEqual(self.instructor, mathCourse.courseInstructor, "editCourse changed instructor when it "
                                                                       "shouldn't have.")

    def test_editTA(self):
        historyCourse = Course.objects.get(courseName="History")
        CourseManagement.editCourse(historyCourse, courseTA=self.TA2)
        self.assertEqual(self.TA2, historyCourse.courseTA, "TA was not edited correctly.")

    def test_invalidTA(self):
        mathCourse = Course.objects.get(courseName="Calculus")
        with self.assertRaises(TypeError,
                               msg="A TypeError was not raised when editCourse was passed an invalid type for courseTA."):
            CourseManagement.editCourse(mathCourse, courseTA="TotallyATAIPromise")
        self.assertEqual(self.TA, mathCourse.TA,
                         "editCourse changed TA when it shouldn't have.")

    def test_editLabs(self):
        historyCourse = Course.objects.get(courseName="History")
        CourseManagement.editCourse(historyCourse, courseLabs="Section 804")
        self.assertEqual("Section 805", historyCourse.courseTA, "Lab was not edited correctly.")

    def test_invalidLabs(self):
        mathCourse = Course.objects.get(courseName="Calculus")
        with self.assertRaises(ValueError,
                               msg="editCourse change courseLabs when they shouldn't have changed course Labs."):
            CourseManagement.editCourse(mathCourse, courseLabs="Invalid")
        self.assertEqual("Section 800", mathCourse.courseLabs,
                         "editCourse changed Course Labs when it shouldn't have.")


class TestDeleteCourse(TestCase):
    def setUp(self):
        self.instructor = UserProfile
        self.TA = UserProfile
        Course(courseName="Art", courseTime="12:00 PM", courseDays="M, W, F", courseHours="12:00 PM - 12:50 PM",
               courseInstructor=self.instructor, courseTA=self.TA).save()

    def test_delete(self):
        oldCourse = Course.objects.get(courseName="Art")
        CourseManagement.deleteCourse(oldCourse)
        self.assertEqual(None, oldCourse, "Course was not deleted successfully.")


class TestPopulateSearch(TestCase):
    def setUp(self):
        self.instructor = UserProfile
        self.TA = UserProfile

    def test_populate_search(self):
        oldCourse = Course.objects.get(courseName="Art")
        CourseManagement.deleteCourse(oldCourse)
        self.assertEqual(None, oldCourse, "Course was not deleted successfully.")


class TestInputErrorChecker(TestCase):
    def setUp(self):
        self.instructor = UserProfile
        self.TA = UserProfile

    def test_input_error_checker(self):
        oldCourse = Course.objects.get(courseName="Art")
        CourseManagement.deleteCourse(oldCourse)
        self.assertEqual(None, oldCourse, "Course was not deleted successfully.")


class TestDisplayCourses(TestCase):
    def setUp(self):
        self.instructor = UserProfile
        self.TA = UserProfile

    def test_display_courses(self):
        oldCourse = Course.objects.get(courseName="Art")
        CourseManagement.deleteCourse(oldCourse)
        self.assertEqual(None, oldCourse, "Course was not deleted successfully.")
