# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('a, b, result', [pytest.param(5, 2, 2.5, marks=pytest.mark.skip('skipping test')),
                                          pytest.param(2.4, 2.0, 1.2, marks=pytest.mark.smoke),
                                          (3, 0, 'division by zero'), (5, -2, -2.5), (-5, -2, 2.5)])
def test_all_division(a, b, result):
    try:
        assert result == all_division(a, b)
    except Exception as e:
        assert result == str(e)
