# MODULE 4: MODULES - good at reusing code
# - ultimate way of keeping code short, clean, and readable
import datetime

from ownlib.objects import *  # asterisk means all but you can just write like below
# import ownlib.objects as o
from ownlib.arithmetic import add as a  # importing add function only and alias it to a

first_num = int(input("Enter first num: "))
second_num = int(input("Enter second num: "))

print(a(first_num, second_num))

name = input("Enter name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")
section = input("Enter section: ")

s1 = Student(name, age, course, section)
s1.introduce()

admin.introduce()  # getting an instance
print(dir(admin))  # returns a lists of valid attributes of the obj


# CODING EXERCISES
from ownlib.functionfile import say_hi as hi
from ownlib.functionfile import say_hello as hello

print(hi())
print(hello())


# USING BUILT-IN PYTHON MODULES
help("modules")  # to see all available modules
help("random")  # view all the attributes of this module

print(dir("random"))

from random import randint
print(int(randint(1, 1000)))  # random number

import datetime as dt
dt = dt.datetime.now()
print(dt.strftime("%m/%d/%Y"))  # 05/04/2022
print(dt.day)  # printing day only

x = datetime.datetime(2002, 6, 6)
print(x)  # printing a specified date
