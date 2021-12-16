import unittest
from TAScheduler.User.User import User

# NEED MORE FUNCTIONS! Specifically getters and setters.


'''
setId()
setName()
setContact()
setSSN()
setAddress()
setPassword()
setType()
getType()
getId()
getName()
getContact()
getSSN()
getAddress()
getPassword()
'''


class TestMyUser(unittest.TestCase):

    def SetUp(self):

        '''
        testusr0: to be empty at all times.
        testusr1: has every field filled off the bat.
        #ID, name, contact, ssn, address, password, userType (we'll use numerical flags for this)
        testusr2: to be used for all of the "set" functions.
        '''

        testusr0 = User()
        testusr1 = User(1000, "John Wick", 4142542688, 101001001, "894 Lake Street, Milwaukee, Wisconsin 99999",
                        "thisismypassword", 2)
        testusr2 = User()

    def test_getType(self):
        # This user's UserType is 2: Supervisor.
        self.assertEqual(2, self.testusr1.getType())
        self.assertFalse(1, self.testusr1.getType())

        # If a user class is created and a user type is not specified, we should have some sort of negative flag
        # to identify that the user doesn't have a type yet
        self.assertEqual(-1, self.testusr0.getType())

    def test_getId(self):
        # User id is 0001
        self.assertEqual(1000, self.testusr1.getId())
        self.assertFalse(0000, self.testusr1.getId())

        # Similar concept in the test_getType() function, we should have a flag for no id assigned
        self.assertEqual(-1, self.testusr0.getId())
        self.assertFalse(1000, self.testusr0.getId())

    def test_getName(self):
        self.assertEqual("John Wick", self.testusr1.getName())
        self.assertFalse("Tony Danza", self.testusr1.getName())

        self.assertEqual("NA", self.testusr0.getName())
        self.assertFalse("John Wick", self.testusr0.getName())

    def test_getContact(self):
        self.assertEqual(4142542688, self.testusr1.getContact())
        self.assertFalse(9875471111, self.testusr1.getContact())

        self.assertEqual(0000000000, self.testusr0.getContact())
        self.assertFalse(4142542688, self.testusr0.getContact())

    def test_getSSN(self):
        self.assertEqual(101001001, self.testusr1.getSSN())
        self.assertFalse(000000000, self.testusr1.getSSN())

        self.assertEqual(000000000, self.testusr0.getSSN())
        self.assertFalse(101001001, self.testusr0.getSSN())

    def test_getAddress(self):
        self.assertEqual("894 Lake Street, Milwaukee, Wisconsin 99999", self.testusr1.getAddress())
        self.assertFalse("203948203948230jsdlkfjsdlkfjsd", self.testusr1.getAddress())

        self.assertEqual("No Address", self.testusr0.getAddress())
        self.assertFalse("894 Lake Street, Milwaukee, Wisconsin 99999", self.testusr0.getAddress())

    def test_getPassword(self):
        self.assertEqual("thisismypassword", self.testusr1.getPassword())
        self.assertFalse("thisisnotmypassword", self.testusr1.getPassword())

        self.assertEqual("newuser1", self.testusr0.getPassword())
        self.assertFalse("thisismypassword", self.testusr0.getPassword())

    def test_setId(self):
        self.assertEqual(-1, self.testusr2.getId())
        self.testusr2.setId(2000)
        self.assertEqual(2000, self.testusr2.getId())

    def test_setName(self):
        self.assertEqual("No Name", self.testusr2.getName())
        self.testusr2.setName("Gabe Newell")
        self.assertEqual("Gabe Newell", self.testusr2.getName())

    def test_setContact(self):
        self.assertEqual(0000000000, self.testusr2.getContact())
        self.testusr2.setContact(4148675309)
        self.assertEqual(4148675309, self.testusr2.getContact())

    def test_setSSN(self):
        self.assertEqual(000000000, self.testusr2.getSSN())
        self.testusr2.setSSN(1111111111)
        self.assertEqual(111111111, self.testusr2.getSSN())

    def test_setAddress(self):
        self.assertEqual("No Address", self.testusr2.getAddress())
        self.testusr2.setAddress("Fun Land")
        self.assertEqual("Fun Land", self.testusr2.getAddress())

    def test_setPassword(self):
        self.assertEqual("newuser1", self.testusr2.getPassword())
        self.testusr2.setPassword("supersecretpw")
        self.assertEqual("supersecretpw", self.testusr2.getPassword())

    def test_setType(self):
        self.assertEqual(-1, self.testusr2.getType())
        self.testusr2.setType(2)
        self.assertEqual(2, self.testusr2.getType())
