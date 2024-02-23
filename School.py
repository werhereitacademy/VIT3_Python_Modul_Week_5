"""Question2: Create a "School" class in Python. This class should have the following features and functionality:

Features:
"name"
"foundation_year"
"students"
"teachers"
Methods:
add_new_student(self, student_name, class): A method used to add a new student to the school.
It takes the student's name and class and adds it to the "students" list.
add new_teacher(self, teacher_name, branch): A method used to add a new teacher to the school.
It takes the teacher's name and major and adds it to the "teachers" dictionary.
display_student_list(self): A method used to display the list of students enrolled in the school.
List student names and classes.
display_teacher_list(self): A method used to display the list of teachers working at the school.
List teacher names and majors."""

class School:
    def __init__(self, name, foundation_year):
        self.name = name
        self.foundation_year = foundation_year
        self.students_list = []
        self.teachers_dict = {}

    def add_new_student(self):
        student_name = input("Please enter the student's name: ")
        class1 = input("Please enter the student's class: ")
        self.students_list.append({student_name: class1})

    def add_new_teacher(self):
        teacher_name = input("Please enter the teacher's name: ")
        branch = input("Please enter the teacher's branch: ")
        self.teachers_dict[teacher_name] = branch

    def display_student_list(self):
        print(f"Students in {self.name} school:")
        for student in self.students_list:
            for student_name, grade in student.items():
                print(f"{student_name} - Class: {grade}")

    def display_teacher_list(self):
        print(f"Teachers in {self.name} school:")
        for teacher, branch in self.teachers_dict.items():
            print(f"{teacher} - Branch: {branch}")


school = School("Altay", "2024")
while True:

    choice = input(
        "≀~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~≀" +
        "\n≀   Press 1 to add a new student                      ≀" +
        "\n≀   Press 2 to add a new teacher                      ≀" +
        "\n≀   Press 3 to display students                       ≀" +
        "\n≀   Press 4 to display teachers                       ≀" +
        "\n≀   Press 5 to exit                                   ≀" +
        "\n≀                                                     ≀" +
        "\n≀~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~≀")


    if choice == "1":
        school.add_new_student()
    elif choice == "2":
        school.add_new_teacher()
    elif choice == "3":
        school.display_student_list()
    elif choice == "4":
        school.display_teacher_list()
    elif choice == "5":
        break
