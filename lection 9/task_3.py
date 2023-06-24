# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
with open("test_file/task_3.txt", 'r', encoding='utf-8') as file:
    file_lines = [file_line.rstrip() for file_line in file.readlines()]
    sum_price = 0
    list_sum = []
    for line in file_lines:
        if line != '':
            sum_price += int(line)
        else:
            list_sum.append(sum_price)
            sum_price = 0
    list_sum = sorted(list_sum, reverse=True)[0: 3]
    three_most_expensive_purchases = sum(list_sum)

assert three_most_expensive_purchases == 202346
