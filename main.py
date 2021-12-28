# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from domain.entities import Disciplina, Student

from domain.validators import StudentValidator, DisciplinaValidator, \
    GradeValidator
from repository.discipline_repo import DisciplineRepoFile
from repository.dto_repo import FileRepositoryStatistics
from repository.grades_repo import RepositoryGradesFile
from repository.student_repo import InMemoryRepositoryStudent, \
    InMemoryRepositoryDisciplina, \
    InMemoryRepositoryGrades, InMemoryRepositoryStatistics, StudentRepoInFile
from service.discipline_service import DisciplinaService
from service.dto_service import StatisticsService
from service.grade_service import GradesService
from service.student_service import StudentService

from ui.console import Console

print("1. Memorie")
print("2. Fisiere text")
opt = int(input("Alegeti optiunea de savare a datelor:"))
if opt == 1:
    stud_validation = StudentValidator()
    stud_repo = InMemoryRepositoryStudent()
    stud_service = StudentService(stud_repo, stud_validation)

    disc_validation = DisciplinaValidator()
    disc_repo = InMemoryRepositoryDisciplina()
    disc_service = DisciplinaService(disc_repo, disc_validation)

    grade_repo = InMemoryRepositoryGrades()
    grade_validator = GradeValidator()
    grade_service = GradesService(stud_repo, disc_repo, grade_repo, grade_validator)

    stat_repo = InMemoryRepositoryStatistics()
    stat_service = StatisticsService(stat_repo, grade_repo, stud_repo)
elif opt == 2:
    stud_validation = StudentValidator()
    stud_repo = StudentRepoInFile('data/students.txt')
    stud_service = StudentService(stud_repo, stud_validation)

    disc_validation = DisciplinaValidator()
    disc_repo = DisciplineRepoFile('data/discipline.txt')
    disc_service = DisciplinaService(disc_repo, disc_validation)

    grade_repo = RepositoryGradesFile('data/grades.txt')
    grade_validator = GradeValidator()
    grade_service = GradesService(stud_repo, disc_repo, grade_repo, grade_validator)

    stat_repo = FileRepositoryStatistics('data/dto.txt')
    stat_service = StatisticsService(stat_repo, grade_repo, stud_repo)

ui = Console(stud_service, disc_service, grade_service, stat_service, opt)
ui.show_ui()
