from domain.entities import Disciplina


class DisciplinaService():
    def __init__(self, repo, validator):
        """
        Initializeaza disciplina service
        :param repo: obiectul de tip repo ce ne auta la gestionarea disciplinelor
        :type InMemoryRepositoryDisciplina
        :param validator: Obiectul ce se ocupa de validarea disciplinei
        :type DisciplinaValidator
        """
        self.__repo = repo
        self.__validator = validator

    def add_disciplina(self, IDdisciplina, Nume, Profesor):
        """
        Se adauga o disciplina noua in lista
        :param IDdisciplina: Id-ul disciplinei
        :type int
        :param Nume:Numele disciplinei
        :type str
        :param Profesor Numele profesorului:
        :type str
        :return: disciplina ca obiect de tip discplina
        :raise Value error daca disciplina nu e buna
        """
        disciplina = Disciplina(IDdisciplina, Nume, Profesor)
        self.__validator.validare(disciplina)
        self.__repo.add_disciplines(disciplina)
        return disciplina

    def get_all_disciplines(self):
        """
        Returneaza toate disciplinele introduse pana acuma
        :return: lista cu disciplinele
        :rtype list
        """
        return self.__repo.get_all_disciplines()

    def generate_disciplines(self):
        return self.__repo.generate_disciplines()

    def delete_discipline(self, position):
        """
        Sterge un element de pe o pozitie data
        :param position: pozia de unde va fi stearsa disciplina
        :type int
        :return:lista fara disciplina stearsa
        :rtype list
        """
        return self.__repo.__delitem__(position)

    def get_disciplina(self, position):
        return self.__repo.get_discipline(position)

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
        d = Disciplina(Id, Nume, Profesor)
        self.__validator.validare(d)
        return self.__repo.modify_discipline(Id, Nume, Profesor)

    def find_discipline(self, Id):
        """
        Cauta o disciplina dupa un id
        :param Id: Id -ul disciplinei ce o cautam
        :type int
        :raise ValueError daca nu exista id-ul introdus
        """
        return self.__repo.find_discipline(Id)
