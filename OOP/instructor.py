from user import User
from assignment import Assignment


# implement getters and setters

class Professor(User):
    def __init__(self, firstName, lastName, password, userName, designation, qualification, courses):
        super().__init__(firstName, lastName, password, userName)
        self.designation = designation
        self.qualification = qualification
        self.courses = courses

    def getProfile(self):
        """
        View instructor profile 
        """
        print("{} is {} at LUMS".format(self.firstName + ' ' + self.lastName, self.designation))

    def viewRoster(self, courseCode):
        """
        View roster 
        """
        roster = self.getCourse(courseCode).roster
        print("following is the roster for course {}".format(courseCode))
        for person in roster:
            print(person.firstName + " " + person.lastName)
    
    def getCourse(self, courseCode):
        for course in self.courses:
            if course.courseCode == courseCode:
                return course
    
    def viewResources(self, courseCode):
        resources = self.getCourse(courseCode).resouces
        print("following are resouces for course {}".format(courseCode))
        for resource in resources:
            print(resource.name)

    def addResource(self, courseCode, name):
        """
        Add assignment resources
        """
        for course in self.courses:
            if course.courseCode == courseCode:
                course.resouces.append(name)

    def viewAssignments(self, courseCode):
        """
        """
        print("following are assignments for course {}".format(courseCode))
        assignments = self.getCourse(courseCode).assignments
        print("Name | Due Date | total Marks")
        for assignment in assignments:
            print("{} | {} | {}".format(assignment.name, assignment.dueDate, assignment.totalMarks))

    def addAssignment(self, courseCode, aname='', tmarks=0, ddate=''):
        """
        """
        for course in self.courses:
            if course.courseCode == courseCode:
                course.assignments.append(Assignment(name = aname, dueDate = ddate, totalMarks = tmarks))

    def viewMarks(self, sRoll, smarks, courseCode):
        """
        View Marks
        """
        print("marks of student {} for course {}".format(sRoll, courseCode))
        assignments = self.getCourse(courseCode).assignments
        print("Name | Due Date | obtained marks | total Marks")
        for assignment in assignments:
            print("{} | {} | {} | {}".format(assignment.name, assignment.dueDate, assignment.getStudentMarks(sRoll), assignment.totalMarks))

    def addMarks(self, courseCode, assignmentName, omarks, sroll):
        """
        """
        for course in self.courses:
            if course.courseCode == courseCode:
                for assignment in course.assignments:
                    if assignment.name == assignmentName:
                        assignment.addStudentsMarks([sroll],[omarks])