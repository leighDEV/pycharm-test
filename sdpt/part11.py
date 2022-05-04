# PART 11: ARGUMENTS, ARBITRARY ARGUMENTS, KEYWORD ARGUMENTS


def say_hello(name):
    print("Hello,", name)


i = 1
while i > 0:
    say_hello(input("Enter a name: "))  # using function to input


# arbitrary arguments - asterisk args
# can't have two in a function, it is neverending


def say_hi(*names):  # it converts to tuples, unspecified size
    for name in names:
        print("Hi,", name)


say_hi("Leigh", "Inna", "Jamolin",)

# keyword arguments(kwargs) - an alternative way for sending arguments inside a function by specifying
# the parameter name in no certain order. Often used in combination with arbitrary args or if you don't know
# the order of the arguments in the function.


def jaja(fname, lname):
    print(fname + " " + lname)


jaja(lname="Jamolin", fname="Leigh")  # using kwargs


def jamolin_fam(*fnames, lname):
    for fname in fnames:
        print(fname + " " + lname)


jamolin_fam("Lionel", "Gina", "Leigh", "Janna", "Mira", lname="Jamolin")

# arbitrary keyword arguments(**kwargs)
# used when you are uncertain on what parameter name and how many param you want to pass


def students_info(**student):
    print(student["fname"] + " " + student["lname"])
    print(f"Age:", student["age"])
    print(f"Course: " + student["course"])


# keywords are always strings
fname = input("Enter first name: ")
lname = input("Enter last name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")

print("Student #1")
students_info(fname=fname, lname=lname, course=course, age=age)  # no certain order


# challenge - summation program


def summation(*num):
    x = 0
    for n in num:
        x += n
    return x


print(summation(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
