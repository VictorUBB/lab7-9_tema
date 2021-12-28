from domain.entities import Student, Disciplina, Grades, Statistics
from domain.sort import cocktailSort
from exceptions.exceptions import InexistentGradesException, NoGradesException
from repository.student_repo import InMemoryRepositoryStudent, InMemoryRepositoryDisciplina, InMemoryRepositoryGrades, \
    InMemoryRepositoryStatistics
from domain.validators import StudentValidator, DisciplinaValidator, GradeValidator
import random
import string


class StudentService():
    def __init__(self, repo, validator):
        """
        Initializeaza student service
        :param repo: obiectul repo ce auta la gestionarea studentilor
        :type InMemoryRepositoryStudent
        :param validator: obiectul ce se asigura ce studentul e bun
        :type StudentValidator
        """
        self.__repo = repo
        self.__validator = validator

    def add_students(self, IDStudent, Nume):
        """
        Se adauga un student
        :param IDStudent: Id-ul studentului ce dorim sa-l adaugam
        :type int
        :param Nume:Numele studentului ce  dorim sa-l adauga
        :type str
        :return: studentul adaugat in lista
        :rtype student
        :raise Value error daca studentul nu e bun
        """

        student = Student(IDStudent, Nume)
        self.__validator.validare(student)
        self.__repo.add_students(student)
        return student

    def get_all_students(self):
        """
        Returneaza o lista cu totii studentii
        :return: lista cu toti studentii
        :rtype list de obiecte student
        """
        return self.__repo.get_all_students()

    def get_student(self, value):
        """
        Returneaza un student de pe o pozitie
        :param value: pozitia de unde va fi luat studentul
        :type int
        :return: studentul
        :type student
        """
        return self.__repo.get_student(value)

    def test_generate_students(self):
        """
        Genereaza o lista cu studenti
        :return: lista cu studenti
        :type list
        """
        return self.__repo.generate_students()

    def delete_student(self, position):
        """
        Sterge studentul de pe  pozitia introdusa din lisat
        :param key: Pozitia de unde va fi sters studentul
        :type int
        :return: lista fara student
        :type list
        :raise ValueError daca pozitia nu este buna
        """
        return self.__repo.__delitem__(position)

    def modify_student(self, ID, Nume):
        """
        Modifica numele unui student in functie de un id dat
        :param ID: Id-ul studentului ce vrem sa il modificam
        :type int
        :param Nume:numele studentului ce vrem sa il modificam
        :type str
        :return: studentul modificat
        :rtype Student
        :raise Value Error daca nu exista id-ul introdus
        """
        s = Student(ID, Nume)
        self.__validator.validare(s)
        return self.__repo.modify_student(ID, Nume)

    def find_student(self, ID):
        """
        Cauta un student in functie de id
        :param ID: Id-ul dupa care cautam studentul
        :type int
        :return Studentul cu id-ul introdus
        :rtype Student
        :raise: ValueError daca nu exista id-ul introdus
        """
        return self.__repo.find_student(ID)

    def random_student(self, value):
        """
        Returneaza un numar de studenti random
        :param value: numarul de studenti
        """
        for index in range(value):
            s = self.generate_random_student()
            try:
                self.__validator.validare(s)
                self.__repo.add_students(s)
            except ValueError:
                index -= 1

    def generate_random_student(self):
        """
        Genereaza un obiect de timp student random
        :return: student
        """
        id_s = random.randint(100, 999)
        letters = string.ascii_letters
        nume = ''.join(random.choice(letters) for i in range(9))
        return Student(id_s, nume)

    def sort_students(self):
        list=self.__repo.get_all_students()
        cocktailSort(list,key=lambda x:x.getID())
        for elm in list:
            print(str(elm))



















