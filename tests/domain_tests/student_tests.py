import unittest

from domain.entities import Student
from domain.validators import StudentValidator
from exceptions.exceptions import ValidationException


class TestCaseStudent(unittest.TestCase):
    def setUp(self) -> None:
        self.__validator=StudentValidator()

    def test_create_Student(self):
        S = Student(123, 'Andrei')
        self.assertEqual(S.getID(),123)
        self.assertEqual(S.getName(),'Andrei')

        S.setId(234)
        self.assertEqual(S.getID(),234)

        S.setName('Vlad')
        self.assertEqual(S.getName(),'Vlad')

    def test_StudentValidator(self):
        s = Student(10, '')
        self.assertRaises(ValidationException,self.__validator.validare,s)

        s = Student(1228, 'Andrei')
        self.assertRaises(ValidationException,self.__validator.validare,s)

        s=Student(222,'Vlad')
        self.__validator.validare(s)
