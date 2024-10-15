# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string


def generate_random_name():
    letters = string.ascii_lowercase
    while True:
        rand1 = random.randint(1, 15)
        rand2 = random.randint(1, 15)
        first_name = ''
        last_name = ''
        for i in range(rand1):
            first_name += random.choice(letters)

        for i in range(rand2):
            last_name += random.choice(letters)

        yield f'{first_name} {last_name}'


print(next(generate_random_name()))
print(next(generate_random_name()))
print(next(generate_random_name()))
print(next(generate_random_name()))
print(next(generate_random_name()))