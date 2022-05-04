# PART 4: SETS
# sets - partially writable, and it's unordered and un-indexed.

evenNum = {2, 4, 8, 10}
print(evenNum)
print(len(evenNum))  # can also use some builtin functions like list

evenNum = list(evenNum)
evenNum[0] = 6
print(evenNum[0])
print(evenNum)
evenNum = set(evenNum)
print(evenNum)

evenNum.add(12)  # can add item at the end of set
print(evenNum)

evenNum.update([14, 16, 18, 20])  # add multiple items through list
extension = [22, 24, 26]
evenNum.update(extension)  # can also use variable inside
print(evenNum)

evenNum.remove(2)  # remove item by value, has error if value doesn't exist
print(evenNum)

evenNum.discard(1)  # delete an item by value, no error
print(evenNum)

evenNum.pop()  # deletes first item
print(evenNum)

evenNum2 = evenNum.copy()  # copy the whole set to another new set
print(evenNum2)

evenNum.clear()  # deletes all the value in set
print(evenNum)

del evenNum  # deletes the set

# union set
set_one = {1, 3, 5, 7, 9}
set_two = {4, 8, 6, 10, 2}
set_union = set_one.union(set_two)  # combine two sets
print(set_union)
print(len(set_union))

# difference set
num1 = {1, 2, 3, 4, 5}
num2 = {1, 2, 6, 7, 8}
# mind what's first set below
num3 = num1.difference(num2)  # return values that only exist on the left/first side
print(num3)  # output is 3, 4, 5

# intersection set
set_inter = num1.intersection(num2)  # returns the same values
print(set_inter)  # output is 1, 2

# symmetric difference set
set_sym = num1.symmetric_difference(num2)  # remove the set that is both on sets
# and returns values that exist exclusively on each set
print(set_sym)  # output is 3, 4, 5, 6, 7, 8

# disjoint set
set_dis = num1.isdisjoint(num2)  # returns a boolean whether two sets have an intersection or not
print(set_dis)  # output is False, because both set has same value even one
odd = {1, 3, 5, 7, 9}
even = {2, 4, 6, 8, 10}
print(odd.isdisjoint(even))  # output is True

# subset
set_sub = num1.issubset(num2)  # returns a boolean whether the left set is contained in the right set
print(set_sub)  # output is False
num = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(even.issubset(num))  # output is True cause all the value in even is in num

# superset
set_sup = num.issuperset(even)  # returns a boolean whether the right set is contained in the left set
print(set_sup)  # output is True cause num is the superset of even
print(num1.issuperset(num2))  # output is False

# casting sets
# you can cast them vice versa
print(list(num))
print(tuple(even))
num = list(num)
print(num)
num = set(num)
print(num)

# nested sets
set_nes = {1, 2, 3, {4, 5, 6}}  # unhashable type: set
