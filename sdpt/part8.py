# PART 8: FOR LOOP AND BREAK KEYWORD
fruits = ["apples", "banana", "grapes", "mango", "strawberry"]
for x in fruits:
    print(x)
else:
    print("No more fruits.")

# break keyword in for loop
for x in range(10):
    if x == 5:
        break
    print(x)  # does not include 5 and so on

# conditions in for loop
for x in fruits:
    if x == "grapes":
        continue  # skips grapes
    print(x)

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in num:
    if n % 2 == 1:
        print(n, "is an odd number.")
    else:
        print(n, "is an even number.")

# range in for loop
for x in range(5):
    print(x)

# challenge: account authentication simulation
usernames = ["leigh", "inna", "jamolin"]
passwords = ["qwer", "asdf", "zxcv"]

username = input("Enter username: ")
password = input("Enter password: ")

for x in range(len(usernames)):
    if username == usernames[x] and password == passwords[x]:
        print("\nWelcome,", username + "!")
        break
else:
    print("Account not found.")
