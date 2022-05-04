# PART 6: CONDITIONAL STATEMENTS
name = input("Enter name: ")
age = int(input("Enter age: "))

if age >= 18:
    registered = input("Are you registered? Yes or No? ")
    if registered == "Yes":
        print("You are qualified to vote!")
    else:
        print("Please register first.")
else:
    print("You are not yet qualified to vote.")
print("\nThank you for using the program.")

# not keyword
math_grades = int(input("Enter math grades: "))

if not math_grades >= 95:
    print("You are so bobo.")
else:
    print("Thumbs up!")

# logical operators
username = input("Enter username: ")
password = input("Enter password: ")

if (username == "leighter" and password == "asdf") or (username == "Innay" and password == "qwer"):
    print("Welcome,", username)
else:
    print("Login failed.")

# collection conditional statements
name = ["Leigh", "Inna", "Jam"]
other_team = ("John", "Janna", "Jane", "Joe")

search = input("Enter name: ")
if search in name and search in other_team:
    print(search, "is in the two collections.")
elif search in name:
    print(search, "is in the name list.")
elif search in other_team:
    print(search, "is in the other_team tuple.")
else:
    print(search, "is not in the two list.")

# challenge
print("Enter grades")
math = int(input("Math: "))
science = int(input("Science: "))
tech = int(input("Tech: "))

avg = (math + science + tech) / 3
print("Average:", str(round(avg)))

if avg > 100 or avg <= 50:
    print("Invalid Grade")
elif avg >= 98:
    print("With Highest Honor")
elif avg >= 95:
    print("With High Honors")
elif avg >= 90:
    print("With Honors")
elif avg >= 75:
    print("Passed")
else:
    print("Failed")
