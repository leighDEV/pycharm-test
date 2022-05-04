# MODULE 4
# if elif else

print("It is greater than or less than 69?")
num = int(input("Enter a number: "))

if num > 69:
    print("It's greater than 69")
elif num == 69:
    print("It's equals to 69")
else:
    print("It's less than 69")


print("Odd or even?")
n = int(input("Enter a number: "))

if n % 2 == 0:
    print(n, "is an even number.")
else:
    print(n, "is an odd number.")

# coding exercise
x = 332
y = 2031

if x >= y:
    print(x, "is greater than or equal to", y)
elif x == y:
    print(x, "is equal to", y)
else:
    print(x, "is less than", y)

# loops and iterations
# loops - used to iterate until the condition is met
names = ["Leigh", "Inna", "Jam", "Harry", "Hermione"]
for x in names:  # this one is like foreach statement in c#
    print(x)
for x in "Leigh":  # can be used like this
    print(x)
for x in names:
    if x == "Inna":
        continue  # skip value of the variable
    print(x)
for x in names:
    if x == "Inna":
        break  # stop the loop on Inna
    print(x)
for x in names:
    print(x)
    if x == "Inna":  # stop after Inna
        break

# using range
x = range(5)
for y in x:
    print(y)  # by default, range always starts with 0

# nested keyword - a loop within a loop
other_team = ["John", "Janna", "Jane", "Joe", "Jake"]

for x in names:
    for y in other_team:
        print(x, y)

# while loops - used to iterate until it becomes false
i = 1
while i <= 10:
    print(i)
    i += 1  # i = i + 1 or i++

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # skip 3
    print(i)
else:
    print("i is no longer than 5.")  # will run after the iteration

i = 0
while i < 5:
    i += 1
    if i == 3:
        break  # break after 3
    print(i)

x = range(3)
for y in x:
    print(y)  # output is 0, 1, 2

# coding exercises

furniture = ["table", "chair", "cabinet", "desk", "couch"]
for x in furniture:
    if x == "cabinet":
        continue
    print(x)

i = 1
while i < 15:
    print(i)
    i += 1
else:
    print("i is no longer less than 15.")

# coding challenge
for x in range(4):
    print(x)

z = range(1, 11)  # starts with 1 not 0
for x in z:
    for y in z:
        print(x, "x", y, "=", int(x * y))
    print()

i = 0
while i < 5:
    i += 1
    if i == 4:
        continue
    print(i)
else:
    print("i is no longer less than 5.")

print(29 % 11)

