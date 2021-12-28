import unittest

from domain.entities import Statistics


class TestCaseStatistics(unittest.TestCase):
    def test_create_Statistics(self):
        S = Statistics('Vlad', 6)
        self.assertEqual(S.getStudentName(),'Vlad')
        self.assertEqual(S.getMedie(),6)

        S = Statistics('Andrei', 7.01)
        self.assertEqual(S.getStudentName(),'Andrei')
        self.assertEqual(S.getMedie(),7.01)
