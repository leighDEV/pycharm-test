# INIT KEYWORD

class Guest:
    def __init__(self, first, last, interest, phone):  # self represents the instance of our class
        self._first = first  # _first is instance variable, is the above instance variables too?
        self._last = last
        self._interest = interest
        self._phone = phone

    @property
    def first(self):
        return self._first

    @property
    def last(self):
        return self._last

    @property
    def interest(self):
        return self._interest


g_1 = Guest("Eve", "Dela Cruz", "Anime", 12345)
g_2 = Guest("Adam", "Perez", "Russian Literature", 678910)
print(g_1.last)
print(g_2.first)
g_3 = Guest("Mike", "Lim", "Movies", 13456)
print(g_3.interest)


# coding exercises
class Customers:
    greetings = "Welcome to Coffee Palace"  # a class variable

    def __init__(self, name, beverage, food, total):
        self._name = name
        self._beverage = beverage
        self._food = food
        self._total = total

    @property
    def name(self):
        return self._name

    @property
    def beverage(self):
        return self._beverage

    @property
    def food(self):
        return self._food

    @property
    def total(self):
        return self._total


c_2 = Customers("Elaine", "Strawberry fap", "Tuna wrap", 270)
c_4 = Customers("Jerry", "Caramel mach", "Glazed doughnut", 230)

print(Customers.greetings)
print(f"Name: {c_2.name}\n"
      f"Beverage: {c_2.beverage}\n"
      f"Food: {c_2.food}\n"
      f"Total: {c_2.total}")


# INHERITANCE
class User:
    def __init__(self, username, password):
        self._username = username
        self._password = password

    def display(self):
        print(f"Username: {self._username}\nPassword: {self._password}")


class Admin(User):
    def __init__(self, name, username, password):
        self._name = name
        User.__init__(self, username, password)  # it can be written like this and placed here too?

    def display(self):  # overriding
        print(f"Name: {self._name}")
        super().display()


u_1 = User("inna", "qwer")
u_1.display()

a_1 = Admin("Leigh", "leighter", "asdf")
a_1.display()


# CODING EXERCISES
class ClubMembers:
    def __init__(self, name, birthday, age, favourite_food, goal):
        self._name = name
        self._birthday = birthday
        self._age = age
        self._favourite_food = favourite_food
        self._goal = goal

    def introduce(self):
        print("Name:", self._name,
              "\nBirthday:", self._birthday,
              "\nAge:", self._birthday,
              "\nFavourite food:", self._favourite_food,
              "\nGoal:", self._goal)


class ClubOfficers(ClubMembers):
    def __init__(self, name, birthday, age, favourite_food, goal, position):
        super().__init__(name, birthday, age, favourite_food, goal)
        self._position = position

    def introduce(self):
        super().introduce()
        print("Position:", self._position)


cm = ClubMembers("Leigh", "June 06, 2002", 19, "Mami", "Be rich.")
co = ClubOfficers("Inna", "December 13, 1999", 22, "Girls", "Rule the world.", "President")
cm.introduce()
co.introduce()
