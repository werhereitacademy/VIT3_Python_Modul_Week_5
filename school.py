'''Question 2: Create a "School" class in Python. This class should have the following properties and functionalities:

##### Properties:
- "name" 
- "establishment_year" 
- "students" 
- "teachers"
- 
##### Methods:
- add_new_student(self, student_name, class): A method used to add a new student to the school. It takes the student's name and class, and adds them to the "students" list.
- add_new_teacher(self, teacher_name, subject): A method used to add a new teacher to the school. It takes the teacher's name and subject, and adds them to the "teachers" dictionary.
- display_student_list(self): A method used to display a list of registered students at the school. List the student names and their classes.
- display_teacher_list(self): A method used to display a list of teachers working at the school. List the teacher names and their subjects.
##

'''

# Let's create the school class.

class School:
    def __init__(self, name, establishment_year):
    ## Properties
        self.name = name
        self.establishment_year = establishment_year
    # Create a list to hold the students
        self.students = []
    # Create a list to hold the teachers
        self.teachers = []
        
 # Methods
 
    def add_new_student(self, student_name, class_name):
        self.students.append({"student_name": student_name, "class_name": class_name})
        
    def add_new_teacher(self, teacher_name, subject):
        self.teachers.append({"teacher_name": teacher_name, "subject": subject})
        
    def display_student_list(self):
        print(self.students)
    def display_teacher_list(self):
        print(self.teachers)
        
        
        
school = School("Samanyolu High School", 1998)
school.display_student_list()
school.display_teacher_list()
school.establishment_year
school.name
school.add_new_student("aysima", "11a")
school.display_student_list()
school.add_new_student("suheyb", "12a")
school.display_student_list()

middle_school = School("Inkilap Middle School", 1996)
middle_school.display_student_list()
middle_school.add_new_student("mavis", "7a")
middle_school.add_new_student("sedef", "7b")
middle_school.add_new_student("mehmet", "7c")
middle_school.display_student_list()