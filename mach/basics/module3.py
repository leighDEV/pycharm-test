# MODULE 3
# Introducing classes

class NewClass:
    pass  # empty class with result to error, so put a pass keyword


class Pets:
    looks = "Adorable!"  # class variable


hamster = Pets()
print(hamster.looks)

crocodile = Pets()
print(crocodile.looks)


class Guest:
    pass


g_1 = Guest()

# instance variable is g_1
g_1.first = "Eve"  # first is attributes
g_1.last = "Dela Cruz"
g_1.interest = "Anime"
g_1.phone = 12345

print(g_1.first, g_1.last)

g_2 = Guest()

g_2.first = "Adam"
g_2.last = "Perez"
g_2.interest = "Russian Literature"
g_2.phone = 54321

print(g_2.first, "interest is", g_2.interest)

# Coding exercises


class Customers:
    greetings = "Welcome to the Coffee Palace"


cus1 = Customers()
cus1.name = "Leigh"
cus1.beverage = "Yakult"
cus1.food = "Banana Nutella"
cus1.total = 699

cus2 = Customers()
cus2.name = "Inna"
cus2.beverage = "Coffee"
cus2.food = "Pork"
cus2.total = 1000

print(cus1.greetings)
print(cus2.greetings)
print(Customers.greetings)
print(cus1.name, "favourite drink is", cus1.beverage)
print(cus2.name, "favourite food is", cus2.food)

# arithmetic operators and precedence
# basic arithmetic operation
x = 23
y = 33
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)  # modulo operator
print(x // y)  # floor division operator, rounds of the quotient, it's like removing the decimal
print(x ** y)  # exponentiation operator, uses the second value as an exponent

# precedence
# almost the same as pemdas
print((4 - 3) * 6 ** 2)
print(2 ** 4)

# coding exercise

print(217 * 6)
print(600 + 35234)
print(67 // 12)
print(56329 % 982)
print(34 ** 5)

# comparison and logical operators

# comparison operators - compare two values and indicate the difference between those two
x = 20
y = 11
print(x == y)  # equal operator
print(x != y)  # not equal operator
print(x > y)  # greater than operator
print(x < y)  # less than operator
print(x >= y)  # greater than or equal to operator
print(x <= y)  # less than or equal to operator

# logical operators - combine conditional statements
print()
print(x > y and y < x)  # and operator, checks if both true
print(x > y or x < y)  # or operator, checks if one statement is true
print(not(x > y and y < x))  # not operator, reverse the result
print(not(x < y or y > x))  # not operator with or
print(x < y or y > x)

# coding exercises

my_age = 22
mom_age = 61
sis_age = 29
print(mom_age < sis_age and my_age == 22)
print(mom_age == 61)
print(mom_age > 34 or sis_age == 22)
print(mom_age >= 54)
print(not(sis_age <= 400 and my_age == 22))

print(324 == 210 or 324 < 527)
print(9 ** 5)
