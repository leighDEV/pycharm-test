# PART 7: WHILE LOOP AND BREAK STATEMENT
i = 0
while i < 10:
    i += 1
    if i == 6:
        continue
    print(i)
else:
    print("while loop end")

age = 1
while age < 18:
    print("Minor:", age)
    age += 1
else:  # run once
    print("Legal age:", age)

# while loop in collections
odd = [1, 3, 5, 7, 9]

a = 0
while a < len(odd):
    print(odd[a])
    a += 1

# conditions in while loop
print("Do your crush like you too?")
while True:  # infinity unless you use break keyword
    answer = input("Answer: ")
    if answer == "No":
        print("HAHAHAHAHAHAHHAHAHA")
        break
    elif answer == "Yes":
        print("Hmmmm.")
    else:
        print("Yes or No")

print("Odd or even?")
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(num):
    if num[i] % 2 == 0:
        print(num[i], "is an even number.")
    else:
        print(num[i], "is an odd number.")
    i += 1

# challenge - math quiz game
print("What is the root of 64?")

lives = 3
while True:
    print("Lives:", lives)
    answer = int(input("Answer: "))
    print()
    if not answer == 8:
        lives -= 1
        if lives == 0:
            print("Game over.")
            break
    else:
        print("You are correct!")
        break
