# Question 2: Create a "School" class in Python. This class should have the following properties and functionalities:

# Properties:

# "name"
# "establishment_year"
# "students"
# "teachers"
# Methods:

# add_new_student(self, student_name, grade): A method used to add a new student to the school. It takes the student's name and grade and adds them to the "students" list.
# add_new_teacher(self, teacher_name, subject): A method used to add a new teacher to the school. It takes the teacher's name and subject and adds them to the "teachers" dictionary.
# display_student_list(self): A method used to display the list of enrolled students in the school. List the names of the students and their grades.
# display_teacher_list(self): A method used to display the list of teachers working in the school. List the names of the teachers and their subjects.

class School_class:
    def __init__(self,name, establishment_year):
        self.name = name
        self.establishment_year = establishment_year
        self.students = []
        self.teachers = []

    def add_new_student(self, studentName, classes):
        self.students.append({"Student's name":studentName, "Class":classes})
    def add_new_teacher(self, teacherName, branch):
        self.teachers.append({"Teacher's name":teacherName, "Branch:":branch})
    def view_students_list(self):
        return self.students
    def view_teachers_list(self):
        return self.teachers

school = School_class("ABC school", 2002)
school.add_new_student("Beyza Dag", "12")
school.add_new_student("Nur", "11")
school.add_new_teacher("Firat Celik", "Maths")
print(school.view_students_list())
print(school.view_teachers_list())

