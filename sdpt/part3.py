# PART 3: LIST AND TUPLES
# list - a read and write collection of variables
names = ["Leigh", "Inna", "Jam", "Harry", "Hermione"]
print(names[2:])
print(names[:3])  # end index item is excluded
print(names[1:4])

# Assigning list items, also works with numbers
names[3] = "Ron"  # replacing harry with ron
print(names)
print(len(names))
names[1] = "Leigh"
print(names.count("Leigh"))  # counting the leigh in the value, case sensitive
names.append("Leigh")  # appending an item in the list
print(len(names))
print(names)
names.insert(2, "Inna")  # inserting an item in the middle of list
print(names)
names.remove("Leigh")  # I think it will remove the latest leigh in the list, not all
print(names)
names.pop(-2)  # deleting item bases on index
names.pop()  # deleting last item
print(names)
del names[2]  # deletes item bases on index
print(names)
del names  # deletes whole list
names = ["Leigh", "Inna", "Jam"]
print(names)
print(names.clear())  # clear all items in list but not list, output is None
print(names)  # output is square brackets
names = ["Leigh", "Inna", "Jam"]
group_members = names.copy()  # copying the items in names to this list
print("Names list:", names)
print("Group members:", group_members)
# sequencing is very important, sabi sa tutorial
duplicate = names + group_members
print("Combined list:", duplicate)
other_team = ["John", "Janna", "Jane"]
print(other_team.extend(group_members))  # not working? output is None
other_team.append(group_members)
print(other_team)  # append list inside a list
names.reverse()  # reversing the items in list
print(names)
# print(names.reverse()) - I think this is not working when I put the function inside print function? Output is None
names.sort()  # sort the list in ascending order
print(names)
names.sort(reverse=True)  # sort list in descending order
print(names)
alphabet = ['A', 'B', 'C', 'Z', 'X', 'N', 'O', 'M']
alphabet.sort(reverse=True)
print(alphabet)

# nested lists
# index =    0        1       2                             3                                     4
# index =                                       0               1        2       3        1       2          3
# index =                              0        1       2
courses = ["BSCS", "BSIT", "BSIS", [["DSCS", "DSIT", "DSIS"], "MSCS", "MSIT", "MSIS"], ["GOD", "MASTER", "EMPRESS"]]
print(courses)
print(courses[2])  # output is BSIS
print(courses[3])  # output is the list of d and m
print(courses[4])  # output is list of god
print(courses[4][1])  # output is MASTER
print(courses[3][0])  # output is list of d
print(courses[3][0][0])  # output is DSCS, this has 3 index because it's a list inside a list of a list
print(courses[3][1])  # output is MSCS

# tuples - a read only collection
# can use some functions of list here
# can read, combined, delete completely but can't be assigned, can't delete one by one
# usually use in constants, formula like pi
print()
tup_courses = ("BSCS", "BSIT", "BSIS")
print(tup_courses)
del tup_courses
tup_names = ("Leigh", "Inna", "Jam", ("John", "Janna", "Jane"))  # nested tuples
print(tup_names[3])

# casting tuples and lists
tup_names = list(tup_names)  # useful when you want to edit your tuple
courses = tuple(courses)
print(tup_names)
print(courses)
