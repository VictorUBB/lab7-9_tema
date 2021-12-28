import unittest

from domain.entities import Student
from domain.sort import SpecialSort
from domain.validators import StudentValidator
from exceptions.exceptions import InexistentIdException
from repository.student_repo import InMemoryRepositoryStudent
from service.student_service import StudentService


class TestCaseStudentService(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = InMemoryRepositoryStudent()
        self.__validator = StudentValidator()
        self.__service = StudentService(self.__repo, self.__validator)

    def test_add_student(self):
        self.__service.test_generate_students()
        self.__service.add_students(678, 'Marian')
        self.assertEqual(self.__service.get_student(10).getID(), 678)
        self.assertEqual(self.__service.get_student(10).getName(), 'Marian')

        self.__service.add_students(676, 'Oana')
        self.assertEqual(self.__service.get_student(11).getID(), 676)
        self.assertEqual(self.__service.get_student(11).getName(), 'Oana')

    def test_delete_student(self):
        self.__service.test_generate_students()
        position = 0
        initial_id = self.__service.get_student(position).getID()
        initial_name = self.__service.get_student(position).getName()
        self.__service.delete_student(position)
        self.assertNotEqual(self.__service.get_student(position).getID(), initial_id)
        self.assertNotEqual(self.__service.get_student(position).getName(), initial_name)

        position1 = 1
        initial_id = self.__service.get_student(position).getID()
        initial_name = self.__service.get_student(position).getName()
        self.__service.delete_student(position1)
        self.assertEqual(self.__service.get_student(position).getID(), initial_id)
        self.assertEqual(self.__service.get_student(position).getName(), initial_name)

    def test_service_modify_student(self):
        self.__service.test_generate_students()
        student_inlocuitor = Student(111, 'Marian')
        self.__service.modify_student(student_inlocuitor.getID(), student_inlocuitor.getName())
        self.assertEqual(self.__service.get_student(0).getID(), 111)
        self.assertEqual(self.__service.get_student(0).getName(), 'Marian')

        initial_student = self.__service.get_student(1)
        student_inlocuitor = Student(121, 'Marian')
        self.assertRaises(InexistentIdException, self.__service.modify_student, student_inlocuitor.getID(),
                          student_inlocuitor.getName())

        self.assertEqual(self.__service.get_student(1).getID(), initial_student.getID())
        self.assertEqual(self.__service.get_student(1).getName(), initial_student.getName())

    def test_service_find_student(self):
        self.__service.test_generate_students()
        id = 111
        test_student = self.__service.find_student(id)
        self.assertEqual(test_student.getID(), 111)
        self.assertEqual(test_student.getName(), 'Tudor')

        id = 122
        test_student = self.__service.find_student(id)
        self.assertEqual(test_student.getID(), 122)
        self.assertEqual(test_student.getName(), 'Ion')

        id = 444
        self.assertRaises(InexistentIdException, self.__service.find_student, id)

    def test_sort(self):
        self.__service.test_generate_students()
        list=SpecialSort(self.__service.get_all_students(),reverse=True,key=self).cocktailSort()
        print(list)