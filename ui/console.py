from termcolor import colored
import random
from exceptions.exceptions import *

class Console:
    def __init__(self, stud_service, disc_service, grade_service, stat_service,menu_option):
        self.__stud_service = stud_service
        self.__disc_service = disc_service
        self.__grade_service = grade_service
        self.__stat_service = stat_service
        self.__option=menu_option

    def __show_all_students(self):
        """
        Afiseaza toti studenti adaugati
        :return:
        """
        students = self.__stud_service.get_all_students()
        if len(students) > 0:
            print("Studenti actuali sunt :")
            for index in students:
                print(colored(str(index), 'blue'))
        else:
            print(colored("Nu exista studenti introdusi", 'red'))

    def __add_students(self):
        try:
            ID = int(input("Introduceti id-ul studentului : "))
            Nume = input("Introduceti numele studentului")
        except ValueError:
            print(colored("Introduceti id numeric", 'red'))

        try:
            student = self.__stud_service.add_students(ID, Nume)
            print("Studentul ", student, " a fost adaugat cu succes")
        except ValidationException as ve:
            print(colored(str(ve), 'red'))
        except DuplicateIdException as ve:
            print(colored(str(ve), 'red'))

    def __delete_student(self):
        try:
            position = int(input("Introduceti pozitia de unde doriti sa stergeti studentul"))
        except ValueError:
            print(colored("Introduceti pozitie numerica", 'red'))
        try:
            self.__stud_service.delete_student(position)
        except InexistentPositionException as ve:
            print(colored(str(ve), 'red'))

    def __delete_discipline(self):
        try:
            position = int(input("Introduceti pozitia de unde doriti sa stergeti disciplina"))
        except ValueError:
            print(colored("Pozitia nu este buna", 'red'))

        try:
            self.__disc_service.delete_discipline(position)
        except InexistentPositionException as ve:
            print(colored(str(ve), 'red'))

    def __show_discipline(self):
        """
        Afiseaza totate disciplinele adaugate
        :return:
        """
        disciplina = self.__disc_service.get_all_disciplines()
        if len(disciplina) > 0:
            print("Disciplinele actuale sunt: ")
            for index in disciplina:
                print(colored(str(index), 'blue'))
        else:
            print(colored("Nu exista discipline introduse ", 'red'))

    def __add_disciplina(self):
        try:
            ID = int(input("Introduceti id-ul disciplinei"))
            nume = input("Introduceti numele disciplinei")
            profesor = input("Introduceti profesorul")
        except ValueError:
            print(colored("Introduceti id numeric", 'red'))

        try:
            disciplina = self.__disc_service.add_disciplina(ID, nume, profesor)
            print("Disciplina ", disciplina, "a fost adaugata cu succes")
        except ValidationException as ve:
            print(colored(str(ve), 'red'))
        except DuplicateIdException as ve:
            print(colored(str(ve), 'red'))


    def __modify_student(self):
        try:
            ID = int(input("Introduceti id-ul studentului : "))
            Nume = input("Introduceti numele inlocuitor")

        except ValueError:
            print(colored("Introduceti id numeric", 'red'))
        try:
            self.__stud_service.modify_student(ID, Nume)
        except InexistentIdException as ve:
            print(colored(str(ve), 'red'))

    def __modify_discipline(self):
        try:
            ID = int(input("Introduceti id-ul disciplinei : "))
            Nume = input("Introduceti numele disciplinei inlocuitoare :")
            Profesor = input("Introduceti numele profesorului inlocuitor :")

        except ValueError:
            print(colored("Introduceti id numeric", 'red'))

        try:
            self.__disc_service.modify_discipline(ID, Nume, Profesor)
        except InexistentIdException as ve:
            print(colored(str(ve), 'red'))

    def __find_student(self):
        try:
            Id = int(input("Introduceti id-ul studentului cautat"))
        except ValueError:
            print(colored("Introduceti id numeric", 'red'))
        try:
            print(self.__stud_service.find_student(Id))
        except InexistentIdException as ve:
            print(colored(str(ve), 'red'))

    def __find_discipline(self):
        try:
            id = int(input("Introduceti id-ul disciplinei cautate"))
        except ValueError:
            print(colored("Introduceti id numeric", 'red'))
        try:
            print(self.__disc_service.find_discipline(id))
        except InexistentIdException as ve:
            print(colored(str(ve), 'red'))

    def __add_grade(self):
        try:
            id_student = int(input("Introduceti id-ul studentului "))
            id_disc = int(input("Introduceti id-ul disciplinei "))
            nota = int(input("Introduceti nota"))
        except ValueError:
            print("Introduceti valori numerice")
        try:
            self.__grade_service.add_grade(id_student, id_disc, nota)
        except ValidationException as ve:
            print(colored(str(ve), 'red'))

    def __show_grades(self):
        for index in self.__grade_service.get_all_grades():
            print(colored(str(index), 'blue'))

    def __random_student(self):
        value = random.randint(1, 10)
        self.__stud_service.random_student(value)

    def __statistic_of_medie(self):
        try:
            self.__stat_service.create_medie_list()
            nr = int(len(self.__stat_service) / 5)
            for index in range(nr):
                print("Studentul ",self.__stat_service.sort_medii()[index].getStudentName() , "are media ", self.__stat_service.sort_medii()[index].getMedie())
        except NoGradesException as ve:
            print(colored(str(ve), 'red'))

    def __sort(self):
        try:
            disc = int(input("Introduceti id-ul disciplinei dorite :"))
        except ValueError:
            print(colored("Introduceti id numeric", 'red'))
        try:
            self.__stat_service.sort_by_disc(disc)
            sorted_list = self.__stat_service.sort_medii()
            sorted_list = self.__stat_service.sort_by_name()
            for index in sorted_list:
                print(str(index))
        except InexistentGradesException as ve:
            print(colored(str(ve), 'red'))

    def __popular_disc(self):
        try:
            id=self.__grade_service.most_popular_disc()
            print("Cea mai populara disciplina este :",self.__disc_service.find_discipline(id))
            print("Studenti ce iau parte la aceasta disciplina sunt:")
            for student in self.__grade_service.students_of_disc(id):
                print(str(self.__stud_service.find_student( student) ))
        except InexistentIdException as ve:
            print(colored(str(ve), 'red'))

    def sort__stud(self):
        self.__stud_service.sort_students()
    def show_ui(self):
        if self.__option==1:
            self.__stud_service.test_generate_students()
            self.__disc_service.generate_disciplines()
            self.__grade_service.generate_grades()
        while True:
            print("Optiunile dumneavoastra sunt : ")
            print(colored("Adaugare", 'cyan'))
            print("  Adaugare student")
            print("  Adaugare discplina")
            print("  Adauga nota")
            print(colored("Afisare", 'cyan'))
            print("  Afisare studenti")
            print("  Afisare discpline")
            print("  Afisare note")
            print(colored("Stergere", 'cyan'))
            print("  Sterge student")
            print("  Sterge disciplina")
            print(colored("Modificare", 'cyan'))
            print("  Modifica student")
            print("  Modifica disciplina")
            print(colored("Cautare", 'cyan'))
            print("  Cauta student")
            print("  Cauta disciplina")
            print(colored("Statistica top", 'magenta'))
            print(colored("Statistica disciplina", 'magenta'))
            print(colored("Statistica populara", 'magenta'))
            print(colored("Ghid", 'magenta'))
            print(colored("Iesi", 'magenta'))
            option = input("Optiunea dumneavoastra este:")
            if option.lower() == 'adauga student':
                self.__add_students()
            elif option.lower() == 'afisare studenti':
                self.__show_all_students()
            elif option.lower() == 'adauga disciplina':
                self.__add_disciplina()
            elif option.lower() == 'afisare discipline':
                self.__show_discipline()
            elif option.lower() == 'sterge student':
                self.__delete_student()
            elif option.lower() == 'sterge disciplina':
                self.__delete_discipline()
            elif option.lower() == 'modifica student':
                self.__modify_student()
            elif option.lower() == 'modifica disciplina':
                self.__modify_discipline()
            elif option.lower() == 'cauta student':
                self.__find_student()
            elif option.lower() == 'cauta disciplina':
                self.__find_discipline()
            elif option.lower() == 'adauga nota':
                self.__add_grade()
            elif option.lower() == 'afisare note':
                self.__show_grades()
            elif option.lower() == 'random student':
                self.__random_student()
            elif option.lower() == 'sort':
                self.__sort()
            elif option.lower() == 'statistica':
                self.__statistic_of_medie()
            elif option.lower()=='popular':
                self.__popular_disc()
            elif option.lower()=='iesi':
                return False
            elif option.lower() == 'ghid':
                print("     Pt. afisare : 'afisare' + studenti/disciplina/note")
                print("     Pt. adaugare: 'adauga' + student/disciplina/nota")
                print("     Pt. stergere: 'sterge' + student/disciplina")
                print("     Pt. modificare: 'modifica' + student/disciplina")
                print("     Pt. cautare: 'cauta' + student/disciplina")
                print("     Pt. sortare la o disciplina: 'sort'")
                print("     Pt. cele mai marii medii: 'statistica'")
                print("     Pt. cea mai populara disciplina: 'popular'")
            else:
                print(colored("Inputul este gresit", 'red'))
