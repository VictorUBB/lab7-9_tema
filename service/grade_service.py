from domain.entities import Grades


class GradesService:
    def __init__(self, stud_repo, disc_repo, repo, grade_validator):
        """
        Initializam grade service
        :param stud_repo: repository-ul pentru studenti
        :param disc_repo: repository-ul pentru disciplina
        :param repo: repository-ul pentru note
        :param grade_validator: validarea pentru note
        """
        self.__student_repo = stud_repo
        self.__discipline_repo = disc_repo
        self.__validator = grade_validator
        self.__repo = repo

    def add_grade(self, IDstudent, IDdisciplina, nota):
        """
        adauga in lista un nou obiect de timp nota
        :param IDstudent: id-ul studentului la care vrem sa adaugam nota
        :type int
        :param IDdisciplina: id-ul disciplinei la care vrem sa adaugam nota
        :type int
        :param nota: nota ce vrem sa o adaugam
        :type int
        :return: obiectul nota
        :rtype grade
        """
        s = self.__student_repo.find_student(IDstudent)
        d = self.__discipline_repo.find_discipline(IDdisciplina)
        grade = Grades(IDstudent, IDdisciplina, nota)
        self.__validator.validate(grade)
        self.__repo.add_grade(grade)
        return grade

    def get_all_grades(self):
        return self.__repo.get_grades()

    def generate_grades(self):
        return self.__repo.generate_grades()

    def most_popular_disc(self):
        """
        Afla id-ul celei mai populare dsicipline
        :return: id-ul disciplinei
        :rtype int
        """
        max = 0
        id_max = 0
        for index in self.__discipline_repo.get_all_disciplines():
            ap = 0
            for disc in self.__repo.get_grades():
                if int(index.getId()) == int(disc.getDiscipline()):
                    ap += 1
            if ap > max:
                max = ap
                id_max = index.getId()
        return id_max

    def students_of_disc(self, id):
        """
        Adauga intr-o lista studenti ce iau parte la o disciplina
        :param id: id-ul disciplinei
        :type int
        :return: lista de sudenti
        :rtype list
        """
        list_of_students = []
        for grade in self.__repo.get_grades():
            if grade.getDiscipline() == id:
                list_of_students.append(grade.getStudent())
        return list_of_students

