from user import User

class Student(User):
    """
    Child Student class
    """
    #STATUS = ['freshman', 'sophomore', 'junior', 'senior']

    def __init__(self, firstName, lastName, password, userName, rollNumber, status, courses):
        super().__init__(firstName, lastName, password, userName)
        self.rollNumber = rollNumber
        if status.lower() in ['freshman', 'sophomore', 'junior', 'senior']:
            self.status = status
        else:
            print("incorrect status can only be  freshman, sophomore, junior or senior")
            self.courses = courses

    def getProfile(self):
        """
        Get student profile
        """
        print("{} is a {} student at LUMS".format(self.firstName + ' ' + self.lastName, self.status))

    def getCourse(self, courseCode):
        """
        Get student courses
        """
        for course in self.courses:
            if course.courseCode == courseCode:
                return course

    def viewResources(self, courseCode):
        """
        View resources uploaded by instructor
        """
        resources = self.getCourse(courseCode).resouces
        print("following are resouces for course {}".format(courseCode))
        for resource in resources:
            print(resource.name)

    def viewRoster(self, courseCode):
        """
        View roster of a course (list of students enrolled in a course + instructor(s) offering that course)
        """
        roster = self.getCourse(courseCode).roster
        print("following is the roster for course {}".format(courseCode))
        for person in roster:
            print(person.firstName + " " + person.lastName)

    def viewAssignments(self, courseCode):
        """
        View Assignments of a course
        """
        print("following are assignments for course {}".format(courseCode))
        assignments = self.getCourse(courseCode).assignments
        print("Name | Due Date | obtained marks | total Marks")
        for assignment in assignments:
            print("{} | {}| | {}".format(assignment.name, assignment.dueDate,
                                            assignment.getStudentMarks(self.rollNumber), assignment.totalMarks))
