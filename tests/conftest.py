
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Браузер для тестов: chrome, firefox или edge")
    parser.addoption("--browser-version", action="store", default="latest", help="Версия браузера")
