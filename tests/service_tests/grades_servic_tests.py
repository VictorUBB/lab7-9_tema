import unittest

from domain.entities import Student, Disciplina
from domain.validators import GradeValidator
from exceptions.exceptions import ValidationException, InexistentIdException
from repository.discipline_repo import InMemoryRepositoryDisciplina
from repository.grades_repo import InMemoryRepositoryGrades
from repository.student_repo import InMemoryRepositoryStudent
from service.grade_service import GradesService


class TestCaseGradeService(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = InMemoryRepositoryGrades()
        self.__validator = GradeValidator()
        self.__stud_repo = InMemoryRepositoryStudent()
        self.__disc_repo = InMemoryRepositoryDisciplina()
        self.__service = GradesService(self.__stud_repo, self.__disc_repo, self.__repo, self.__validator)

    def test_service_add_grades(self):
        s1 = Student(123, 'Tudor')
        self.__stud_repo.add_students(s1)
        d1 = Disciplina(1111, 'matematica', 'Vasile')
        self.__disc_repo.add_disciplines(d1)
        nota = 7
        self.__service.add_grade(s1.getID(), d1.getId(), nota)
        self.assertEqual(len(self.__service.get_all_grades()), 1)

        s1 = Student(123, 'Tudor')
        d2 = Disciplina(4444, 'informatica', 'Andrei')
        self.__disc_repo.add_disciplines(d2)
        nota = 5
        self.__service.add_grade(s1.getID(), d2.getId(), nota)
        self.assertEqual(len(self.__service.get_all_grades()), 2)

        nota = 12
        self.assertRaises(ValidationException, self.__service.add_grade, s1.getID(), d2.getId(), nota)

    def test_student_of_disc(self):
        self.__service.generate_grades()
        id = 1212
        test_list = self.__service.students_of_disc(id)
        self.assertEqual(len(test_list), 4)

        id = 1699
        test_list = self.__service.students_of_disc(id)
        self.assertEqual(len(test_list), 4)

        id = 5433
        test_list = self.__service.students_of_disc(id)
        self.assertEqual(len(test_list), 3)

    def test_most_popular_disc(self):
        self.__service.generate_grades()
        self.__disc_repo.generate_disciplines()
        test_id=self.__service.most_popular_disc()
        self.assertEqual(test_id,1212)