# Напишите класс Trigon, для инициализации передаётся неизвестное кол-во атрибутов

# В классе при инициализации происходит проверка на корректность переданных данных и генерируются следующие исключения:

# 1) Если хотя бы одна сторона передана не числом,
# то падаем с TypeError и текстом 'Стороны должны быть числами'

# 2) Если хотя бы одна сторона передана нулем или отрицательным числом,
# то падаем с ValueError и текстом 'Стороны должны быть положительными'

# 3) Если не соблюдается неравенство треугольника,
# то Exception и текст "Не треугольник"

# 4) Если передано не 3 аргумента, то IndexError "Передано {n} аргументов, а ожидается 3", где n - кол-во аргументов

import unittest  # Не удалять


class Trigon:
    def __init__(self, *side):

        """
        Метод инициализации класса Trigon
        при инициализации происходит проверка на корректность переданных данных.
        Если хотя бы одна сторона передана не числом возвращаем исключение 'Стороны должны быть числами'.
        Если хотя бы одна сторона передана нулем или отрицательным числом.
        возвращаем исключение 'Стороны должны быть положительными'
        Если не соблюдается неравенство треугольника возвращаем исключение 'Не треугольник'.
        Если передано не 3 аргумента возвращаем исключение 'Передано {n} аргументов, а ожидается 3'.
        :param side: переданные атрибуты (стороны треугольника)
        """
        if len(side) != 3:
            raise IndexError(f'Передано {len(side)} аргументов, а ожидается 3')
        try:
            self.a, self.b, self.c = [int(val) for val in sorted(side)]
        except TypeError:
            raise TypeError('Стороны должны быть числами')
        if any(number <= 0 for number in (self.a, self.b, self.c)):
            raise ValueError('Стороны должны быть положительными')
        elif self.a + self.b <= self.c:
            raise Exception('Не треугольник')

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


class MyTestCase(unittest.TestCase):

    def test(self):
        data = [(3, '7', 5), (-3, 7, 5), (2, 5, 2), (3, 4, 5, 6), (3, 4), (3, 4, 5)]

        test_data = [('Стороны должны быть числами', 'TypeError'),
                     ('Стороны должны быть положительными', 'ValueError'),
                     ("Не треугольник", 'Exception'),
                     ("Передано 4 аргументов, а ожидается 3", 'IndexError'),
                     ("Передано 2 аргументов, а ожидается 3", 'IndexError'),
                     0]
        for i, d in enumerate(data):
            try:
                Trigon(*data[i])
            except Exception as e:
                assert e.args[0] == test_data[i][0], 'Исключение имеет неправильный текст'
                assert type(e).__name__ == test_data[i][1], 'У исключения неправильный тип'

        print('Всё ок')


if __name__ == '__main__':
    unittest.main()
