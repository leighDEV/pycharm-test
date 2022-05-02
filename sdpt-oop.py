# PART 13: OOP | CLASSES AND OBJECTS

class Enemy:
    name = "Name"  # default value
    hp = 100
    mp = 50
    atk = 12
    lvl = 1


enemy_one = Enemy()
enemy_one.name = "Leigh"
enemy_one.hp = 99
enemy_one.mp = 50
enemy_one.atk = 8
enemy_one.lvl = 99

enemy_two = Enemy()
enemy_two.name = "Inna"

print(enemy_one.name)
print(enemy_two.name)


class Product:
    brand = "Brand"
    id = 1000
    qty = 0


product_one = Product()
product_one.brand = "Tesla"
product_one.id = 999
product_one.qty = 9

print(product_one.brand)
print(product_one.id)
print(product_one.qty)

product_two = Product()
