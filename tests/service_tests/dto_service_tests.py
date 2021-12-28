import unittest

from domain.entities import Disciplina
from repository.dto_repo import InMemoryRepositoryStatistics
from repository.grades_repo import InMemoryRepositoryGrades
from repository.student_repo import InMemoryRepositoryStudent
from service.dto_service import StatisticsService


class TestCaseDTOService(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = InMemoryRepositoryStatistics()
        self.__grade_repo = InMemoryRepositoryGrades()
        self.__stud_repo = InMemoryRepositoryStudent()
        self.__service = StatisticsService(self.__repo, self.__grade_repo, self.__stud_repo)

    def test_create_medii(self):
        self.__stud_repo.generate_students()
        self.__grade_repo.generate_grades()
        self.__service.create_medie_list()
        self.assertEqual(len(self.__service.get_medii()), 10)

    def test_sort_medii(self):
        self.__stud_repo.generate_students()
        self.__grade_repo.generate_grades()
        self.__service.create_medie_list()
        self.__service.sort_medii()
        self.assertGreaterEqual(self.__service.get_statistics(0).getMedie(),
                                self.__service.get_statistics(1).getMedie())
        self.assertGreaterEqual(self.__service.get_statistics(1).getMedie(),
                                self.__service.get_statistics(2).getMedie())
        self.assertGreaterEqual(self.__service.get_statistics(2).getMedie(),
                                self.__service.get_statistics(3).getMedie())
        self.assertGreaterEqual(self.__service.get_statistics(3).getMedie(),
                                self.__service.get_statistics(4).getMedie())
        self.assertGreaterEqual(self.__service.get_statistics(4).getMedie(),
                                self.__service.get_statistics(5).getMedie())
        self.assertGreaterEqual(self.__service.get_statistics(5).getMedie(),
                                self.__service.get_statistics(6).getMedie())
        self.assertGreaterEqual(self.__service.get_statistics(6).getMedie(),
                                self.__service.get_statistics(7).getMedie())
        self.assertGreaterEqual(self.__service.get_statistics(7).getMedie(),
                                self.__service.get_statistics(8).getMedie())
        self.assertGreaterEqual(self.__service.get_statistics(8).getMedie(),
                                self.__service.get_statistics(9).getMedie())


