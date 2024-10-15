# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.smoke
def test_divide_ints():
    assert 2.5 == all_division(5, 2)


@pytest.mark.smoke
def test_divide_floats():
    assert 1.2 == all_division(2.4, 2.0)

@pytest.mark.smoke
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(3, 0)


def test_divide_negative():
    assert -2.5 == all_division(5, -2)


def test_divide_negatives():
    assert 2.5 == all_division(-5, -2)
