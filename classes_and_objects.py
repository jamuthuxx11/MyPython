class Student:
    admission_number = ''
    student_name = ''
    student_age = ''

    def __init__(self, admission, name, age):
        self.admission_number = admission
        self.student_name = name
        self.student_age = age
        print('Student:', self.admission_number, self.student_name, self.student_age)



class student:
    adm_number = ""
    student_name = ""
    student_age = ""

    def __init__(self):  # constructor gets called by default whenever an object is created
        print("Initializes students class")

    def set_name(self, name):  # setting name
        self.student_name = name

    def display_name(self):  # displaying the name
        print("The student name is", self.student_name)


student1 = student()
student1.set_name("franklin")
student1.display_name()
student2 = student()
student2.set_name("john")
student2.display_name()

#how to create classes using inheritance
class person:
    person_age=0
    person_name= ""
    person_residence=""
    def __init__(self,name,age,residence):
        self.person_name = name
        self.person_ageperson_age = age
        self.person_residence =residence

    def print_person(self):
        print("name:", self.person_name,"age:", self.person_ageperson_age,"residence:",self.person_residence)
#inheriting from