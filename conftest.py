import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from utils.data_reader import read_users_csv
from pytest_html import extras
import pathlib
import base64


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()

    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    # 🔥 FIX PARA GITHUB ACTIONS 🔥
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver

    time.sleep(1)
    driver.quit()


@pytest.fixture
def driver_logged(driver):
    login_page = LoginPage(driver)
    user = read_users_csv()[0]
    login_page.login(user["username"], user["password"])
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if not hasattr(report, "extras"):
        report.extras = []

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            screenshots_dir = pathlib.Path("reports/screenshots")
            screenshots_dir.mkdir(parents=True, exist_ok=True)

            file_path = screenshots_dir / f"{item.name}.png"
            driver.save_screenshot(str(file_path))

            # Convertir a base64 (pytest-html 4.x lo requiere)
            with open(file_path, "rb") as f:
                encoded_image = base64.b64encode(f.read()).decode("utf-8")

            report.extras.append(
                extras.image(encoded_image, mime_type="image/png", extension="png")
            )
