import unittest

from domain.entities import Student, Disciplina, Grades
from domain.validators import GradeValidator
from exceptions.exceptions import ValidationException


class TestCaseGrades(unittest.TestCase):
    def setUp(self) -> None:
        self.__validator=GradeValidator()

    def test_create_Grade(self):
        S = Student(123, 'Andrei')
        D = Disciplina(333, 'informatica', 'Andrei')
        G = Grades(S, D, 8)
        self.assertEqual(G.getStudent(),S)
        self.assertEqual(G.getDiscipline(),D)
        self.assertEqual(G.getGrades(),8)


        G.setGrade(4)
        self.assertEqual(G.getStudent(),S)
        self.assertEqual(G.getDiscipline(),D)
        self.assertEqual(G.getGrades(),4)

    def test_GradeValidator(self):
        s1 = Student(123, 'Tudor')
        d1 = Disciplina(1111, 'matematica', 'Vasile')
        nota = 12
        grade = Grades(s1, d1, nota)
        self.assertRaises(ValidationException,self.__validator.validate,grade)