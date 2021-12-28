from domain.entities import Student, Disciplina, Grades, Statistics
import random
import string
from exceptions.exceptions import *
from repository.discipline_repo import InMemoryRepositoryDisciplina
from repository.dto_repo import InMemoryRepositoryStatistics
from repository.grades_repo import InMemoryRepositoryGrades


class InMemoryRepositoryStudent:
    """
    Clasa ce se ocupa de memorarea tuturor studentilor si de gestionarea acestora
    """

    def __init__(self):
        """
        Creeam o lista cu toti studenti
        """
        self.__students = []

    def add_students(self, student):
        """
        Se adauga un student nou in lista
        :param student: Un obiect de tip student ce nu este in lista
        :type student
        :raise ValueError daca exista id-ul la alt student
        """
        for index in self.__students:
            if student.getID() == index.getID():
                raise DuplicateIdException
        self.__students.append(student)

    def get_all_students(self):
        return self.__students

    def generate_students(self):
        """
        Initializeaza lista de studenti cu o serie de studenti
        """
        s = Student(111, 'Tudor')
        self.__students.append(s)
        s = Student(222, 'Andrei')
        self.__students.append(s)
        s = Student(122, 'Ion')
        self.__students.append(s)
        s = Student(312, 'Vlad')
        self.__students.append(s)
        s = Student(852, 'Victor')
        self.__students.append(s)
        s = Student(733, 'Radu')
        self.__students.append(s)
        s = Student(552, 'Maria')
        self.__students.append(s)
        s = Student(971, 'Alina')
        self.__students.append(s)
        s = Student(345, 'Mara')
        self.__students.append(s)
        s = Student(643, 'Emanuela')
        self.__students.append(s)

    def __delitem__(self, key):
        """
        Sterge studentul de pe  pozitia introdusa din lisat
        :param key: Pozitia de unde va fi sters studentul
        :type int
        :return: lista fara student
        :type list
        :raise ValueError daca pozitia nu este buna
        """

        if key >= 0 and key < (len(self.__students)):
            del self.__students[key]
        else:
            raise InexistentPositionException

    def get_student(self, value):
        return self.__students[value]

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
        s = self.find_student(ID)
        if type(s) == Student:
            s.setName(Nume)
            return s
        else:
            raise InexistentIdException

    def generate_random_student(self):
        id = random.randint(100, 999)
        letters = string.ascii_letters
        nume = ''.join(random.choice(letters) for i in range(9))
        return Student(id, nume)

    def find_student(self, ID):
        """
        Cauta un student in functie de id
        :param ID: Id-ul dupa care cautam studentul
        :type int
        :return Studentul cu id-ul introdus
        :rtype Student
        :raise: ValueError daca nu exista id-ul introdus
        """
        for student in self.__students:
            if student.getID() == ID:
                return student
        raise InexistentIdException



# class StudentRepoFile(InMemoryRepositoryStudent):
#     def __init__(self,file_name):
#         InMemoryRepositoryStudent.__init__(self)
#         self.__filename=file_name
#         self.__load_from_file()
#
#     def __load_from_file(self):
#         try:
#             f=open(self.__filename,'r')
#         except IOError:
#             raise CorruptetFileException()
#
#         lines=f.readlines()
#         for line in lines:
#             stud_id,stud_name=[stud.strip() for stud in line.split(';')]
#             student=Student(stud_id,stud_name)
#             InMemoryRepositoryStudent.add_students(self,student)
#         f.close()
#
#     def __save_to_file(self):
#         stud_list=InMemoryRepositoryStudent.get_all_students(self)
#         with open(self.__filename,'w') as f:
#             for stud in stud_list:
#                 stud_string=str(stud.getID())+';'+str(stud.getName())+'\n'
#                 f.write(stud_string)
#
#     def add_students(self, student):
#         """
#         Se adauga un student nou in lista
#         :param student: Un obiect de tip student ce nu este in lista
#         :type student
#         :raise ValueError daca exista id-ul la alt student
#         """
#         InMemoryRepositoryStudent.add_students(self,student)
#         self.__save_to_file()
#
#     def get_all_students(self):
#         return InMemoryRepositoryStudent.get_all_students(self)
#
#     def modify_student(self, ID, Nume):
#         """
#         Modifica numele unui student in functie de un id dat
#         :param ID: Id-ul studentului ce vrem sa il modificam
#         :type int
#         :param Nume:numele studentului ce vrem sa il modificam
#         :type str
#         :return: studentul modificat
#         :rtype Student
#         :raise Value Error daca nu exista id-ul introdus
#         """
#         modified= InMemoryRepositoryStudent.modify_student(self, ID, Nume)
#         self.__save_to_file()
#         return modified
#
#
#     def find_student(self, ID):
#         """
#         Cauta un student in functie de id
#         :param ID: Id-ul dupa care cautam studentul
#         :type int
#         :return Studentul cu id-ul introdus
#         :rtype Student
#         :raise: ValueError daca nu exista id-ul introdus
#         """
#         return InMemoryRepositoryStudent.find_student(self,ID)
#
#     def __delitem__(self, key):
#         """
#         Sterge studentul de pe  pozitia introdusa din lisat
#         :param key: Pozitia de unde va fi sters studentul
#         :type int
#         :return: lista fara student
#         :type list
#         :raise ValueError daca pozitia nu este buna
#         """
#         delete=InMemoryRepositoryStudent.__delitem__(key)
#         self.__save_to_file()
#         return delete

