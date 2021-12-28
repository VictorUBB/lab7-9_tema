import unittest

from domain.entities import Statistics
from repository.dto_repo import InMemoryRepositoryStatistics


class TestCaseDTORepo(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo=InMemoryRepositoryStatistics()

    def test_add_medie(self):
        s = Statistics(111, 5)
        self.__repo.add_medie(s)
        self.assertEqual( len(self.__repo), 1)

        s = Statistics(122, 9)
        self.__repo.add_medie(s)
        self.assertEqual( len(self.__repo) , 2)