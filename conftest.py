import pytest

def pytest_addoption(parser):
    parser.addoption("--base_url", help="url", default="https://ya.ru")
    parser.addoption("--status_code", help="status_code", default=200, type=int)

@pytest.fixture
def url(request):
    return request.config.getoption("--base_url")

@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")