import unittest

from domain.entities import Student
from exceptions.exceptions import InexistentIdException
from repository.student_repo import InMemoryRepositoryStudent, StudentRepoInFile


class TestCaseStudentRepo(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo=InMemoryRepositoryStudent()

    def test_all_students(self):
        s1 = Student(123, 'Tudor')
        self.__repo.add_students(s1)
        self.assertEqual(len(self.__repo.get_all_students()),1)

        s2 = Student(456, 'Andrei')
        self.__repo.add_students(s2)
        self.assertEqual(len(self.__repo.get_all_students()),2)

    def test_delitem(self):
        self.__repo.generate_students()
        position = 0
        initial_id = self.__repo.get_student(position).getID()
        initial_name =  self.__repo.get_student(position).getName()
        self.__repo.__delitem__(position)
        self.assertNotEqual(self.__repo.get_student(position).getID(),initial_id)
        self.assertNotEqual(self.__repo.get_student(position).getName(), initial_name)

        position1 = 1
        initial_id = self.__repo.get_student(position).getID()
        initial_name = self.__repo.get_student(position).getName()
        self.__repo.__delitem__(position1)
        self.assertEqual(self.__repo.get_student(position).getID(),initial_id)
        self.assertEqual(self.__repo.get_student(position).getName(), initial_name)

    def test_modify_student(self):
        self.__repo.generate_students()
        student_inlocuitor = Student(111, 'Marian')
        self.__repo.modify_student(student_inlocuitor.getID(), student_inlocuitor.getName())
        self.assertEqual(self.__repo.get_student(0).getID(),111)
        self.assertEqual(self.__repo.get_student(0).getName(),'Marian')

        initial_student = self.__repo.get_student(1)
        student_inlocuitor = Student(121, 'Marian')
        self.assertRaises(InexistentIdException,self.__repo.modify_student,student_inlocuitor.getID(), student_inlocuitor.getName())

        self.assertEqual(self.__repo.get_student(1).getID(),initial_student.getID())
        self.assertEqual(self.__repo.get_student(1).getName(),initial_student.getName())

    def test_find_students(self):

        self.__repo.generate_students()
        id = 111
        test_student = self.__repo.find_student(id)
        self.assertEqual(test_student.getID(),111)
        self.assertEqual(test_student.getName(),'Tudor')

        id = 122
        test_student = self.__repo.find_student(id)
        self.assertEqual(test_student.getID(),122)
        self.assertEqual(test_student.getName(),'Ion')


        id = 444
        self.assertRaises(InexistentIdException,self.__repo.find_student,id)

class TestCaseStudentFile(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo=StudentRepoInFile('test_student_repo.txt')

    def test_all_students_file(self):
        self.__repo.clear()
        s1 = Student(123, 'Tudor')
        self.__repo.add_students(s1)
        self.assertEqual(len(self.__repo.get_all_students()),1)

        s2 = Student(456, 'Andrei')
        self.__repo.add_students(s2)
        self.assertEqual(len(self.__repo.get_all_students()),2)


    def test_delitem(self):
        self.__repo.generate_students()
        position = 0
        initial_id = int(self.__repo.get_student(position).getID())
        initial_name =  self.__repo.get_student(position).getName()
        self.__repo.__delitem__(position)
        self.assertNotEqual(int(self.__repo.get_student(position).getID()),initial_id)
        self.assertNotEqual(self.__repo.get_student(position).getName(), initial_name)

        position1 = 1
        initial_id = int(self.__repo.get_student(position).getID())
        initial_name = self.__repo.get_student(position).getName()
        self.__repo.__delitem__(position1)
        self.assertEqual(int(self.__repo.get_student(position).getID()),initial_id)
        self.assertEqual(self.__repo.get_student(position).getName(), initial_name)

    def test_modify_student(self):
        self.__repo.generate_students()
        student_inlocuitor = Student(111, 'Marian')
        self.__repo.modify_student(student_inlocuitor.getID(), student_inlocuitor.getName())
        self.assertEqual(int(self.__repo.get_student(0).getID()),111)
        self.assertEqual(self.__repo.get_student(0).getName(),'Marian')

        initial_student = self.__repo.get_student(1)
        student_inlocuitor = Student(121, 'Marian')
        self.assertRaises(InexistentIdException,self.__repo.modify_student,student_inlocuitor.getID(), student_inlocuitor.getName())

        self.assertEqual(self.__repo.get_student(1).getID(),initial_student.getID())
        self.assertEqual(self.__repo.get_student(1).getName(),initial_student.getName())

    def test_find_students(self):

        self.__repo.generate_students()
        id = 111
        test_student = self.__repo.find_student(id)
        self.assertEqual(int(test_student.getID()),111)
        self.assertEqual(test_student.getName(),'Tudor')

        id = 122
        test_student = self.__repo.find_student(id)
        self.assertEqual(int(test_student.getID()),122)
        self.assertEqual(test_student.getName(),'Ion')


        id = 444
        self.assertRaises(InexistentIdException,self.__repo.find_student,id)
