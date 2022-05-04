import os

# MODULE 3: FILES AND EXCEPTIONS

# creating a file - x stands for create
# f1 = open("newfile.txt", "x")

# writing to file - w stands for write
f = open("newfile.txt", "w")
f.write("Hello World")

# reading to a file - r stands for read
f = open("newfile.txt", "r")
print(f.read())
f.close()

# using w will overwrite content

# appending to a file - a stands for append
f = open("newfile.txt", "a")
f.write("\nHello, Leigh")  # used new line

# CODING EXERCISES
f = open("newfile.txt", "w")
f.write("It's short and covers a lot of area in tech.")
f.write("\nUse it to learn data science.")
f.write("\nBy creating projects.")
f.write("\nMy goal is to become an AI engineer.")

f = open("newfile.txt", "r")
print(f.read())
f.close()

# READING FROM A FILE
# r is a default value for python
# always make sure that the file exists before reading
f = open("newfile.txt")  # does not require "r" in reading
print(f.read(12))  # reading 12 characters from file

print(f.readline())  # returns single line
print(f.readline())

print("loop start")
# using loops to read one line at a time
for x in f:
    print(x)  # some lines are gone, maybe because of read and readline above

f.close()  # always close the file

# deleting a file
# make sure first the file exist by using conditional statement
if os.path.exists("newfile.txt"):
    print("This file will be deleted.")
    # os.remove("newfile.txt")
else:
    print("The file does not exist.")

# if you're sure that file exists, you can just
# os.remove("newfile.txt")


# CODING EXERCISES
f = open("newfile.txt", "r")
print("f.read")
print(f.read())

f = open("newfile.txt", "r")
print("f.readline")
print(f.readline())

f = open("newfile.txt", "r")
print("for loop")
for x in f:
    print(x)

f.close()

if os.path.exists("newfile.txt"):
    print("File exists")
    # os.remove("newfile.txt")
else:
    print("File doesn't exists")

# EXCEPTIONS

# raise keyword
# n = -5
# if n < 0:
#     raise Exception("No negative numbers allowed.")

# SyntaxError - occurs when code is not written correctly
# for f in fsx  # doesn't have colon
#     print(f)

# assertions - boolean expressions that make sure that the conditions are true
# can also be used as a debugging tool
# employee_one = "Leigh"
# assert employee_one == "Leigh"
# assert employee_one == "Inna"

# ZeroDivisionError - occurs when you divide by zero
# print(3/0)

# TypeError - occurs when an operation is performed on an incorrect or unsupported object type
# print(50 ** "two")

# handling exceptions
try:
    print(x)
except:
    print("Exception alert!")
finally:  # will run our code even if there's an error
    print("Let's run our code anyway")
# can define many exception blocks as you want for any type of error you may encounter

try:
    print(y + "macarons")
except NameError:
    print("Please define your variable.")
except IndentationError:
    print("Please be careful when indenting your code.")
except:
    print("Something else is wrong.")
else:
    print("No issues here.")
# since these are conditional statements, we can use else too


# CODING EXERCISES
# x = 500
# if x > 100:
#     raise Exception(x, "is greater than 100")

try:
    print(v)
except NameError:
    print("Please define your variable.")


for i in range(3):
    print("haha")


try:
    print(12 * 6)
except:
    print("The operation can't be performed")
else:
    print("The operation can be performed")

best_burger = "Burger King"
second_bes_burger = "McDonald's"
assert best_burger == "Burger King"
assert best_burger == "McDonalds"
