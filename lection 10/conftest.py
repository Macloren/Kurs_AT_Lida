import datetime
import pytest


@pytest.fixture(scope='class')
def print_time():
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'Время начала выполнения: {now}\n')
    yield  # выполнение тестов
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'\nВремя завершения выполнения: {now}\n')


@pytest.fixture
def show_duration():
    time = datetime.datetime.now()
    yield
    duration = datetime.datetime.now() - time
    print(f'Время выполнения: {duration}')
