from domain.entities import Student, Disciplina,Grades
from exceptions.exceptions import ValidationException


class StudentValidator:
    """
    Clasa pentru incapsularea algoritmului de validare a datelor
    """

    def validare(self, student):
        errors = []

        if student.getID() < 100 or student.getID() > 999:
            errors.append("Id-ul studentului nu respecta criterile date")

        if student.getName() == '':
            errors.append("Numele studentului nu poate sa fie nul")

        if len(errors) > 0:
            error_string = '\n'.join(errors)
            raise ValidationException(error_string)


class DisciplinaValidator:
    """
    Clasas pentru a incapsula algoritmul de validare a datelor
    """

    def validare(self, disciplina):
        errors = []
        if type(disciplina.getId()) == str:
            errors.append("Id-ul destinatiei nu poate contine litere")
        elif disciplina.getId() < 1000 or disciplina.getId() > 9999:
            errors.append("Id-ul destinatiei nu respecta criterile date")

        if disciplina.getName() == '':
            errors.append("Numele disciplinei nu poate fi nul")
        if disciplina.getProfesor() == '':
            errors.append("Numele profesorului nu poate vi nul")

        if len(errors) > 0:
            error_string = '\n'.join(errors)
            raise ValidationException(error_string)

class GradeValidator:
    """
    Clasa pentru validarea notelor
    """
    def validate(self,grade):
        errors=[]
        if grade.getGrades()<0 or grade.getGrades()>10:
            errors.append("Nota nu respecta criterile cerute")
        if len(errors) >0:
            error_string = '\n'.join(errors)
            raise ValidationException(error_string)
