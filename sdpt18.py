from sdpt18lib.arithmetic import add as a  # import certain function(can also variable, objects, etc)
import sdpt18lib.objects as o  # used as keyword to simplify the name


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(a(num1, num2))

s_one = o.Student("Leigh", 19, "BSCS", 'A')
s_one.introduce()

# GLOBAL VARIABLES
y = "World"


# LOCAL VARIABLES
def say_hello():
    x = "Hello"  # local
    print(x)
    print(y)


say_hello()


# PARAMETER VARIABLES
def say(word):  # also a local variable
    print(word)


say("What")


hi = "Hi"


def say_hi():
    global hi
    hi = "Hello"  # this become a global variable
    print(hi)


say_hi()
print(hi)  # hi variable becomes hello too


# import keyword
# lets you use other files
# are often used in the topmost part of the code
