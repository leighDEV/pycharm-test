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

# PART 16: INHERITANCE
class Employee:
    def __init__(self, name, job, salary):
        self.name = name
        self.job = job
        self.salary = salary

    def introduce(self):
        print(f"Hi, my name is {self.name}")

    def full_profile(self):
        print(f"Name: {self.name}\nJob: {self.job}\nSalary: {self.salary}")


class Engineer(Employee):  # child class of Employee class
    def __init__(self, name, job, salary, type, tools):  # adding attributes
        super().__init__(name, job, salary)  # pertaining to parent's params
        self.type = type
        self.tools = tools

    def introduce(self):
        super().introduce()
        print(end=f", a {self.type}. I'm using {self.tools}.")  # used end= so this will attach to the code above

    def full_profile(self):  # overriding methods
        super().full_profile()  # getting the codes from parent's full profile's method
        print(f"Type: {self.type}\nTools: {self.tools}")  # adding this to the code in that method


class Teacher(Employee):
    def __init__(self, name, job, salary, school, position):
        super().__init__(name, job, salary)
        self.school = school
        self.position = position

    def introduce(self):
        print(f"Hi, my name is {self.name}, a {self.position} from {self.school}.")

    def full_profile(self):
        print(f"School: {self.school}\nPosition: {self.position}")
        super().full_profile()  # it can be placed before or after the added code

    def cheer_school(self):  # added a new method that is not inside a parent class
        print(f"Go, {self.school}! Go! Go! Go!")


emp_one = Employee("Harry", "Manager", 200000)
emp_one.introduce()
emp_one.full_profile()

eng_one = Engineer("Leigh", "Engineer", 150000, "Software Engineer", "IDEs")
eng_one.introduce()
eng_one.full_profile()

teach_one = Teacher("Hermione", "Teacher", 70000, "Hogwarts", "Teacher III")
teach_one.introduce()
teach_one.full_profile()
teach_one.cheer_school()
