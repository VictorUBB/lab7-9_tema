import unittest

from domain.entities import Student, Disciplina, Grades
from repository.grades_repo import InMemoryRepositoryGrades, RepositoryGradesFile


class TestCaseGrades(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo=InMemoryRepositoryGrades()

    def test_add_grade(self):
        s1 = Student(123, 'Tudor')
        d1 = Disciplina(1111, 'matematica', 'Vasile')
        nota = 7
        grade = Grades(s1.getID(), d1.getId(), nota)
        self.__repo.add_grade(grade)
        self.assertEqual(len(self.__repo.get_grades()),1)

        s1 = Student(123, 'Tudor')
        d2 = Disciplina(4444, 'informatica', 'Andrei')
        nota = 5
        grade = Grades(s1.getID(), d2.getId(), nota)
        self.__repo.add_grade(grade)
        self.assertEqual(len(self.__repo.get_grades()), 2)

class TestCaseGradesFile(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo=RepositoryGradesFile('test_grades_repo.txt')

    def test_add_grade(self):
        self.__repo.clear()
        s1 = Student(123, 'Tudor')
        d1 = Disciplina(1111, 'matematica', 'Vasile')
        nota = 7
        grade = Grades(s1.getID(), d1.getId(), nota)
        self.__repo.add_grade(grade)
        self.assertEqual(len(self.__repo.get_grades()),1)

        s1 = Student(123, 'Tudor')
        d2 = Disciplina(4444, 'informatica', 'Andrei')
        nota = 5
        grade = Grades(s1.getID(), d2.getId(), nota)
        self.__repo.add_grade(grade)
        self.assertEqual(len(self.__repo.get_grades()), 2)
