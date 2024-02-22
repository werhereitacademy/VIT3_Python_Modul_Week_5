class School:
    def __init__(self, name, establishment_year):
        self.name = name
        self.establishment_year = establishment_year
        self.students = []
        self.teachers = {}

    def add_new_student(self, student_name, grade):
        self.students.append((student_name, grade))

    def add_new_teacher(self, teacher_name, subject):
        self.teachers[teacher_name] = subject

    def display_student_list(self):
        print("Registered students in the school:")
        for student, grade in self.students:
            print(f"{student} (Grade {grade})")

    def display_teacher_list(self):
        print("Teachers working in the school:")
        for teacher, subject in self.teachers.items():
            print(f"{teacher} ({subject})")

# Create an instance of School class
our_school = School("High School 42", 1990)

# Add students and teachers
our_school.add_new_student("Ali", 10)
our_school.add_new_student("Ayşe", 11)
our_school.add_new_teacher("Fatma", "Mathematics")
our_school.add_new_teacher("Mehmet", "Physics")

# Display the lists
our_school.display_student_list()
our_school.display_teacher_list()
