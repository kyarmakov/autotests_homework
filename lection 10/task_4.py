# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.
import time

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.usefixtures('class_measure_time')
class TestDivision:

    def test_divide_ints(self):
        assert 2.5 == all_division(5, 2)

    def test_divide_floats(self, method_measure_time):
        time.sleep(1)
        assert 1.2 == all_division(2.4, 2.0)

    def test_divide_by_zero(self, method_measure_time):
        with pytest.raises(ZeroDivisionError):
            all_division(3, 0)

    def test_divide_negative(self, method_measure_time):
        assert -2.5 == all_division(5, -2)

    def test_divide_negatives(self):
        assert 2.5 == all_division(-5, -2)
