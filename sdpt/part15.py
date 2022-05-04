# PART 15: OBJECT FUNCTIONS
# also called methods (functions inside a class) - represent the object's purpose
# constructors are also an object functions

class Animal:
    def __init__(self, a_type, sound):
        self.type = a_type
        self.sound = sound

    def speak(self):  # methods always have self parameter at first
        print(f"{self.type}: {self.sound}")


animal_dog = Animal("Dog", "Woof")
animal_dog.speak()
animal_cat = Animal("Cat", "Meow")
animal_cat.speak()


# challenge - user in a social media

class User:
    def __init__(self, first_name, last_name, likes_count, friends_name):
        self.first_name = first_name
        self.last_name = last_name
        self.likes_count = likes_count
        self.friends_name = friends_name
        print(f"User created. Welcome, {self.first_name}!")

    def introduce(self):
        print(f"Hi, I am  {self.first_name} {self.last_name}!")

    def full_profile(self):
        print(f"Full name: {self.first_name} {self.last_name}")
        print(f"Likes    : {str(self.likes_count)}")
        print("Friends  : ")
        for friend in self.friends_name:  # this is a list
            print(" -" + friend)


user_one = User("Leigh", "Jamolin", 10, ["Harry", "Ron", "Hermione"])
user_one.introduce()
user_one.full_profile()

print()
user_two = User("Hermione", "Granger", 99, ["Harry", "Ron", "Ginny"])
user_two.introduce()
user_two.full_profile()
