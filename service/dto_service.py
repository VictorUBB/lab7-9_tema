from domain.entities import Statistics
from domain.sort import cocktailSort, selectionSort
from exceptions.exceptions import InexistentGradesException


class StatisticsService:
    def __init__(self, repo, grade_repo, student_repo):
        """
        Initializam StatisiticsService
        :param repo: Repository ul pentru Statistics
        :param grade_repo: Repository ul pentru Grades
        :param student_repo: Repository ul pentru Student
        """
        self.__repo = repo
        self.__grade_repo = grade_repo
        self.__student_repo = student_repo

    def get_medii(self):
        """
        :return: toate medile din memorie
        :rtype list
        """
        return self.__repo.get_medii()

    def get_statistics(self, value):
        return self.__repo.get_statistic(value)

    def create_medie_list(self):
        """
        Initializeaza list de Statistica cu mediile fiecarui student si id-ul acestuia daca are macar o nota
        :return:-
        """
        self.__repo.clear()
        val = 0
        for student in self.__student_repo.get_all_students():
            len = 0
            medie = 0
            for grades in self.__grade_repo.get_grades():
                if grades.getStudent() == student.getID():
                    len += 1
                    medie += int(grades.getGrades())
            if len > 0:
                stat = Statistics(student.getName(), float(medie / len))
                self.__repo.add_medie(stat)
                val = 1
            else:
                stat = Statistics(student.getName(), 0)
                self.__repo.add_medie(stat)
        if val == 0:
            raise InexistentGradesException

    def sort_medii(self):
        """
        Ordoneaza descrescator dupa medii lista de statistics
        :return: lista ordonata descrescator
        :rtype list
        """
        list = self.get_medii()
        cocktailSort(list, key=lambda x: x.getMedie(),reverse=True)
        #list.sort(key=Statistics.getMedie, reverse=True)
        return list

    def sort_by_disc(self, disc):
        """
        Initializeaza Statistic cu numele studentilor si notele acestora daca au note la disciplina data
        :param disc: disciplina la care vrem sa gasim studenti
        :return: -
        :raises InexistentGradesException daca nu exista note
        """
        self.__repo.clear()
        val = 0
        grade_list=self.__grade_repo.get_grades()
        for grade in grade_list:
            if int(grade.getDiscipline()) == disc:
                name = self.__student_repo.find_student(int(grade.getStudent()))
                stat = Statistics(name.getName(), grade.getGrades())
                self.__repo.add_medie(stat)
                val = 1
        if val == 0:
            raise InexistentGradesException

    def sort_by_name(self):
        """
        Sorteaza lista de statistici in ordine alfabetica
        :return: lista sortata
        """
        list = self.get_medii()
        selectionSort(list,key=lambda x: x.getStudentName())
        #list.sort(key=Statistics.getStudentName)
        return list

    def __len__(self):
        """
        :return:lungimea listei de statistics
        :rtype int
        """
        return self.__repo.__len__()