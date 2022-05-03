# # PART 13: OOP | CLASSES AND OBJECTS
#
# class Enemy:
#     name = "Name"  # default value
#     hp = 100
#     mp = 50
#     atk = 12
#     lvl = 1
#
#
# enemy_one = Enemy()
# enemy_one.name = "Leigh"
# enemy_one.hp = 99
# enemy_one.mp = 50
# enemy_one.atk = 8
# enemy_one.lvl = 99
#
# enemy_two = Enemy()
# enemy_two.name = "Inna"
#
# print(enemy_one.name)
# print(enemy_two.name)
#
#
# class Product:
#     brand = "Brand"
#     id = 1000
#     qty = 0
#
#
# product_one = Product()
# product_one.brand = "Tesla"
# product_one.id = 999
# product_one.qty = 9
#
# print(product_one.brand)
# print(product_one.id)
# print(product_one.qty)
#
# product_two = Product()
#
#
# # PART 14: CONSTRUCTORS
#
# class Student:  # everytime we call this, the constructors also run
#
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course
#
#     def introduce(self):
#         print(f"Name: {self.name}\nAge: {self.age}\nCourse: {self.course}")
#
#
# student_one = Student("Leigh", 19, "BSCS")
# student_one.introduce()  # printing already
#
#
# # PART 15: OBJECT FUNCTIONS
# # also called methods (functions inside a class) - represent the object's purpose
# # constructors are also an object functions
#
# class Animal:
#     def __init__(self, type, sound):
#         self.type = type
#         self.sound = sound
#
#     def speak(self):  # methods always have self parameter at first
#         print(f"{self.type}: {self.sound}")
#
#
# animal_dog = Animal("Dog", "Woof")
# animal_dog.speak()
# animal_cat = Animal("Cat", "Meow")
# animal_cat.speak()
#
#
# # challenge - user in a social media
#
# class User:
#     def __init__(self, first_name, last_name, likes_count, friends_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.likes_count = likes_count
#         self.friends_name = friends_name
#         print(f"User created. Welcome, {self.first_name}!")
#
#     def introduce(self):
#         print(f"Hi, I am  {self.first_name} {self.last_name}!")
#
#     def full_profile(self):
#         print(f"Full name: {self.first_name} {self.last_name}")
#         print(f"Likes    : {str(self.likes_count)}")
#         print("Friends  : ")
#         for friend in self.friends_name:  # this is a list
#             print(" -" + friend)
#
#
# user_one = User("Leigh", "Jamolin", 10, ["Harry", "Ron", "Hermione"])
# user_one.introduce()
# user_one.full_profile()
#
# print()
# user_two = User("Hermione", "Granger", 99, ["Harry", "Ron", "Ginny"])
# user_two.introduce()
# user_two.full_profile()
#
#
# # PART 16: INHERITANCE
# class Employee:
#     def __init__(self, name, job, salary):
#         self.name = name
#         self.job = job
#         self.salary = salary
#
#     def introduce(self):
#         print(f"Hi, my name is {self.name}")
#
#     def full_profile(self):
#         print(f"Name: {self.name}\nJob: {self.job}\nSalary: {self.salary}")
#
#
# class Engineer(Employee):  # child class of Employee class
#     def __init__(self, name, job, salary, category, tools):  # adding attributes
#         super().__init__(name, job, salary)  # pertaining to parent's params
#         self.category = category
#         self.tools = tools
#
#     def introduce(self):
#         super().introduce()
#         print(end=f", a {self.category}. I'm using {self.tools}.")  # used end= so this will attach to the code above
#
#     def full_profile(self):  # overriding methods
#         super().full_profile()  # getting the codes from parent's full profile's method
#         print(f"Category: {self.category}\nTools: {self.tools}")  # adding this to the code in that method
#
#
# class Teacher(Employee):
#     def __init__(self, name, job, salary, school, position):
#         super().__init__(name, job, salary)
#         self.school = school
#         self.position = position
#
#     def introduce(self):
#         print(f"Hi, my name is {self.name}, a {self.position} from {self.school}.")
#
#     def full_profile(self):
#         print(f"School: {self.school}\nPosition: {self.position}")
#         super().full_profile()  # it can be placed before or after the added code
#
#     def cheer_school(self):  # added a new method that is not inside a parent class
#         print(f"Go, {self.school}! Go! Go! Go!")
#
#
# emp_one = Employee("Harry", "Manager", 200000)
# emp_one.introduce()
# emp_one.full_profile()
#
# eng_one = Engineer("Leigh", "Engineer", 150000, "Software Engineer", "IDEs")
# eng_one.introduce()
# eng_one.full_profile()
#
# # prompting a user then using it as arguments
# teach_name = input("Enter name: ")
# teach_job = input("Enter job: ")
# teach_salary = int(input("Enter salary: "))
# teach_school = input("Enter school: ")
# teach_position = input("Enter position: ")
#
# teach_one = Teacher(teach_name, teach_job, teach_salary, teach_school, teach_position)
# teach_one.introduce()
# teach_one.full_profile()
# teach_one.cheer_school()
#
#
# # PART 17: COLLECTION OF OBJECTS
#
# # creating object by user input (example above)
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print(f"{self.name} created!")
#
#     def introduce(self):
#         print(f"Hi, my name is {self.name}, {self.age} years old.")
#
#
# p_one = Person("Leigh", 19)
# p_two = Person("Inna", 20)
# p_three = Person("Jamolin", 22)
# p_four = Person("Hermione", 27)
#
# # store objects in a collection
# person_list = [p_one, p_two, p_three, p_four]
#
# # reading objects in a collection
# print(person_list[0].name)
# person_list[1].introduce()  # the reason why there's sometimes None in the console
# # is because you use print when there's already print in the method
#
# # using loop to read collections
# for person in person_list:
#     person.introduce()
#
# # using loop to write collections
# for i in range(5):
#     name = input("Enter name: ")
#     age = int(input("Enter age: "))
#     p = Person(name, age)
#     person_list.append(p)
#
# for person in person_list:
#     person.introduce()
#
#
# # try
#
# class ProgrammingLanguage:
#     def __init__(self, pname, p_ide):
#         self.pname = pname
#         self.p_ide = p_ide
#         print(f"{self.pname} created!\n")
#
#     def info(self):
#         print(f"Name: {self.pname}\nIDE: {self.p_ide}")
#
#
# p_list = []
#
# num = int(input("Enter how many: "))
# for i in range(num):
#     name = input("Enter name: ")
#     ide = input("Enter ide: ")
#     pl = ProgrammingLanguage(name, ide)
#     p_list.append(pl)
#
# print("Programming Languages:")
# i = 1
# for p in p_list:
#     print(f"#{i}")
#     p.info()
#     print()
#     i += 1
#
#
# # challenge - student registration program
#
# class Student:
#     def __init__(self, name, course, year, section):
#         self._name = name
#         self._course = course
#         self._year = year
#         self._section = section
#         print(f"{self._name} created!\n")
#
#     def introduce(self):
#         print(f"Name   : {self._name}")
#         print(f"Course : {self._course}")
#         print(f"Year   : {self._year}")
#         print(f"Section: {self._section}")
#
#
# student_list = []
# while True:
#     add = input("Add? (Y/N): ")
#     if add == 'Y':
#         name = input("Enter name: ")
#         course = input("Enter course: ")
#         year = input("Enter year: ")
#         section = input("Enter section: ")
#         students = Student(name, course, year, section)
#         student_list.append(students)
#     elif add == 'N':
#         print("\nStudents in the list:")
#         i = 0
#         for student in student_list:
#             i += 1
#             print(f"Student #{i}")
#             student.introduce()
#             print()
#         break
#     else:
#         print("Wrong input.")
#

# solutions from tutorial
class Student:
    def __init__(self, name, course, year, section):
        self.name = name
        self.course = course
        self.year = year
        self.section = section

    def introduce(self):
        print(f"     Name   : {self.name}")
        print(f"     Course : {self.course}")
        print(f"     Year   : {self.year}")
        print(f"     Section: {self.section}")


student_list = []
while True:
    print()
    name = input("Name: ")
    course = input("Course: ")
    year = input("Year: ")
    section = input("Section: ")
    s = Student(name, course, year, section)
    student_list.append(s)

    print()
    choice = input("Create another student? [Y/Any Char]: ")
    if choice == 'Y' or choice == 'y':
        pass
    else:
        break

i = 1
for student in student_list:
    print()
    print(f"Student #{str(i)}")
    student.introduce()
    i = i + 1
