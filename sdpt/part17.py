# PART 17: COLLECTION OF OBJECTS

# creating object by user input (example above)

class Person:
    def __init__(self, p_name, p_age):
        self.name = p_name
        self.age = p_age
        print(f"{self.name} created!")

    def introduce(self):
        print(f"Hi, my name is {self.name}, {self.age} years old.")


p_one = Person("Leigh", 19)
p_two = Person("Inna", 20)
p_three = Person("Jamolin", 22)
p_four = Person("Hermione", 27)

# store objects in a collection
person_list = [p_one, p_two, p_three, p_four]

# reading objects in a collection
print(person_list[0].name)
person_list[1].introduce()  # the reason why there's sometimes None in the console
# is because you use print when there's already print in the method

# using loop to read collections
for person in person_list:
    person.introduce()

# using loop to write collections
for i in range(5):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    p = Person(name, age)
    person_list.append(p)

for person in person_list:
    person.introduce()


# try

class ProgrammingLanguage:
    def __init__(self, pname, p_ide):
        self.pname = pname
        self.p_ide = p_ide
        print(f"{self.pname} created!\n")

    def info(self):
        print(f"Name: {self.pname}\nIDE: {self.p_ide}")


p_list = []

num = int(input("Enter how many: "))
for i in range(num):
    name = input("Enter name: ")
    ide = input("Enter ide: ")
    pl = ProgrammingLanguage(name, ide)
    p_list.append(pl)

print("Programming Languages:")
i = 1
for p in p_list:
    print(f"#{i}")
    p.info()
    print()
    i += 1


# challenge - student registration program

class Student:
    def __init__(self, s_name, s_course, s_year, s_section):
        self._name = s_name
        self._course = s_course
        self._year = s_year
        self._section = s_section
        print(f"{self._name} created!\n")

    def introduce(self):
        print(f"Name   : {self._name}")
        print(f"Course : {self._course}")
        print(f"Year   : {self._year}")
        print(f"Section: {self._section}")


student_list = []
while True:
    add = input("Add? (Y/N): ")
    if add == 'Y':
        name = input("Enter name: ")
        course = input("Enter course: ")
        year = input("Enter year: ")
        section = input("Enter section: ")
        students = Student(name, course, year, section)
        student_list.append(students)
    elif add == 'N':
        print("\nStudents in the list:")
        i = 0
        for student in student_list:
            i += 1
            print(f"Student #{i}")
            student.introduce()
            print()
        break
    else:
        print("Wrong input.")


# solutions from tutorial
class Student:
    def __init__(self, s_name, s_course, s_year, s_section):
        self.name = s_name
        self.course = s_course
        self.year = s_year
        self.section = s_section

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
