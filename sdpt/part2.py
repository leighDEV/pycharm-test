# PART 2: VARIABLES, DATA TYPES, AND INPUT

first_name = "Leigh"
last_name = "Jamolin"
x = 10
y = 12.33
is_tall = False

print(first_name + " " + last_name)
print(first_name + last_name)
deci = 12.3300
print(deci)
# cannot concatenate int

jaja = "Jaja"
num = 3
print(jaja + str(num))

# user input is always in string format
name = input("Enter name: ")
print("Welcome, " + name)
t = input("Enter first num: ")
r = input("Enter second num: ")
print(int(x) + int(y))

salary = input("Enter salary: ")
another = input("Enter random int: ")
print(float(salary) + int(another))

yy = 23.33
dd = 3
print(yy + dd)

xx = float(input("Enter first num: "))
yy = float(input("Enter second num: "))
ope = input("Enter operator: ")

if ope == "+":
    result = xx + yy
    print(str(xx) + " + " + str(yy) + " = " + str(result))
elif ope == "-":
    result = xx - yy
elif ope == "*":
    print(xx * yy)
elif ope == "/":
    print(xx / yy)
else:
    print("Wrong operator.")
