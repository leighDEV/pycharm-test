# first_name = "Leigh"
# last_name = "Jamolin"
# x = 10
# y = 12.33
# is_tall = False
#
# print(first_name + " " + last_name)
# print(first_name + last_name)
# deci = 12.3300
# print(deci)
# # cannot concatenate int
#
# jaja = "Jaja"
# num = 3
# print(jaja + str(num))
#
# # user input is always in string format
# name = input("Enter name: ")
# print("Welcome, " + name)
# t = input("Enter first num: ")
# r = input("Enter second num: ")
# print(int(x) + int(y))
#
# salary = input("Enter salary: ")
# another = input("Enter random int: ")
# print(float(salary) + int(another))
#
# yy = 23.33
# dd = 3
# print(yy + dd)
#
# xx = float(input("Enter first num: "))
# yy = float(input("Enter second num: "))
# ope = input("Enter operator: ")
#
# if ope == "+":
#     result = xx + yy
#     print(str(xx) + " + " + str(yy) + " = " + str(result))
# elif ope == "-":
#     result = xx - yy
# elif ope == "*":
#     print(xx * yy)
# elif ope == "/":
#     print(xx / yy)
# else:
#     print("Wrong operator.")
#
#
# # PART 3: LIST AND TUPLES
# # list - a read and write collection of variables
# names = ["Leigh", "Inna", "Jam", "Harry", "Hermione"]
# print(names[2:])
# print(names[:3])  # end index item is excluded
# print(names[1:4])
#
# # Assigning list items, also works with numbers
# names[3] = "Ron"  # replacing harry with ron
# print(names)
# print(len(names))
# names[1] = "Leigh"
# print(names.count("Leigh"))  # counting the leigh in the value, case sensitive
# names.append("Leigh")  # appending an item in the list
# print(len(names))
# print(names)
# names.insert(2, "Inna")  # inserting an item in the middle of list
# print(names)
# names.remove("Leigh")  # I think it will remove the latest leigh in the list, not all
# print(names)
# names.pop(-2)  # deleting item bases on index
# names.pop()  # deleting last item
# print(names)
# del names[2]  # deletes item bases on index
# print(names)
# del names  # deletes whole list
# names = ["Leigh", "Inna", "Jam"]
# print(names)
# print(names.clear())  # clear all items in list but not list, output is None
# print(names)  # output is square brackets
# names = ["Leigh", "Inna", "Jam"]
# group_members = names.copy()  # copying the items in names to this list
# print("Names list:", names)
# print("Group members:", group_members)
# # sequencing is very important, sabi sa tutorial
# duplicate = names + group_members
# print("Combined list:", duplicate)
# other_team = ["John", "Janna", "Jane"]
# print(other_team.extend(group_members))  # not working? output is None
# other_team.append(group_members)
# print(other_team)  # append list inside a list
# names.reverse()  # reversing the items in list
# print(names)
# # print(names.reverse()) - I think this is not working when I put the function inside print function? Output is None
# names.sort()  # sort the list in ascending order
# print(names)
# names.sort(reverse=True)  # sort list in descending order
# print(names)
# alphabet = ['A', 'B', 'C', 'Z', 'X', 'N', 'O', 'M']
# alphabet.sort(reverse=True)
# print(alphabet)
#
# # nested lists
# # index =    0        1       2                             3                                     4
# # index =                                       0               1        2       3        1       2          3
# # index =                              0        1       2
# courses = ["BSCS", "BSIT", "BSIS", [["DSCS", "DSIT", "DSIS"], "MSCS", "MSIT", "MSIS"], ["GOD", "MASTER", "EMPRESS"]]
# print(courses)
# print(courses[2])  # output is BSIS
# print(courses[3])  # output is the list of d and m
# print(courses[4])  # output is list of god
# print(courses[4][1])  # output is MASTER
# print(courses[3][0])  # output is list of d
# print(courses[3][0][0])  # output is DSCS, this has 3 index because it's a list inside a list of a list
# print(courses[3][1])  # output is MSCS
#
# # tuples - a read only collection
# # can use some functions of list here
# # can read, combined, delete completely but can't be assigned, can't delete one by one
# # usually use in constants, formula like pi
# print()
# tup_courses = ("BSCS", "BSIT", "BSIS")
# print(tup_courses)
# del tup_courses
# tup_names = ("Leigh", "Inna", "Jam", ("John", "Janna", "Jane"))  # nested tuples
# print(tup_names[3])
#
# # casting tuples and lists
# tup_names = list(tup_names)  # useful when you want to edit your tuple
# courses = tuple(courses)
# print(tup_names)
# print(courses)
#
# # PART 4: SETS
# # sets - partially writable, and it's unordered and un-indexed.
#
# evenNum = {2, 4, 8, 10}
# print(evenNum)
# print(len(evenNum))  # can also use some builtin functions like list
#
# evenNum = list(evenNum)
# evenNum[0] = 6
# print(evenNum[0])
# print(evenNum)
# evenNum = set(evenNum)
# print(evenNum)
#
# evenNum.add(12)  # can add item at the end of set
# print(evenNum)
#
# evenNum.update([14, 16, 18, 20])  # add multiple items through list
# extension = [22, 24, 26]
# evenNum.update(extension)  # can also use variable inside
# print(evenNum)
#
# evenNum.remove(2)  # remove item by value, has error if value doesn't exist
# print(evenNum)
#
# evenNum.discard(1)  # delete an item by value, no error
# print(evenNum)
#
# evenNum.pop()  # deletes first item
# print(evenNum)
#
# evenNum2 = evenNum.copy()  # copy the whole set to another new set
# print(evenNum2)
#
# evenNum.clear()  # deletes all the value in set
# print(evenNum)
#
# del evenNum  # deletes the set
#
# # union set
# set_one = {1, 3, 5, 7, 9}
# set_two = {4, 8, 6, 10, 2}
# set_union = set_one.union(set_two)  # combine two sets
# print(set_union)
# print(len(set_union))
#
# # difference set
# num1 = {1, 2, 3, 4, 5}
# num2 = {1, 2, 6, 7, 8}
# # mind what's first set below
# num3 = num1.difference(num2)  # return values that only exist on the left/first side
# print(num3)  # output is 3, 4, 5
#
# # intersection set
# set_inter = num1.intersection(num2)  # returns the same values
# print(set_inter)  # output is 1, 2
#
# # symmetric difference set
# set_sym = num1.symmetric_difference(num2)  # remove the set that is both on sets
# # and returns values that exist exclusively on each set
# print(set_sym)  # output is 3, 4, 5, 6, 7, 8
#
# # disjoint set
# set_dis = num1.isdisjoint(num2)  # returns a boolean whether two sets have an intersection or not
# print(set_dis)  # output is False, because both set has same value even one
# odd = {1, 3, 5, 7, 9}
# even = {2, 4, 6, 8, 10}
# print(odd.isdisjoint(even))  # output is True
#
# # subset
# set_sub = num1.issubset(num2)  # returns a boolean whether the left set is contained in the right set
# print(set_sub)  # output is False
# num = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(even.issubset(num))  # output is True cause all the value in even is in num
#
# # superset
# set_sup = num.issuperset(even)  # returns a boolean whether the right set is contained in the left set
# print(set_sup)  # output is True cause num is the superset of even
# print(num1.issuperset(num2))  # output is False
#
# # casting sets
# # you can cast them vice versa
# print(list(num))
# print(tuple(even))
# num = list(num)
# print(num)
# num = set(num)
# print(num)
#
# # nested sets
# set_nes = {1, 2, 3, {4, 5, 6}}  # unhashable type: set
#
#
# # PART 5: DICTIONARY | LIST OF DICTIONARIES
# # a collection of Key Pairs that is unordered , changeable and indexed
# student_one = {
#     "name": "Leigh",
#     "age": 19,
#     "course": "BSCS"
# }
#
# student_two = {
#     "name": "Inna",
#     "age": 18,
#     "course": "BSIT"
# }
#
# print(student_one)  # reading the whole dict
# print(student_two)
# print(student_one["name"])  # reading the value of key "Name"
# print(student_two["course"])
# print(student_one.get("age"))  # reading value by using get
# print(student_two.get("name"))
#
# student_two["age"] = 19  # changing the value
# print(student_two)
#
# print(len(student_one))  # checking the number of items
#
# student_one["town"] = "Famy"  # adding items
# print(student_one)
#
# student_one.pop("town")  # deletes an item based on their key value
# print(student_one)
#
# student_two.popitem()  # deletes the last item
# print(student_two)
#
# student_two.clear()  # clears all the items
# print(student_two)
#
# del student_two  # deletes the dict
#
# student_three = student_one.copy()  # copies the whole dict to another dict
# print(student_three)
#
# print(student_three.keys())  # getting all keys in dict
# print(student_three.values())  # getting all values in dict
#
# students = [student_one, student_three]  # dicts inside a list
# print(students)
# print(students[0])  # returns a dict from a list
# print(students[0].get("name"))  # getting item of a dict in a list
#
# # nested dictionaries
# student_four_grades = {
#     "math": 99,
#     "science": 98,
#     "english": 97
# }
#
# student_four = {
#     "name": "Inna",
#     "age": 19,
#     "course": "BSCS",
#     "grades": student_four_grades  # nesting dict
# }
# print(student_four)
# print(student_four.get("grades").get("math"))  # getting the item from the nested dict
#
#
# # PART 6: CONDITIONAL STATEMENTS
# name = input("Enter name: ")
# age = int(input("Enter age: "))
#
# if age >= 18:
#     registered = input("Are you registered? Yes or No? ")
#     if registered == "Yes":
#         print("You are qualified to vote!")
#     else:
#         print("Please register first.")
# else:
#     print("You are not yet qualified to vote.")
# print("\nThank you for using the program.")
#
# # not keyword
# math_grades = int(input("Enter math grades: "))
#
# if not math_grades >= 95:
#     print("You are so bobo.")
# else:
#     print("Thumbs up!")
#
# # logical operators
# username = input("Enter username: ")
# password = input("Enter password: ")
#
# if (username == "leighter" and password == "asdf") or (username == "Innay" and password == "qwer"):
#     print("Welcome,", username)
# else:
#     print("Login failed.")
#
# # collection conditional statements
# name = ["Leigh", "Inna", "Jam"]
# other_team = ("John", "Janna", "Jane", "Joe")
#
# search = input("Enter name: ")
# if search in name and search in other_team:
#     print(search, "is in the two collections.")
# elif search in name:
#     print(search, "is in the name list.")
# elif search in other_team:
#     print(search, "is in the other_team tuple.")
# else:
#     print(search, "is not in the two list.")
#
# # challenge
# print("Enter grades")
# math = int(input("Math: "))
# science = int(input("Science: "))
# tech = int(input("Tech: "))
#
# avg = (math + science + tech) / 3
# print("Average:", str(round(avg)))
#
# if avg > 100 or avg <= 50:
#     print("Invalid Grade")
# elif avg >= 98:
#     print("With Highest Honor")
# elif avg >= 95:
#     print("With High Honors")
# elif avg >= 90:
#     print("With Honors")
# elif avg >= 75:
#     print("Passed")
# else:
#     print("Failed")
#
#
# # PART 7: WHILE LOOP AND BREAK STATEMENT
# i = 0
# while i < 10:
#     i += 1
#     if i == 6:
#         continue
#     print(i)
# else:
#     print("while loop end")
#
# age = 1
# while age < 18:
#     print("Minor:", age)
#     age += 1
# else:  # run once
#     print("Legal age:", age)
#
# # while loop in collections
# odd = [1, 3, 5, 7, 9]
#
# a = 0
# while a < len(odd):
#     print(odd[a])
#     a += 1
#
# # conditions in while loop
# print("Do your crush like you too?")
# while True:  # infinity unless you use break keyword
#     answer = input("Answer: ")
#     if answer == "No":
#         print("HAHAHAHAHAHAHHAHAHA")
#         break
#     elif answer == "Yes":
#         print("Hmmmm.")
#     else:
#         print("Yes or No")
#
# print("Odd or even?")
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# i = 0
# while i < len(num):
#     if num[i] % 2 == 0:
#         print(num[i], "is an even number.")
#     else:
#         print(num[i], "is an odd number.")
#     i += 1
#
# # challenge - math quiz game
# print("What is the root of 64?")
#
# lives = 3
# while True:
#     print("Lives:", lives)
#     answer = int(input("Answer: "))
#     print()
#     if not answer == 8:
#         lives -= 1
#         if lives == 0:
#             print("Game over.")
#             break
#     else:
#         print("You are correct!")
#         break
#
#
# # PART 8: FOR LOOP AND BREAK KEYWORD
# fruits = ["apples", "banana", "grapes", "mango", "strawberry"]
# for x in fruits:
#     print(x)
# else:
#     print("No more fruits.")
#
# # break keyword in for loop
# for x in range(10):
#     if x == 5:
#         break
#     print(x)  # does not include 5 and so on
#
# # conditions in for loop
# for x in fruits:
#     if x == "grapes":
#         continue  # skips grapes
#     print(x)
#
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for n in num:
#     if n % 2 == 1:
#         print(n, "is an odd number.")
#     else:
#         print(n, "is an even number.")
#
# # range in for loop
# for x in range(5):
#     print(x)
#
# # challenge: account authentication simulation
# usernames = ["leigh", "inna", "jamolin"]
# passwords = ["qwer", "asdf", "zxcv"]
#
# username = input("Enter username: ")
# password = input("Enter password: ")
#
# for x in range(len(usernames)):
#     if username == usernames[x] and password == passwords[x]:
#         print("\nWelcome,", username + "!")
#         break
# else:
#     print("Account not found.")
#
# # PART 9: NESTED FOR LOOP
# # a for loop inside a for loop
#
# # using range
# for x in range(5):
#     for y in range(5):
#         print("*" * x, end="")
#     print("New Line")
#
# # reading multi-dimensional collections
# ccs_students = [
#     ["BSCS", "Leigh"],
#     ["BSIT", "Hermione"],
#     ["BSIS", "Dumbledore"],
#     ["MSIT", "Frankeinstein"],
#     ["MSCS", "Daenerys"]
# ]
#
# print(ccs_students[0][1])
# for list_student in ccs_students:
#     for y in list_student:
#         print(y)
#     print()
#
# # multiplication table
# for x in range(1, 11):
#     for y in range(1, 11):
#         print(x, "x", y, "=", (x * y))
#     print()
#
# # challenge - extracting the data
# students_sample9 = [
#     ["BSIT", ["David", "Alenere"]],
#     ["BSCS", ["Jaymar", "Emman", "Patrick"]]]
# for student_lists in students_sample9:
#     for students in student_lists:
#         print(student_lists[0])
#         for student in student_lists[1]:
#             print(student)
#         print()
#         break
#
# # solution from another programmer
# x = [
#     ['BSIT', ['David','Alenere']],
#     ['BSCS', ['Jaymar', 'Emman', 'Patrick']],
# ]
#
# for courseStudents in x:
#     for listStudents in courseStudents:
#         print(f'{courseStudents[0]}')
#         for students in courseStudents[1]:
#             print(f'    -{students}')
#         print()
#         break
#
# # easier version
# for courseStudents in x:
#     print(courseStudents[0])
#     for students in courseStudents[1]:
#         print("-", students)
#     print()
# import math
# import sys
#
# print()
# # PART 10: FUNCTIONS, PARAMETERS OR ARGUMENTS, RETURN VALUES
#
#
# def sqrtfuc(n):
#     print(math.sqrt(n))
#
#
# num = int(input("Enter a number: "))
# sqrtfuc(num)
#
# # arguments or parameters
#
#
# def greetings(fname, lname):
#     print(f"Hello, {fname} {lname}!")
#
#
# first_name = input("Enter first name: ")
# last_name = input("Enter last name: ")
# greetings(first_name, last_name)
#
# # return values - a value returned after executing a function
# # used to get results from a function that computes or does something that needs a result
#
#
# def add_num(n1, n2):
#     total = n1 + n2
#     return total
#
#
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print(f"{num1} + {num2} = {add_num(num1, num2)}")
#
#
# # calculator
#
#
# def add(n1, n2):
#     sum = n1 + n2
#     return sum
#
#
# def subtract(n1, n2):
#     diff = n1 - n2
#     return diff
#
#
# def multiply(n1, n2):
#     prod = n1 * n2
#     return prod
#
#
# def divide(n1, n2):
#     quotient = n1 / n2
#     return quotient
#
#
# print("Operations:\n+ for add\n- for subtract\n* for multiply\n/ for divide.\nx for exit.")
#
# i = 1
# while i > 0:
#     ope = input("Enter operation: ")
#     if ope == "x":
#         sys.exit()
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))
#
#     if ope == "+":
#         print(f"{num1} {ope} {num2} = {add(num1, num2)}")
#     elif ope == "-":
#         print(subtract(num1, num2))
#     elif ope == "*":
#         print(multiply(num1, num2))
#     elif ope == "/":
#         print(divide(num1, num2))
#     else:
#         print("Wrong input.")
#
#
# # challenge - square a number using functions w/ parameters
#
#
# def square(n):
#     return n * n
#
#
# num = int(input("Input: "))
# print(f"Output: {square(num)}")
#
#
# print()
# # PART 11: ARGUMENTS, ARBITRARY ARGUMENTS, KEYWORD ARGUMENTS
#
#
# def say_hello(name):
#     print("Hello,", name)
#
#
# i = 1
# while i > 0:
#     say_hello(input("Enter a name: "))  # using function to input
#
#
# # arbitrary arguments - asterisk args
# # can't have two in a function, it is neverending
#
#
# def say_hi(*names):  # it converts to tuples, unspecified size
#     for name in names:
#         print("Hi,", name)
#
#
# say_hi("Leigh", "Inna", "Jamolin",)
#
# # keyword arguments(kwargs) - an alternative way for sending arguments inside a function by specifying
# # the parameter name in no certain order. Often used in combination with arbitrary args or if you don't know
# # the order of the arguments in the function.
#
#
# def jaja(fname, lname):
#     print(fname + " " + lname)
#
#
# jaja(lname="Jamolin", fname="Leigh")  # using kwargs
#
#
# def jamolin_fam(*fnames, lname):
#     for fname in fnames:
#         print(fname + " " + lname)
#
#
# jamolin_fam("Lionel", "Gina", "Leigh", "Janna", "Mira", lname="Jamolin")
#
# # arbitrary keyword arguments(**kwargs)
# # used when you are uncertain on what parameter name and how many param you want to pass
#
#
# def students_info(**student):
#     print(student["fname"] + " " + student["lname"])
#     print(f"Age:", student["age"])
#     print(f"Course: " + student["course"])
#
#
# # keywords are always strings
# fname = input("Enter first name: ")
# lname = input("Enter last name: ")
# age = int(input("Enter age: "))
# course = input("Enter course: ")
#
# print("Student #1")
# students_info(fname=fname, lname=lname, course=course, age=age)  # no certain order
#

# challenge - summation program


def summation(*num):
    x = 0
    for n in num:
        x += n
    return x


print(summation(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

