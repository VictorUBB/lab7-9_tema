from domain.entities import Student, Disciplina, Grades, Statistics
from exceptions.exceptions import *


class InMemoryRepositoryGrades:
    """
    Clasa ce se ocupa cu memorarea notelor si gestoniarea acestora
    """

    def __init__(self):
        """
        Se creeaza o lista cu toate notele
        """
        self.__grades = []

    def add_grade(self, grade):
        """
        Adauga o nota in lista
        :param grade: Nota ce urmeaza sa fie adaugata
        :type Grades
        """
        self.__grades.append(grade)

    def get_grades(self):
        """
        Returneaza lista cu toate notele
        :return: toate notele
        :rtype list
        """
        return self.__grades

    def generate_grades(self):
        d = Disciplina(1212, 'matematica', 'Alexandru')
        d1 = Disciplina(2592, 'informatica', 'Vasile')
        d2 = Disciplina(1699, 'programare', 'Pop')
        d3 = Disciplina(7234, 'biologie', 'ABC')
        d4 = Disciplina(5433, 'sport', 'XYX')
        s = Student(111, 'Tudor')
        s1 = Student(222, 'Andrei')
        s2 = Student(122, 'Ion')
        s3 = Student(312, 'Vlad')
        s4 = Student(852, 'Victor')
        s5 = Student(733, 'Radu')
        s6 = Student(552, 'Maria')
        s7 = Student(971, 'Alina')
        s8 = Student(345, 'Mara')
        s9 = Student(643, 'Emanuela')
        g = Grades(s1.getID(), d.getId(), 6)
        self.add_grade(g)
        g = Grades(s3.getID(), d2.getId(), 2)
        self.add_grade(g)
        g = Grades(s2.getID(), d1.getId(), 8)
        self.add_grade(g)
        g = Grades(s.getID(), d.getId(), 4)
        self.add_grade(g)
        g = Grades(s1.getID(), d2.getId(), 9)
        self.add_grade(g)
        g = Grades(s1.getID(), d.getId(), 8)
        self.add_grade(g)
        g = Grades(s5.getID(), d3.getId(), 10)
        self.add_grade(g)
        g = Grades(s7.getID(), d4.getId(), 2)
        self.add_grade(g)
        g = Grades(s8.getID(), d.getId(), 5)
        self.add_grade(g)
        g = Grades(s7.getID(), d3.getId(), 7)
        self.add_grade(g)
        g = Grades(s4.getID(), d2.getId(), 1)
        self.add_grade(g)
        g = Grades(s9.getID(), d4.getId(), 6)
        self.add_grade(g)
        g = Grades(s6.getID(), d2.getId(), 5)
        self.add_grade(g)
        g = Grades(s7.getID(), d4.getId(), 6)
        self.add_grade(g)


class RepositoryGradesFile:
    """
    Clasa ce se ocupa cu memorarea notelor si gestoniarea acestora
    """

    def __init__(self, filename):
        """
        Se creeaza o lista cu toate notele
        """
        self.__filename = filename

    def __load_from_file(self):
        try:
            f = open(self.__filename, 'r')
        except IOError:
            raise CorruptetFileException

        grades = []
        lines = f.readlines()
        for line in lines:
            stud_id, disc_id, nota = [grade.strip() for grade in line.split(';')]
            grade = Grades(stud_id, disc_id, nota)
            grades.append(grade)
        f.close()
        return grades

    def __save_to_file(self, grade_list):
        with open(self.__filename, 'w') as f:
            for grade in grade_list:
                grade_str = str(grade.getStudent()) + ';' + str(grade.getDiscipline()) + ';' + str(grade.getGrades())+'\n'
                f.write(grade_str)

    def add_grade(self, grade):
        """
        Adauga o nota in fisier
        :param grade: Nota ce urmeaza sa fie adaugata
        :type Grades
        """
        grade_list = self.__load_from_file()
        grade_list.append(grade)
        self.__save_to_file(grade_list)

    def get_grades(self):
        """
        Returneaza lista cu toate notele
        :return: toate notele
        :rtype list
        """
        return self.__load_from_file()

    def clear(self):
        list=[]
        self.__save_to_file(list)
