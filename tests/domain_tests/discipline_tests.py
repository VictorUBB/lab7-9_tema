import unittest

from domain.entities import Disciplina
from domain.validators import DisciplinaValidator
from exceptions.exceptions import ValidationException


class TestCaseDiscipline(unittest.TestCase):
    def setUp(self) -> None:
        self.__validator=DisciplinaValidator()

    def test_create_Disciplina(self):
        D = Disciplina(333, 'informatica', 'Andrei')
        self.assertEqual(D.getName(),'informatica')
        self.assertEqual(D.getId(),333)
        self.assertEqual(D.getProfesor(),'Andrei')

        D.setID(222)
        self.assertEqual(D.getId(),222)
        D.setName('matematica')
        self.assertEqual(D.getName(),'matematica')
        D.setProfesor('Alex')
        self.assertEqual(D.getProfesor(),'Alex')

    def test_DisciplinaValidator(self):

        d = Disciplina(100, 'matematica', 'Ion')
        self.assertRaises(ValidationException,self.__validator.validare,d)

        d = Disciplina(1001, '', 'Ion')
        self.assertRaises(ValidationException, self.__validator.validare, d)

        d = Disciplina('1234', 'matematica', 'Ion')
        self.assertRaises(ValidationException,self.__validator.validare,d)

        d = Disciplina(1234, 'matematica', 'Ion')
        self.__validator.validare(d)
