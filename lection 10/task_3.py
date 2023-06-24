# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('test_data, result', [
    pytest.param((100, 50), 2, marks=pytest.mark.smoke('smoke test')),
    pytest.param((30, 6, 2), 2.5, marks=pytest.mark.skip('skipped test')),
    ((99999, 521, 10, -245), -0.07834149398723021),
    ((99, 0), 'division by zero'),
    (('a', 'b'), "unsupported operand type(s) for /=: 'str' and 'str'")
])
def test_division(test_data, result):
    try:
        assert all_division(*test_data) == result
    except Exception as error:
        assert error.args[0] == result

