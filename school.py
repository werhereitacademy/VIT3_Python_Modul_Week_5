'''Soru2: Python'da bir "Okul" sınıfı oluşturun. Bu sınıf aşağıdaki özelliklere ve işlevselliklere sahip olmalıdır:

##### Özellikler:
- "ad" 
- "kuruluş_yılı" 
- "öğrenciler" 
- "öğretmenler"
- 
##### Metodlar:
- yeni_öğrenci_ekle(self, öğrenci_adı, sınıf): Yeni bir öğrenciyi okula eklemek için kullanılan bir metod. Öğrencinin adını ve sınıfını alır ve "öğrenciler" listesine ekler.
- yeni_öğretmen_ekle(self, öğretmen_adı, branş): Yeni bir öğretmeni okula eklemek için kullanılan bir metod. Öğretmenin adını ve branşını alır ve "öğretmenler" sözlüğüne ekler.
- öğrenci_listesi_görüntüle(self): Okula kayıtlı öğrencilerin listesini görüntülemek için kullanılan bir metod. Öğrenci adlarını ve sınıflarını listeleyin.
- öğretmen_listesi_görüntüle(self): Okulda çalışan öğretmenlerin listesini görüntülemek için kullanılan bir metod. Öğretmen adlarını ve branşlarını listeleyin.
##

'''

#okul sinifi olusturalim.

'''class Okul :
    def __init__(self, ad, kurulus_yili):
    ## ozellikler
        self.ad = ad
        self.kurulus_yili = kurulus_yili
    #ogrcileri tutmak icin bir liste olusturalim
        self.ogrenciler = []
    #ogretmenleri tutmak icin bir liste olusturalim
        self.ogretmenler = []
        
 #metodlar
 

    def yeni_ogrenci_ekle(self, ogrenci_adi, sinifi):
        self.ogrenciler.append({"ogrenci_adi":ogrenci_adi, "sinifi":sinifi})
        
    def yeni_ogretmen_ekle(self, ogretmen_adi, brans):
        self.ogretmenler.append({"ogretmen_adi":ogretmen_adi, "brans":brans})
        
    def ogrenci_listesi_goruntule(self):
        print(self.ogrenciler)
    def ogretmen_listesi_goruntule(self):
        print(self.ogretmenler)
    
    
    
    
lise = Okul("samanyolu lisesi", 1998)
lise.ogrenci_listesi_goruntule()
lise.ogretmen_listesi_goruntule()
lise.kurulus_yili
lise.ad
lise.yeni_ogrenci_ekle("aysima", "11a")
lise.ogrenci_listesi_goruntule()
lise.yeni_ogrenci_ekle("suheyb", "12a")
lise.ogrenci_listesi_goruntule()


ortaokul = Okul("inkilap ortaokulu", 1996)
ortaokul.ogrenci_listesi_goruntule()
ortaokul.yeni_ogrenci_ekle("mavis", "7a")
ortaokul.yeni_ogrenci_ekle("sedef", "7b")
ortaokul.yeni_ogrenci_ekle("mehmet", "7c")
ortaokul.ogrenci_listesi_goruntule()'''







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