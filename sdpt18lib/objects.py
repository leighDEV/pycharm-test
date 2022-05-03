class Student:
    def __init__(self, name, age, course, section):
        self._name = name
        self._age = age
        self._course = course
        self._section = section

    def introduce(self):
        print(f"Hi, I'm {self._name}, {self._age}, years old")
