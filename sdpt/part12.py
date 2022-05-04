# PART 12: LAMBDA
# a small anonymous function that can take any amount of arguments but can only have one expression
add = lambda x, y: x + y
print(add(1, 2))
print(add(2, 3))

# challenge - triple any number
tripler = lambda x: x * 3
print(tripler(int(input("Enter any number: "))))
