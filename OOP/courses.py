class Course:
    """
    Courses class
    """
	def __init__(self, courseName, ccode, offeringsch, capacity, instructors, students, resources):
		self.courseName = courseName
		self.courseCode = courseCode
		self.offeringSchool = offeringsch
		self.capacity = capacity
		self.instructors = instructors
		self.resources = resources
		self.roster = self.instructors + students
		self.assignments = []