import unittest

from domain.entities import Disciplina
from domain.validators import DisciplinaValidator
from exceptions.exceptions import InexistentIdException
from repository.discipline_repo import InMemoryRepositoryDisciplina
from service.discipline_service import DisciplinaService


class TestCaseDisciplineService(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = InMemoryRepositoryDisciplina()
        self.__validator = DisciplinaValidator()
        self.__service = DisciplinaService(self.__repo, self.__validator)

    def test_add_disciplines(self):
        self.__service.add_disciplina(1111, 'matematica', 'Vasile')
        self.assertEqual(len(self.__service.get_all_disciplines()), 1)

        self.__service.add_disciplina(4444, 'informatica', 'Andrei')
        self.assertEqual(len(self.__service.get_all_disciplines()), 2)

    def test_delete_disciplines(self):
        self.__service.generate_disciplines()
        position = 0
        initial_id = self.__service.get_disciplina(position).getId()
        initial_Name = self.__service.get_disciplina(position).getName()
        initial_profesor = self.__service.get_disciplina(position).getProfesor()
        self.__service.delete_discipline(position)
        self.assertNotEqual(initial_id, self.__service.get_disciplina(position).getId())
        self.assertNotEqual(initial_Name, self.__service.get_disciplina(position).getName())
        self.assertNotEqual(initial_profesor, self.__service.get_disciplina(position).getProfesor())

    def test_service_modify_discipline(self):
        self.__service.generate_disciplines()
        discipline_inlocuitor = Disciplina(1699, 'logica', 'Maria')
        self.__service.modify_discipline(discipline_inlocuitor.getId(), discipline_inlocuitor.getName(),
                                         discipline_inlocuitor.getProfesor())
        self.assertEqual(self.__service.get_disciplina(2).getId(), discipline_inlocuitor.getId())
        self.assertEqual(self.__service.get_disciplina(2).getName(), discipline_inlocuitor.getName())
        self.assertEqual(self.__service.get_disciplina(2).getProfesor(), discipline_inlocuitor.getProfesor())

        initial_discipline = self.__service.get_disciplina(1)
        discipline_inlocuitor = Disciplina(1679, 'logica', 'Maria')
        self.assertRaises(InexistentIdException, self.__service.modify_discipline, discipline_inlocuitor.getId(),
                          discipline_inlocuitor.getName(),
                          discipline_inlocuitor.getProfesor())

        self.assertEqual(self.__service.get_disciplina(1).getId(), initial_discipline.getId())
        self.assertEqual(self.__service.get_disciplina(1).getName(), initial_discipline.getName())
        self.assertEqual(self.__service.get_disciplina(1).getProfesor(), initial_discipline.getProfesor())

    def test_service_find_discipline(self):
        self.__service.generate_disciplines()
        id = 1699
        d = self.__service.find_discipline(id)
        self.assertEqual(d.getId() , 1699)
        self.assertEqual(d.getName() , 'programare')
        self.assertEqual(d.getProfesor() , 'Pop')

        id = 1111
        self.assertRaises(InexistentIdException,self.__service.find_discipline,id)
