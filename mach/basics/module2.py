# Module 2
# functions, dev keyword, arguments

def hello_function():
    print("Hello")  # the indented line makes up the body of a function


hello_function()


def welcome_function(f_name, l_name):  # different variable name?
    print("Welcome, " + f_name + " " + l_name)


first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
welcome_function(first_name, last_name)


def greetings(y_name):
    print("Have a nice day, " + y_name + "!")
# after a class of def, two blank lines is needed, also with inline comment


greetings("Leigh")


# Input functions
name = input("Enter name: ")
print("Hello, " + name)

first_num = int(input("Enter first num: "))
second_num = int(input("Enter second num: "))
result = first_num + second_num
print(str(first_num) + " + " + str(second_num) + " = " + str(result))


def add_num(n1, n2):
    total = n1 + n2
    return total


num1 = int(input("Enter first num: "))
num2 = int(input("Enter second num: "))
print("Total: ", add_num(num1, num2))  # I can use comma here

name = input("Name: ")
age = int(input("Age: "))
favourite_color = input("Favourite color: ")
favourite_movie = input("Favourite movie: ")
mobile_number = input("Mobile number: ")
motto = input("Motto in life: ")

print("Hi, " + name)
print("You are " + str(age) + " years old.")
print("Your fave color is " + favourite_color + " and your fave movie is " + favourite_movie)
print("Your mobile number is " + mobile_number)
print("Your motto in life is " + motto)


# DATA TYPE AND CONVERSION

this_a_string = "This is a string"
print(this_a_string)
name = input("Enter name: ")
this_an_int = 5
this_a_float = 3.0
print(this_an_int)
print(this_a_float)
salary = float(input("Enter salary: "))
print(salary)
is_hot = True
print(is_hot)
print(1 < 2)
print(2 < 1)
print(int(33.33))  # Converting a float to an int
print(float(33))
print(str(334))
print(tuple("Leigh Inna"))
print(list("Leigh Inna"))

# CODING EXERCISES

hmm = 10 < 7
print(hmm)

num = 73911
print(str(num))

print(tuple("Thank God it's Friday!"))

print(float(4302))

print(int(3299.35640))


def hello_function(f_name, l_name):
    print("Hello, " + f_name + " " + l_name)


hello_function("Leigh", "Molina")
hello_function("Inna", "Jamolin")
hello_function("Inna", "Casino")

num1 = int(input("Enter first num: "))
num2 = int(input("Enter second num: "))
print("Your two numbers are", num1, "and", num2)
