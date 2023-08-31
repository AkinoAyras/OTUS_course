import pytest

def pytest_addoption(parser):
    parser.addoption('--url', action='store', default='https://ya.ru', help='Test base URL')
    parser.addoption('--status_code', action='store', default=200, help='Default status code for the test')

@pytest.fixture
def url(request):
    return request.config.getoption('--url')

@pytest.fixture
def status_code(request):
    return request.config.getoption('--status_code')

