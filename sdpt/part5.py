# PART 5: DICTIONARY | LIST OF DICTIONARIES
# a collection of Key Pairs that is unordered , changeable and indexed
student_one = {
    "name": "Leigh",
    "age": 19,
    "course": "BSCS"
}

student_two = {
    "name": "Inna",
    "age": 18,
    "course": "BSIT"
}

print(student_one)  # reading the whole dict
print(student_two)
print(student_one["name"])  # reading the value of key "Name"
print(student_two["course"])
print(student_one.get("age"))  # reading value by using get
print(student_two.get("name"))

student_two["age"] = 19  # changing the value
print(student_two)

print(len(student_one))  # checking the number of items

student_one["town"] = "Famy"  # adding items
print(student_one)

student_one.pop("town")  # deletes an item based on their key value
print(student_one)

student_two.popitem()  # deletes the last item
print(student_two)

student_two.clear()  # clears all the items
print(student_two)

del student_two  # deletes the dict

student_three = student_one.copy()  # copies the whole dict to another dict
print(student_three)

print(student_three.keys())  # getting all keys in dict
print(student_three.values())  # getting all values in dict

students = [student_one, student_three]  # dicts inside a list
print(students)
print(students[0])  # returns a dict from a list
print(students[0].get("name"))  # getting item of a dict in a list

# nested dictionaries
student_four_grades = {
    "math": 99,
    "science": 98,
    "english": 97
}

student_four = {
    "name": "Inna",
    "age": 19,
    "course": "BSCS",
    "grades": student_four_grades  # nesting dict
}
print(student_four)
print(student_four.get("grades").get("math"))  # getting the item from the nested dict
