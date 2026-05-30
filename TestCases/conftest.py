import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

@pytest.fixture()
def driver():
    opts = Options()
    opts.add_experimental_option('detach', True)
    opts.add_experimental_option('prefs', {
    'credentials_enable_service': False,
    'profile.password_manager_enabled': False,
    'profile.password_manager_leak_detection': False
    })
    driver = webdriver.Chrome(options=opts)
    driver.implicitly_wait(10)
    yield driver
    driver.close()