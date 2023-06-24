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

def generate_random_name():
    """ Генератор двух слов из латинских букв от 1 до 15 символов, разделенных пробелами """
    simbols = 'abcdefghijklmnopqrstuvwxyz'
    while True:
        size_first_world = random.randrange(1, 16)
        size_second_world = random.randrange(1, 16)
        name = ''.join(random.choices(simbols, k=size_first_world)) + \
               ' ' + ''.join(random.choices(simbols, k=size_second_world))
        yield name


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
