# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код
source_file = open("test_file/task1_data.txt", mode='r', encoding='utf-8')
resulting_file = open("test_file/task1_answer.txt", mode='w', encoding='utf-8')

for line in source_file.read():
    result = ''.join(i for i in line if not i.isdigit())
    resulting_file.write(result)

source_file.close()
resulting_file.close()
# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
