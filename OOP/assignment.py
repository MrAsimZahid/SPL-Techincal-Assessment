class Assignment:
    """
    Assignment class
    """

    def __init__(self, name='', studentsMarks={}, dueDate='', totalMarks=0):
        self.name = name
        self._studentMarks = studentsMarks
        self.dueDate = dueDate
        self.totalMarks = totalMarks

    def getStudentMarks(self, rollNumber):
        """
        Get student marks on assignment
        """
        return self.studentsMarks.get(rollNumber)

    def addStudentsMarks(self, sroll=[], smarks=[]):
        """
        Add or update student assignment marks 
        """
        self._studentMarks.update(dict(zip(sroll, smarks)))
