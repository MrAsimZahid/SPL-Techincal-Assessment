from user import User
from student import Student
#import courses
from instructor import Professor


if __name__ == "__main__":
    stu = Student('Asim', 'Zahid', '123', "mrasim",
                  '123', 'junior', ['bla', 'Bla', 'BB'])
    # firstName, lastName, password, userName, rollNumber, status, courses
    prof = Professor('Asim', 'Zahid', '123', "mrasim", "Assistant Professor", "Ph.D", ['Data Structures', 'Web Development'])
    # firstName, lastName, password, userName, designation, qualification, courses
    stu.getProfile()
    prof.getProfile()
    
