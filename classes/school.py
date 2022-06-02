from .person import Person 
from .student import Student
from .staff import Staff 

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.all_staff() 
        self.students = Student.all_students() 







# bob=Staff('bob',30,'Teacher','password',12345)
# bill=Student('bill',12,'Student','password',11111)

