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
    def __init__(self, name, job, salary, category, tools):  # adding attributes
        super().__init__(name, job, salary)  # pertaining to parent's params
        self.category = category
        self.tools = tools

    def introduce(self):
        super().introduce()
        print(end=f", a {self.category}. I'm using {self.tools}.")  # used end= so this will attach to the code above

    def full_profile(self):  # overriding methods
        super().full_profile()  # getting the codes from parent's full profile's method
        print(f"Category: {self.category}\nTools: {self.tools}")  # adding this to the code in that method


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

# prompting a user then using it as arguments
teach_name = input("Enter name: ")
teach_job = input("Enter job: ")
teach_salary = int(input("Enter salary: "))
teach_school = input("Enter school: ")
teach_position = input("Enter position: ")

teach_one = Teacher(teach_name, teach_job, teach_salary, teach_school, teach_position)
teach_one.introduce()
teach_one.full_profile()
teach_one.cheer_school()
