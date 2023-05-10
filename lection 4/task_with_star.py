# Задача со ЗВЁЗДОЧКОЙ. Решать НЕ обязательно.
# Программа получает на вход натуральное число num.
# Программа должна вывести другое натуральное число, удовлетворяющее условиям:
# Новое число должно отличаться от данного ровно одной цифрой
# Новое число должно столько же знаков как исходное
# Новое число должно делиться на 3
# Новое число должно быть максимально возможным из всех таких чисел
# Например (Ввод --> Вывод) :
#
# 379 --> 879
# 15 --> 75
# 4974 --> 7974

def max_division_by_3(num):
    tmp_num = num
    ranks = [int(x) for x in str(tmp_num)]
    max_by_ranks = []

    rank_order = 0
    for rank in ranks:
        for digit in reversed(range(0, 10)):
            if rank == digit or (rank_order == 0 and digit == 0):
                continue
            tmp_ranks = ranks.copy()
            tmp_ranks.pop(rank_order)
            tmp_ranks.insert(rank_order, digit)
            tmp_rank_sum = sum(tmp_ranks)
            if not tmp_rank_sum % 3:
                max_by_ranks.append(int(''.join(str(x) for x in tmp_ranks)))
                break
        rank_order += 1
    return max(max_by_ranks)

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    379, 810, 981, 4974, 996, 9000, 15, 0, 9881, 9984, 9876543210, 98795432109879543210
]

test_data = [
    879, 870, 987, 7974, 999, 9900, 75, 9, 9981, 9987, 9879543210, 98798432109879543210
]


for i, d in enumerate(data):
    assert max_division_by_3(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
