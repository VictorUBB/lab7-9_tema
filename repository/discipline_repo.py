from domain.entities import Disciplina
import random
import string
from exceptions.exceptions import *

class InMemoryRepositoryDisciplina:
    """
    Clasa ce se ocupa cu memorarea tuturor disciplinelor si gestoniarea acestora
    """

    def __init__(self):
        """
        Cream o lista cu toate disciplinele
        """
        self.__discipline = []

    def add_disciplines(self, disciplina):
        """
        Se adauga o disciplina noua in lista
        :param disciplina: Noua disciplina
        :type disciplina
        :raise ValueError daca exita alta disciplina cu id-ul dat
        """
        for index in self.__discipline:
            if index.getId() == disciplina.getId():
                raise DuplicateIdException
        self.__discipline.append(disciplina)

    def get_all_disciplines(self):
        """
        Returneaza toate disciplinele introduse pana acuma
        :return: lista cu disciplinele
        :rtype list
        """
        return self.__discipline

    def generate_disciplines(self):
        d = Disciplina(1212, 'matematica', 'Alexandru')
        self.__discipline.append(d)
        d = Disciplina(2592, 'informatica', 'Vasile')
        self.__discipline.append(d)
        d = Disciplina(1699, 'programare', 'Pop')
        self.__discipline.append(d)
        d = Disciplina(7234, 'biologie', 'ABC')
        self.__discipline.append(d)
        d = Disciplina(5433, 'sport', 'XYX')
        self.__discipline.append(d)

    def __delitem__(self, key):
        """
        Sterge un element din lista de discipline
        :param key: pozitia de unde va fi sters numarul
        :type int
        :raise ValueError daca pozitia nu e buna
        """

        if key >= 0 and key < len(self.__discipline):
            del self.__discipline[key]
        else:
            raise InexistentPositionException

    def get_discipline(self, value):
        return self.__discipline[value]

    def modify_discipline(self, Id, Nume, Profesor):
        """
        Modifica elementele unei discipline cu un id dat
        :param Id: id-ul disciplinei ce vrem sa o modificam
        :type int
        :param Nume: Numele inlocuiotor
        :type str
        :param Profesor: profesorul inlocuitor
        :type str
        :return lista cu disciplinele modificata
        :raise ValueError daca exista disciplina cu id-ul dat
        """
        d = self.find_discipline(Id)
        if type(d) == Disciplina:
            d.setName(Nume)
            d.setProfesor(Profesor)
            return d
        raise InexistentIdException
        # for element in self.__discipline:
        #     if element.getId() == Id:
        #         element.setName(Nume)
        #         element.setProfesor(Profesor)

    def find_discipline(self, Id):
        """
        Cauta o disciplina duppa un id
        :param Id: Id -ul disciplinei ce o cautam
        :type int
        :raise ValueError daca nu exista id-ul introdus
        """
        for disc in self.__discipline:
            if disc.getId() == Id:
                return disc
        raise InexistentIdException

class DisciplineRepoFile:
    def __init__(self,filename):
        self.__filename=filename

    def __load_from_file(self):
        try:
            f=open(self.__filename,'r')
        except IOError :
            raise CorruptetFileException

        disc_list=[]
        lines=f.readlines()
        for line in lines:
            disc_id,disc_name,disc_prof=[disc.strip() for disc in line.split(';')]
            discipline=Disciplina(disc_id,disc_name,disc_prof)
            disc_list.append(discipline)
        f.close()
        return disc_list

    def __save_to_file(self,disc_list):
        with open(self.__filename,'w') as f:
            for disc in disc_list:
                string_disc=str(disc.getId())+';'+str(disc.getName())+';'+str(disc.getProfesor())+'\n'
                f.write(string_disc)

    def add_disciplines(self, disciplina):
        """
        Se adauga o disciplina noua in lista
        :param disciplina: Noua disciplina
        :type disciplina
        :raise ValueError daca exita alta disciplina cu id-ul dat
        """
        try:
            self.find_discipline(disciplina.getId())
            raise DuplicateIdException
        except InexistentIdException:
            disc_list=self.__load_from_file()
            disc_list.append(disciplina)
            self.__save_to_file(disc_list)

    def get_all_disciplines(self):
        """
        Returneaza toate disciplinele introduse pana acuma
        :return: lista cu disciplinele
        :rtype list
        """
        return self.__load_from_file()


    def __delitem__(self, key):
        """
        Sterge un element din lista de discipline
        :param key: pozitia de unde va fi sters numarul
        :type int
        :raise ValueError daca pozitia nu e buna
        """
        disc_list = self.__load_from_file()
        disc_list.pop(key)
        self.__save_to_file(disc_list)


    def modify_discipline(self, Id, Nume, Profesor):
        """
        Modifica elementele unei discipline cu un id dat
        :param Id: id-ul disciplinei ce vrem sa o modificam
        :type int
        :param Nume: Numele inlocuiotor
        :type str
        :param Profesor: profesorul inlocuitor
        :type str
        :return lista cu disciplinele modificata
        :raise InexistentIdException daca nu exista disciplina cu id-ul dat
        """
        disc_list = self.__load_from_file()
        disc=self.find_discipline(Id)
        index=self.__find_by_index(disc_list,Id)
        if index>len(disc_list):
            raise InexistentIdException
        disc.setName(Nume)
        disc.setProfesor(Profesor)
        disc_list[index]=disc
        self.__save_to_file(disc_list)

    def __find_by_index(self,disc_list,id):
        """
        Cauta id-ul unei discipline si returneaza pozitia unde e gaseste
        :param disc_list: lista in care cautam
        :type list
        :param id: id-ul cautat
        :type list
        :return: pozitia unde apare id-ul
        """
        if disc_list==[]:
            return 2
        elif int(disc_list[0].getId())==id:
            return 0
        else: return 1+self.__find_by_index(disc_list[1:],id)
        # index=-1
        # for i in range(len(disc_list)):
        #     if int(disc_list[i].getId())==id:
        #         index=i
        # return index

    def find_discipline(self, Id):
        """
        Cauta o disciplina duppa un id
        :param Id: Id -ul disciplinei ce o cautam
        :type int
        :raise ValueError daca nu exista id-ul introdus
        """
        disc_list=self.__load_from_file()
        for disc in disc_list:
            if int(disc.getId()) == int(Id):
                return disc
        raise InexistentIdException

    def generate_disciplines(self):
        list=[]
        d=Disciplina(1212,'matematica','Alexandru')
        list.append(d)
        d=Disciplina(2592,'informatica','Vasile')
        list.append(d)
        d=Disciplina(1699,'programare','Pop')
        list.append(d)
        self.__save_to_file(list)

    def clear(self):
        list=[]
        self.__save_to_file(list)

    def get_discipline(self,position):
        list=self.__load_from_file()
        return list[position]
