import unittest

from domain.entities import Disciplina
from exceptions.exceptions import InexistentIdException
from repository.discipline_repo import InMemoryRepositoryDisciplina, DisciplineRepoFile


class TestCaseDisciplineRepo(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = InMemoryRepositoryDisciplina()

    def test_all_disciplines(self):
        d1 = Disciplina(1111, 'matematica', 'Vasile')
        self.__repo.add_disciplines(d1)
        self.assertEqual(len(self.__repo.get_all_disciplines()), 1)

        d2 = Disciplina(4444, 'informatica', 'Andrei')
        self.__repo.add_disciplines(d2)
        self.assertEqual(len(self.__repo.get_all_disciplines()), 2)

    def test_delitem_disc(self):
        self.__repo.generate_disciplines()
        position = 0
        initial_id = self.__repo.get_discipline(position).getId()
        initial_Name = self.__repo.get_discipline(position).getName()
        initial_profesor = self.__repo.get_discipline(position).getProfesor()
        self.__repo.__delitem__(position)
        self.assertNotEqual(initial_id, self.__repo.get_discipline(position).getId())
        self.assertNotEqual(initial_Name, self.__repo.get_discipline(position).getName())
        self.assertNotEqual(initial_profesor, self.__repo.get_discipline(position).getProfesor())

    def test_find_discipline(self):
        self.__repo.generate_disciplines()
        id = 1699
        d = self.__repo.find_discipline(id)
        self.assertEqual(d.getId(), 1699)
        self.assertEqual(d.getName(), 'programare')
        self.assertEqual(d.getProfesor(), 'Pop')

        id = 1111
        self.assertRaises(InexistentIdException, self.__repo.find_discipline, id)

    def test_modify_discipline(self):
        self.__repo.generate_disciplines()
        discipline_inlocuitor = Disciplina(1699, 'logica', 'Maria')
        self.__repo.modify_discipline(discipline_inlocuitor.getId(), discipline_inlocuitor.getName(),
                                      discipline_inlocuitor.getProfesor())
        self.assertEqual(self.__repo.get_discipline(2).getId(), discipline_inlocuitor.getId())
        self.assertEqual(self.__repo.get_discipline(2).getName(), discipline_inlocuitor.getName())
        self.assertEqual(self.__repo.get_discipline(2).getProfesor(),discipline_inlocuitor.getProfesor())

        initial_discipline = self.__repo.get_discipline(1)
        discipline_inlocuitor = Disciplina(1679, 'logica', 'Maria')
        self.assertRaises(InexistentIdException, self.__repo.modify_discipline, discipline_inlocuitor.getId(),
                          discipline_inlocuitor.getName(),
                          discipline_inlocuitor.getProfesor())

        self.assertEqual(self.__repo.get_discipline(1).getId(), initial_discipline.getId())
        self.assertEqual(self.__repo.get_discipline(1).getName(), initial_discipline.getName())
        self.assertEqual(self.__repo.get_discipline(1).getProfesor(),initial_discipline.getProfesor())

class TestCaseDisciplineFile(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo=DisciplineRepoFile('test_discipline_repo.txt')

    def test_all_disciplines(self):
        self.__repo.clear()
        d1 = Disciplina(1111, 'matematica', 'Vasile')
        self.__repo.add_disciplines(d1)
        self.assertEqual(len(self.__repo.get_all_disciplines()), 1)

        d2 = Disciplina(4444, 'informatica', 'Andrei')
        self.__repo.add_disciplines(d2)
        self.assertEqual(len(self.__repo.get_all_disciplines()), 2)

    def test_delitem_disc(self):
        self.__repo.generate_disciplines()
        position = 0
        initial_id = self.__repo.get_discipline(position).getId()
        initial_Name = self.__repo.get_discipline(position).getName()
        initial_profesor = self.__repo.get_discipline(position).getProfesor()
        self.__repo.__delitem__(position)
        self.assertNotEqual(initial_id, self.__repo.get_discipline(position).getId())
        self.assertNotEqual(initial_Name, self.__repo.get_discipline(position).getName())
        self.assertNotEqual(initial_profesor, self.__repo.get_discipline(position).getProfesor())

    def test_find_discipline(self):
        self.__repo.generate_disciplines()
        id = 1699
        d = self.__repo.find_discipline(id)
        self.assertEqual(int(d.getId()), 1699)
        self.assertEqual(d.getName(), 'programare')
        self.assertEqual(d.getProfesor(), 'Pop')

        id = 1111
        self.assertRaises(InexistentIdException, self.__repo.find_discipline, id)

    def test_modify_discipline(self):
        self.__repo.generate_disciplines()
        discipline_inlocuitor = Disciplina(1699, 'logica', 'Maria')
        self.__repo.modify_discipline(discipline_inlocuitor.getId(), discipline_inlocuitor.getName(),
                                      discipline_inlocuitor.getProfesor())
        self.assertEqual(int(self.__repo.get_discipline(2).getId()), discipline_inlocuitor.getId())
        self.assertEqual(self.__repo.get_discipline(2).getName(), discipline_inlocuitor.getName())
        self.assertEqual(self.__repo.get_discipline(2).getProfesor(),discipline_inlocuitor.getProfesor())

        initial_discipline = self.__repo.get_discipline(1)
        discipline_inlocuitor = Disciplina(1679, 'logica', 'Maria')
        self.assertRaises(InexistentIdException, self.__repo.modify_discipline, discipline_inlocuitor.getId(),
                          discipline_inlocuitor.getName(),
                          discipline_inlocuitor.getProfesor())

        self.assertEqual(self.__repo.get_discipline(1).getId(), initial_discipline.getId())
        self.assertEqual(self.__repo.get_discipline(1).getName(), initial_discipline.getName())
        self.assertEqual(self.__repo.get_discipline(1).getProfesor(),initial_discipline.getProfesor())
