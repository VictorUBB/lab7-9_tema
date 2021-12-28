class Student:
    def __init__(self, IDStudent, Nume):
        """
        Initializam un obiect de tip student cu valorile date
        :param IDStudent: Id-ul studentului
        :type int(>0)
        :param nume: Numele studentului
        :type str
        """
        self.__ID = IDStudent
        self.__name = Nume

    def getName(self):
        return self.__name

    def getID(self):
        return self.__ID

    def setName(self, value):
        self.__name = value

    def setId(self, value):
        self.__ID = value

    def __str__(self):
        return "IDStudent:" + str(self.__ID) + " ;Nume:" + str(self.__name)


class Disciplina:
    def __init__(self, IDdisciplina, Nume, Profesor):
        """
        Initializam un obiect de tip disciplina cu valori date
        :param IDdisciplina: Id-ul disciplinei
        :type int
        :param Nume:numele disciplinei
        :type str
        :param Profesor: numele profesorului
        :type str
        """
        self.__ID = IDdisciplina
        self.__name = Nume
        self.__Profesor = Profesor

    def getId(self):
        return self.__ID

    def getName(self):
        return self.__name

    def getProfesor(self):
        return self.__Profesor

    def setID(self, value):
        self.__ID = value

    def setName(self, value):
        self.__name = value

    def setProfesor(self, value):
        self.__Profesor = value

    def __str__(self):
        return "IdDisciplina:" + str(self.__ID) + " ;Nume:" + str(self.__name) + " ;Profesor :" + str(self.__Profesor)


class Grades:
    def __init__(self, student_id, discipline, nota):
        """
        Initializam un obiect de tip notaa
        :param student_id: studentul ce a obtinut nota
        :type Student
        :param discipline:dsiciplina la care a obtinut nota
        :type Disciplina
        :param nota: nota obtinuta
        :type int
        """
        self.__student_id = student_id
        self.__discipline_id = discipline
        self.__grade_id = nota

    def getStudent(self):
        return self.__student_id

    # def getStudentName(self):
    #     return self.__student_id.getName()

    def getDiscipline(self):
        return self.__discipline_id

    def getGrades(self):
        return self.__grade_id

    def setStudent(self, student):
        self.__student_id = student

    def setDiscipline(self, discipline):
        self.__discipline_id = discipline

    def setGrade(self, grade):
        self.__grade_id = grade

    def __str__(self):
        return "Studentul :" + str(self.__student_id) + " la disciplina :" + str(self.__discipline_id) + " are nota :" + str(
            self.__grade_id)


class Statistics:
    """
    Clasa pentru a creea obiecte de timp statistics, cu rol in creeare de staatistici privind media studentilor
    """

    def __init__(self, nume, medie):
        """
        Initializam obiectul de tip Statistics
        :param nume: id-ul studentului caruia ii alocam media
        :type int
        :param medie: media studentului
        :type float
        """
        self.__nume_student = nume
        self.__medie = medie

    def getStudentName(self):
        return self.__nume_student

    def getMedie(self):
        return self.__medie

    def __str__(self):
        return "Studentul " + str(self.__nume_student) + " are media " + str(self.__medie)
