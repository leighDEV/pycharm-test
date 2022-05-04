# MODULE 2: DICTIONARIES
# WHAT IS DICTIONARIES?
# it's like a warehouse. it contains set of key-value pairs.
# keys can be a string or a number while values can be any data type.

shopping_list = {"weird hat": 150,
                 "purple rug": 450,
                 "old book": 200,
                 "stuffed elephant": 50}

print(shopping_list)  # printing the whole dict

# using lists as values
basketball_teams = {"sith": ["Leigh", "Inna", "Jamolin"],
                    "jedi": ["DC", "Taylor", "Leia"]}

print(basketball_teams["sith"])  # getting the value of the key
print(basketball_teams["jedi"][1])  # getting the element inside the value(list)

# using different data types as values
anime_character = {"name": {"Eren"}, "age": 19, "friends": ["Mikasa", "Armin"], "alive": False}

# empty dictionary
empty_dict = {}
print(empty_dict)  # output is {}

# adding new key to the dict
shopping_list["plastic ring"] = 20

# overwriting existing key
shopping_list["stuffed elephant"] = 80
print(shopping_list)

# adding more than one item to dict
basketball_teams.update({"avengers": ["Toeny", "Steve", "Nat"], "justice league": ["Kael", "Bruce", "Arthur"]})
print(basketball_teams)

# combining two lists and turn them into one dict
relative = ["Tita", "Tito", "Lola", "Lolo"]
age = [33, 45, 69, 66]
rel_age = zip(relative, age)  # combined the two lists
print(list(rel_age))  # convert them into list
print(dict(rel_age))  # convert them into dict


# CODING EXERCISES
flavor = ["vanilla", "chocolate", "strawberry", "cookies n' cream", "bubblegum"]
toppings = ["almonds", "banana slices", "chocolate syrup", "caramel syrup", "white chocolate chips"]

ice_cream = dict(zip(flavor, toppings))
print(ice_cream)
ice_cream["chocolate"] = "blueberries"  # overwriting the value
ice_cream.update({"matcha": "pistachios", "ube": "mango slices"})
print(ice_cream)


# USING DICTIONARIES
# getting a key
print(ice_cream["bubblegum"])  # getting the value using key

# key error - an error when there's no certain key in dict
check_key = "cheese"

if check_key in ice_cream:  # using conditional statement to avoid key error
    print(check_key, "is in the dict")
else:
    print(check_key, "is not in the dict")

# using get function
print(ice_cream.get("vanilla"))  # getting the value of this
print(ice_cream.get("cheese"))

# deleting a key
ice_cream.pop("ube")
ice_cream.popitem()  # deleting the last item
print(ice_cream)

# getting all the keys
print(ice_cream.keys())

# getting all the values
print(ice_cream.values())

# returning a list containing a tuple for each key value pair
print(ice_cream.items())


# CODING EXERCISES
groceries = {"chicken": 8, "apples": 6, "cucumbers": 3, "milk": 2, "oranges": 4}
groceries.pop("oranges")
print(groceries)

speakers = {"Sir Rafael": 54, "Ms. Joan": 33, "Ms. Dana": 67}
print(speakers.keys())

swimming_team = {"Carl": "passed", "Quentin": "failed", "John Y": "passed", "Jorge": "failed"}
print(swimming_team.get("Jorge"))  # checking if Jorge failed or not


# LOOPING THROUGH DICTIONARIES

# using .items method
for key, value in swimming_team.items():
    print(key, ":", value)

# using .keys method
for name in swimming_team.keys():
    print(name)

# using continue
for name in swimming_team.keys():
    if name == "John Y":
        continue  # skip John Y
    print(name)

# using .values method
for result in swimming_team.values():
    print(result)

# nested keyword - dict within a dict
cat = {1: {"name": "Sweetie", "age": 12, "color": "white"},
       2: {"name": "Pussy", "age": 1, "color": "pink"}}

print(cat)

# accessing elements
print(cat[1]["color"])
print(cat[2]["name"])

# creating new dict using empty {}
cat[3] = {}
cat[3]["name"] = "pretty"
cat[3]["age"] = 2
cat[3]["color"] = "black"
cat[3]["personality"] = "naughty"
print(cat)

# other ways to add dictionaries
cat[4] = {"name": "pp", "age": 5, "color": "brown"}
print(cat)
