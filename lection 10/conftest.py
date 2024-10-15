import time

import pytest


@pytest.fixture(scope='class')
def class_measure_time():
    start_time = time.time()
    yield
    end_time = time.time()
    print(f'Время выполнения класса: {end_time - start_time}')


@pytest.fixture
def method_measure_time():
    start_time = time.time()
    yield
    end_time = time.time()
    print(f'Время выполнения метода: {end_time - start_time}')
