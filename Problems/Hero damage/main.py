hero_damage = 100


def double_damage():
    global hero_damage
    hero_damage *= 2


def disarmed():
    global hero_damage
    hero_damage //= 10


def power_potion():
    global hero_damage
    hero_damage += 100


# hero_damage = 100
# double_damage()
# print(hero_damage)
#
# hero_damage = 100
# disarmed()
# print(hero_damage)
#
# hero_damage = 100
# power_potion()
# print(hero_damage)
