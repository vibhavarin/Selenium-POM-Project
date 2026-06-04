import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    opts = Options()

    # Automatisch erkennen ob CI/CD oder Lokal
    if os.environ.get('CI'):
        opts.add_argument('--headless')
        opts.add_argument('--no-sandbox')
        opts.add_argument('--disable-dev-shm-usage')

    opts.add_experimental_option('prefs', {
        'credentials_enable_service': False,
        'profile.password_manager_enabled': False,
        'profile.password_manager_leak_detection': False
    })
    driver = webdriver.Chrome(options=opts)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()