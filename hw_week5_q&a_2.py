import json


class School:
    def __init__(self, advert, establishment_year):
        self.advert = advert
        self.establishment_year = establishment_year

        # Assigning values from JSON files for self.students and self.teachers
        try:
            with open('students.json', 'r', encoding='UTF-8') as fp:
                self.students = json.load(fp)

            with open('teachers.json', 'r', encoding='UTF-8') as fp:
                self.teachers = json.load(fp)

        # If there are no JSON files, create new ones.
        # Limitations: If you tried to call any function, it will not work properly
        except Exception as e:
            self.students = []
            self.teachers = []
            with open('students.json', 'w', encoding='UTF-8') as fp:
                json.dump(self.students, fp)

            with open('teachers.json', 'w', encoding='UTF-8') as fp:
                json.dump(self.teachers, fp)

            raise e     # raise the errors anyway

    def add_new_student(self, name, clss):
        student = {'name': name, 'class': clss}
        self.students.append(student)
        with open('students.json', 'w', encoding='UTF-8') as fp:
            json.dump(self.students, fp)
        return student  # Maybe we use it later

    def add_new_teacher(self, name, branch):
        teacher = {'name': name, 'branch': branch}
        self.teachers.append(teacher)
        with open('teachers.json', 'w', encoding='UTF-8') as fp:
            json.dump(self.teachers, fp)
        return teacher  # Maybe we use it later

    def list_students(self):
        with open('students.json', 'r', encoding='UTF-8') as fp:
            self.students = json.load(fp)
            for student in self.students:
                print(f'Student Name    : {student["name"]}\n'
                      f'Education Class : {student["class"]}\n')

    def list_teachers(self):
        with open('teachers.json', 'r', encoding='UTF-8') as fp:
            self.teachers = json.load(fp)
            for teacher in self.teachers:
                print(f'Teacher Name : {teacher["name"]}\n'
                      f'Branch       : {teacher["branch"]}\n')


if __name__ == '__main__':
    school = School('First School of Code', 2024)

    # name1 = input('Enter the new student name: ')
    # class1 = input('Enter the class number that this student will get education: ')
    #
    # school.add_new_student(name1, class1)
    #
    # name2 = input('Enter the new teacher name: ')
    # branch1 = input('Enter this teacher\'s branch: ')
    #
    # school.add_new_teacher(name2, branch1)

    print('----------------------Students-------------------------')
    school.list_students()
    print('----------------------Teachers-------------------------')
    school.list_teachers()
