# PART 9: NESTED FOR LOOP
# a for loop inside a for loop

# using range
for x in range(5):
    for y in range(5):
        print("*" * x, end="")
    print("New Line")

# reading multi-dimensional collections
ccs_students = [
    ["BSCS", "Leigh"],
    ["BSIT", "Hermione"],
    ["BSIS", "Dumbledore"],
    ["MSIT", "Frankeinstein"],
    ["MSCS", "Daenerys"]
]

print(ccs_students[0][1])
for list_student in ccs_students:
    for y in list_student:
        print(y)
    print()

# multiplication table
for x in range(1, 11):
    for y in range(1, 11):
        print(x, "x", y, "=", (x * y))
    print()

# challenge - extracting the data
students_sample9 = [
    ["BSIT", ["David", "Alenere"]],
    ["BSCS", ["Jaymar", "Emman", "Patrick"]]]
for student_lists in students_sample9:
    for students in student_lists:
        print(student_lists[0])
        for student in student_lists[1]:
            print(student)
        print()
        break

# solution from another programmer
x = [
    ['BSIT', ['David', 'Alenere']],
    ['BSCS', ['Jaymar', 'Emman', 'Patrick']],
]

for courseStudents in x:
    for listStudents in courseStudents:
        print(f'{courseStudents[0]}')
        for students in courseStudents[1]:
            print(f'    -{students}')
        print()
        break

# easier version
for courseStudents in x:
    print(courseStudents[0])
    for students in courseStudents[1]:
        print("-", students)
    print()
