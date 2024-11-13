import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


LOGIN_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    browser_version = request.config.getoption("--browser-version")

    if browser_name == "chrome":
        options = ChromeOptions()
        service = ChromeService()
        options.add_argument(f"--version={browser_version}")
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        service = FirefoxService()
        options.add_argument(f"--version={browser_version}")
        driver = webdriver.Firefox(service=service, options=options)
    elif browser_name == "edge":
        options = EdgeOptions()
        service = EdgeService()
        options.add_argument(f"--version={browser_version}")
        driver = webdriver.Edge(service=service, options=options)
    else:
        raise ValueError(f"Браузер {browser_name} не поддерживается")

    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_login(browser):
    browser.get(LOGIN_URL)
    browser.find_element(By.ID, "user-name").send_keys(USERNAME)
    browser.find_element(By.ID, "password").send_keys(PASSWORD)
    browser.find_element(By.ID, "login-button").click()

    assert browser.current_url != LOGIN_URL, "Не удалось пройти аутентификацию"
    assert browser.find_element(By.CLASS_NAME, "inventory_list"), "Таблица с товарами не отображается"
    time.sleep(3)


def test_logout(browser):
    browser.get(LOGIN_URL)
    browser.find_element(By.ID, "user-name").send_keys(USERNAME)
    browser.find_element(By.ID, "password").send_keys(PASSWORD)
    browser.find_element(By.ID, "login-button").click()

    menu_button = browser.find_element(By.ID, "react-burger-menu-btn")
    menu_button.click()
    logout_button = browser.find_element(By.ID, "logout_sidebar_link")
    logout_button.click()

    assert browser.current_url == LOGIN_URL, "Не удалось выйти из аккаунта"
    time.sleep(3)
