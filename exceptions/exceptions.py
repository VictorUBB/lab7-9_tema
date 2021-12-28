class StudentsUniversityException(Exception):
    pass


class ValidationException(StudentsUniversityException):
    def __init__(self, msg):
        self.__error_msg = msg

    def getMsg(self):
        return self.__error_msg

    def __str__(self):
        return 'Validation Exception:' + str(self.__error_msg)


class RepositoryException(StudentsUniversityException):
    def __init__(self,msg):
       self.__error_msg=msg

    def getMsg(self):
        return self.__error_msg

    def __str__(self):
        return 'Repository Exception:' + str(self.__error_msg)

class DuplicateIdException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self,"ID existent deja")

class InexistentPositionException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self,"Pozitia nu este buna")

class InexistentIdException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self,"ID-ul nu exista")

class InexistentGradesException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self,"Nu exista note la disciplina ")
class NoGradesException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self,"Nu exista note")

class CorruptetFileException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self,"Fisierul nu poate fi deschis")