# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
# character_job = "pirate"
# character_ride = "ship"
# character_souvenir = "gold"
# character_pet = "parrot"
#
# print("There was once a " + character_job + " who loved adventure.")
# print("The " + character_job + " would take her " + character_ride + " to unknown places.")
# print("She brings home a lot of " + character_souvenir + ".")
# print("Then she goes home to her pet " + character_pet + ", Chuckles.")
# # is this a comment
#
# favourite_name = "Leigh"
# if favourite_name == "Leigh":
#     print("I like Leigh")
# else:
#     print("the fuck?")
#     print("second line")
#
# print("end")
# print("this is not else statement")
# print(character_pet)
#
# x = 1
# y = 2
#
# print(x + y)
#
# print("Roses are red, violets are blue")
# if 10 > 7:
#     print("Ten is greater than 7")
# if 16 < 42:
#     print("Sixteen is less than forty-two!")
# print("A long time ago in a galaxy far, far away...")
#
# is_leigh_pretty = True
# print(is_leigh_pretty)
#
# # Module 2
# # functions, dev keyword, arguments
#
# def hello_function():
#     print("Hello") # the indented line makes up the body of a function
# hello_function()
#
#
# def welcome_function(f_name, l_name):  # different variable name?
#     print("Welcome, " + f_name + " " + l_name)
#
#
# first_name = input("Enter first name: ")
# last_name = input("Enter last name: ")
# welcome_function(first_name, last_name)
#
#
# def greetings(name):
#     print("Have a nice day, " + name + "!")  # after a class of def, two blank lines is needed, also with inline comment
#
#
# greetings("Leigh")
#
#
# # Input functions
# name = input("Enter name: ")
# print("Hello, " + name)
#
# first_num = int(input("Enter first num: "))
# second_num = int(input("Enter second num: "))
# result = first_num + second_num
# print(str(first_num) + " + " + str(second_num) + " = " + str(result))
#
#
# def add_num(n1, n2):
#     total = n1 + n2
#     return total
#
#
# num1 = int(input("Enter first num: "))
# num2 = int(input("Enter second num: "))
# print("Total: ", add_num(num1, num2))  # I can use comma here
#
# name = input("Name: ")
# age = int(input("Age: "))
# favourite_color = input("Favourite color: ")
# favourite_movie = input("Favourite movie: ")
# mobile_number = input("Mobile number: ")
# motto = input("Motto in life: ")
#
# print("Hi, " + name)
# print("You are " + str(age) + " years old.")
# print("Your fave color is " + favourite_color + " and your fave movie is " + favourite_movie)
# print("Your mobile number is " + mobile_number)
# print("Your motto in life is " + motto)
#
#
# # DATA TYPE AND CONVERSION
#
# this_a_string = "This is a string"
# print(this_a_string)
# name = input("Enter name: ")
# this_an_int = 5
# this_a_float = 3.0
# print(this_an_int)
# print(this_a_float)
# salary = float(input("Enter salary: "))
# print(salary)
# is_hot = True
# print(is_hot)
# print(1 < 2)
# print(2 < 1)
# print(int(33.33))  # Converting a float to an int
# print(float(33))
# print(str(334))
# print(tuple("Leigh Inna"))
# print(list("Leigh Inna"))
#
# # CODING EXERCISES
#
# hmm = 10 < 7
# print(hmm)
#
# num = 73911
# print(str(num))
#
# print(tuple("Thank God it's Friday!"))
#
# print(float(4302))
#
# print(int(3299.35640))
#
#
# def hello_function(first_name, last_name):
#     print("Hello, " + first_name + " " + last_name)
#
#
# hello_function("Leigh", "Molina")
# hello_function("Inna", "Jamolin")
# hello_function("Inna", "Casino")
#
# num1 = int(input("Enter first num: "))
# num2 = int(input("Enter second num: "))
# print("Your two numbers are", num1, "and", num2)
#
#
# # MODULE 3
# # Introducing classes
#
# class NewClass:
#     pass  # empty class with result to error, so put a pass keyword
#
#
# class Pets:
#     looks = "Adorable!"  # class variable
#
#
# hamster = Pets()
# print(hamster.looks)
#
# crocodile = Pets()
# print(crocodile.looks)
#
#
# class Guest:
#     pass
#
#
# g_1 = Guest()
#
# # instance variable is g_1
# g_1.first = "Eve"  # first is attributes
# g_1.last = "Dela Cruz"
# g_1.interest = "Anime"
# g_1.phone = 12345
#
# print(g_1.first, g_1.last)
#
# g_2 = Guest()
#
# g_2.first = "Adam"
# g_2.last = "Perez"
# g_2.interest = "Russian Literature"
# g_2.phone = 54321
#
# print(g_2.first, "interest is", g_2.interest)
#
# # Coding exercises
#
#
# class Customers:
#     greetings = "Welcome to the Coffee Palace"
#
#
# cus1 = Customers()
# cus1.name = "Leigh"
# cus1.beverage = "Yakult"
# cus1.food = "Banana Nutella"
# cus1.total = 699
#
# cus2 = Customers()
# cus2.name = "Inna"
# cus2.beverage = "Coffee"
# cus2.food = "Pork"
# cus2.total = 1000
#
# print(cus1.greetings)
# print(cus2.greetings)
# print(Customers.greetings)
# print(cus1.name, "favourite drink is", cus1.beverage)
# print(cus2.name, "favourite food is", cus2.food)
#
# # arithmetic operators and precedence
# # basic arithmetic operation
# x = 23
# y = 33
# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x % y)  # modulo operator
# print(x // y)  # floor division operator, rounds of the quotient, it's like removing the decimal
# print(x ** y)  # exponentiation operator, uses the second value as an exponent
#
# # precedence
# # almost the same as pemdas
# print((4 - 3) * 6 ** 2)
# print(2 ** 4)
#
# # coding exercise
#
# print(217 * 6)
# print(600 + 35234)
# print(67 // 12)
# print(56329 % 982)
# print(34 ** 5)
#
# # comparison and logical operators
#
# # comparison operators - compare two values and indicate the difference between those two
# x = 20
# y = 11
# print(x == y)  # equal operator
# print(x != y)  # not equal operator
# print(x > y)  # greater than operator
# print(x < y)  # less than operator
# print(x >= y)  # greater than or equal to operator
# print(x <= y)  # less than or equal to operator
#
# # logical operators - combine conditional statements
# print()
# print(x > y and y < x)  # and operator, checks if both true
# print(x > y or x < y)  # or operator, checks if one statement is true
# print(not(x > y and y < x))  # not operator, reverse the result
# print(not(x < y or y > x))  # not operator with or
# print(x < y or y > x)
#
# # coding exercises
#
# my_age = 22
# mom_age = 61
# sis_age = 29
# print(mom_age < sis_age and my_age == 22)
# print(mom_age == 61)
# print(mom_age > 34 or sis_age == 22)
# print(mom_age >= 54)
# print(not(sis_age <= 400 and my_age == 22))
#
# print(324 == 210 or 324 < 527)
# print(9 ** 5)
#
#
# # MODULE 4
# # if elif else
#
# print("It is greater than or less than 69?")
# num = int(input("Enter a number: "))
#
# if num > 69:
#     print("It's greater than 69")
# elif num == 69:
#     print("It's equals to 69")
# else:
#     print("It's less than 69")
#
#
# print("Odd or even?")
# n = int(input("Enter a number: "))
#
# if n % 2 == 0:
#     print(n, "is an even number.")
# else:
#     print(n, "is an odd number.")
#
# # coding exercise
# x = 332
# y = 2031
#
# if x >= y:
#     print(x, "is greater than or equal to", y)
# elif x == y:
#     print(x, "is equal to", y)
# else:
#     print(x, "is less than", y)
#
# # loops and iterations
# # loops - used to iterate until the condition is met
# names = ["Leigh", "Inna", "Jam", "Harry", "Hermione"]
# for x in names:  # this one is like foreach statement in c#
#     print(x)
# for x in "Leigh":  # can be used like this
#     print(x)
# for x in names:
#     if x == "Inna":
#         continue  # skip value of the variable
#     print(x)
# for x in names:
#     if x == "Inna":
#         break  # stop the loop on Inna
#     print(x)
# for x in names:
#     print(x)
#     if x == "Inna":  # stop after Inna
#         break
#
# # using range
# x = range(5)
# for y in x:
#     print(y)  # by default, range always starts with 0
#
# # nested keyword - a loop within a loop
# other_team = ["John", "Janna", "Jane", "Joe", "Jake"]
#
# for x in names:
#     for y in other_team:
#         print(x, y)
#
# # while loops - used to iterate until it becomes false
# i = 1
# while i <= 10:
#     print(i)
#     i += 1  # i = i + 1 or i++
#
# i = 0
# while i < 5:
#     i += 1
#     if i == 3:
#         continue  # skip 3
#     print(i)
# else:
#     print("i is no longer than 5.")  # will run after the iteration
#
# i = 0
# while i < 5:
#     i += 1
#     if i == 3:
#         break  # break after 3
#     print(i)
#
# x = range(3)
# for y in x:
#     print(y)  # output is 0, 1, 2
#
# # coding exercises
#
# furniture = ["table", "chair", "cabinet", "desk", "couch"]
# for x in furniture:
#     if x == "cabinet":
#         continue
#     print(x)
#
# i = 1
# while i < 15:
#     print(i)
#     i += 1
# else:
#     print("i is no longer less than 15.")
#
# # coding challenge
# for x in range(4):
#     print(x)
#
# z = range(1, 11)  # starts with 1 not 0
# for x in z:
#     for y in z:
#         print(x, "x", y, "=", int(x * y))
#     print()
#
# i = 0
# while i < 5:
#     i += 1
#     if i == 4:
#         continue
#     print(i)
# else:
#     print("i is no longer less than 5.")
#
# print(29 % 11)
#
