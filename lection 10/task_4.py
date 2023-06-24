# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
import time


@pytest.mark.usefixtures('print_time')
class TestFixt:

    def test_one(self):
        print('Test 1')
        time.sleep(2)

    @pytest.mark.usefixtures('show_duration')
    def test_two(self):
        print('Test 2')
        time.sleep(2)
