# PART 14: CONSTRUCTORS

class Student:  # everytime we call this, the constructors also run

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Name: {self.name}\nAge: {self.age}\nCourse: {self.course}")


student_one = Student("Leigh", 19, "BSCS")
student_one.introduce()  # printing already
