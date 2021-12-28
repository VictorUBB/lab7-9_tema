from domain.entities import Statistics
from exceptions.exceptions import CorruptetFileException


class InMemoryRepositoryStatistics:
    """
    Clasa ce se ocupa cu gestionarea medilor studentilor si memoraraea acestora
    """

    def __init__(self):
        """
        Se creeaza o lista pentru memorarea acestora
        """
        self.__medii = []

    def add_medie(self, medie):
        """
        Adaugarea de medii noi
        :param medie: Studentul si media acestuia
        :typem Statistics
        """
        self.__medii.append(medie)

    def get_medii(self):
        """
        Returneaza toate medile
        :return: toate elementele din lista
        :rtype list
        """
        return self.__medii

    def __len__(self):
        """
        :return: lungimea listei
        """
        return len(self.__medii)

    def get_statistic(self, value):
        return self.__medii[value]

    def clear(self):
        """
        Sterge toate elementele din lista
        """
        self.__medii = []


class FileRepositoryStatistics:

    def __init__(self, filename):
        self.__filename = filename

    def __load_from_file(self):
        try:
            f = open(self.__filename, 'r')
        except IOError:
            raise CorruptetFileException

        date = []
        lines = f.readlines()
        for line in lines:
            nume_std, nota = [data.strip() for data in line.split(';')]
            data = Statistics(nume_std, nota)
            date.append(data)
        f.close()
        return date

    def __save_to_file(self, date_list):
        with open(self.__filename, 'w') as f:
            for data in date_list:
                str_data = str(data.getStudentName()) + ';' + str(data.getMedie())+'\n'
                f.write(str_data)

    def add_medie(self, medie):
        data_list = self.__load_from_file()
        data_list.append(medie)
        self.__save_to_file(data_list)

    def get_medii(self):
        return self.__load_from_file()

    def clear(self):
        data_list = []
        self.__save_to_file(data_list)

    def __len__(self):
        data_list = self.__load_from_file()
        return len(data_list)