import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

opts = Options()
opts.add_experimental_option('detach', True)
opts.add_experimental_option('prefs', {
    'credentials_enable_service': False,
    'profile.password_manager_enabled': False,
    'profile.password_manager_leak_detection': False
})

driver = webdriver.Chrome(options=opts)
driver.get('https://the-internet.herokuapp.com/login')
time.sleep(2)

driver.find_element('id', 'username').send_keys('tomsmith')
driver.find_element('id', 'password').send_keys('SuperSecretPassword!')
driver.find_element('xpath', '//button[@type="submit"]').click()

time.sleep(2)

# 👇 Nur diese 2 Zeilen neu hinzufügen:
driver.switch_to.active_element.send_keys(Keys.TAB)
driver.switch_to.active_element.send_keys(Keys.ENTER)

print("✅ Login erfolgreich!")

driver.find_element('xpath','//a[@class="button secondary radius"]').click()

