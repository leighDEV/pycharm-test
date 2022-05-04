# PART 10: FUNCTIONS, PARAMETERS OR ARGUMENTS, RETURN VALUES

import math
import sys


def sqrtfuc(n):
    print(math.sqrt(n))


num = int(input("Enter a number: "))
sqrtfuc(num)

# arguments or parameters


def greetings(fname, lname):
    print(f"Hello, {fname} {lname}!")


first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
greetings(first_name, last_name)

# return values - a value returned after executing a function
# used to get results from a function that computes or does something that needs a result


def add_num(n1, n2):
    total = n1 + n2
    return total


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"{num1} + {num2} = {add_num(num1, num2)}")


# calculator


def add(n1, n2):
    sum = n1 + n2
    return sum


def subtract(n1, n2):
    diff = n1 - n2
    return diff


def multiply(n1, n2):
    prod = n1 * n2
    return prod


def divide(n1, n2):
    quotient = n1 / n2
    return quotient


print("Operations:\n+ for add\n- for subtract\n* for multiply\n/ for divide.\nx for exit.")

i = 1
while i > 0:
    ope = input("Enter operation: ")
    if ope == "x":
        sys.exit()
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if ope == "+":
        print(f"{num1} {ope} {num2} = {add(num1, num2)}")
    elif ope == "-":
        print(subtract(num1, num2))
    elif ope == "*":
        print(multiply(num1, num2))
    elif ope == "/":
        print(divide(num1, num2))
    else:
        print("Wrong input.")


# challenge - square a number using functions w/ parameters


def square(n):
    return n * n


num = int(input("Input: "))
print(f"Output: {square(num)}")