class StudentRepoInFile:
    def __init__(self,file_name):
        self.__filename=file_name

    def __load_from_file(self):
        try:
            f=open(self.__filename,'r')
        except IOError:
            raise CorruptetFileException()
        students=[]
        lines=f.readlines()
        for line in lines:
            stud_id,stud_name=[stud.strip() for stud in line.split(';')]
            stud=Student(stud_id,stud_name)
            students.append(stud)
        f.close()
        return students

    def __save_to_file(self,stud_list):
        with open(self.__filename,'w') as f:
            for stud in stud_list:
                stud_string=str(stud.getID())+';'+str(stud.getName())+'\n'
                f.write(stud_string)

    def add_students(self, student):
        """
        Se adauga un student nou in lista
        :param student: Un obiect de tip student ce nu este in lista
        :type student
        :raise VDuplicateIdException daca exista id-ul la alt student
        """

        try:
            self.find_student(student.getID())
            raise DuplicateIdException
        except InexistentIdException:
            stud_list = self.__load_from_file()
            stud_list.append(student)
            self.__save_to_file(stud_list)

    def get_all_students(self):
        return self.__load_from_file()

    def modify_student(self, ID, Nume):
        """
        Modifica numele unui student in functie de un id dat
        :param ID: Id-ul studentului ce vrem sa il modificam
        :type int
        :param Nume:numele studentului ce vrem sa il modificam
        :type str
        :raise InexistentIdException daca nu exista id-ul introdus
        """
        stud_list=self.__load_from_file()
        index=self.__find_by_index(stud_list,ID)
        if index>len(stud_list):
            raise InexistentIdException
        student=self.find_student(ID)
        student.setName(Nume)
        stud_list[index]=student
        self.__save_to_file(stud_list)


    def __find_by_index(self,stud_list,id):
        """
        Cauta id-ul unui student si returneaza pozitia la care apare
        :param stud_list:lista cu studenti
        :param id: id-ul cautat
        :return: pozitia unde apare id-ul
        """
        if stud_list==[]:
            return 2
        elif int(stud_list[0].getID())==id:
            return 0
        else:
            return 1+self.__find_by_index(stud_list[1:],id)
        # index=-1
        # for i in range(len(stud_list)):
        #     if int(stud_list[i].getID())==id:
        #          index=i
        # return index

    def find_student(self, ID):
        """
        Cauta un student in functie de id
        :param ID: Id-ul dupa care cautam studentul
        :type :int
        :return Studentul cu id-ul introdus
        :rtype Student
        :raise: InexistentIdException daca nu exista id-ul introdus
        """

        stud_list=self.get_all_students()
        for stud in stud_list:
            if int(stud.getID())==int(ID):
                return stud
        raise InexistentIdException


    def __delitem__(self, key):
        """
        Sterge studentul de pe  pozitia introdusa din lisat
        :param key: Pozitia de unde va fi sters studentul
        :type int
        """
        stud_list=self.__load_from_file()
        stud_list.pop(key)
        self.__save_to_file(stud_list)

    def generate_students(self):
        list=[]
        s=Student(111,'Tudor')
        list.append(s)
        s=Student(222,'Andrei')
        list.append(s)
        s=Student(122,'Ion')
        list.append(s)
        s = Student(312,'Vlad')
        list.append(s)
        self.__save_to_file(list)

    def clear(self):
        """
        Sterge toate elementele din fisiser
        :return:
        """
        list=[]
        self.__save_to_file(list)

    def get_student(self,index):
        """
        Returneaza studentul de la o pozitie din fisier
        :param index: pozitia cautata
        :type int
        :return: studentul
        :rtype Student
        """
        list=self.__load_from_file()
        return list[index]










