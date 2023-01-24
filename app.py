from selenium import webdriver
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import requests
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


API_KEY = 0 """Enter your own API KEY here"""
CHAT_ID = 0 """Enter your own CHAT ID here"""

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
op.add_argument('--headless')
op.add_argument('--no-sandbox')
op.add_argument('--disable-dev-sh-usage')
print('PATH - ', os.environ.get('CHROMEDRIVER_PATH'))
driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), options=op)

driver.maximize_window()

actions = ActionChains(driver)

link = 'https://www.apple.com/shop/buy-iphone/iphone-14-pro/6.7-inch-display-256gb-space-black-unlocked'
wait = WebDriverWait(driver, 30)
clickable_field_xpath = '//*[@id="4b1d0d20-7808-11ed-810b-ef1b0b335c14_label"]'
driver.get(link)
clickable_field = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH, clickable_field_xpath
                ))
            )
time.sleep(4)

apple_care_label = driver.find_element('xpath', '//*[@id="applecareplus_59_noapplecare_label"]')
actions = ActionChains(driver)
actions.move_to_element(apple_care_label).perform()

apple_care_xpath = '//*[@id="applecareplus_59_noapplecare_label"]'
apple_care_button = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH, apple_care_xpath
                ))
            )
apple_care_button.click()

check_store_xpath = '//*[@id="root"]/div[3]/div[3]/div[10]/div/div/div/div/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/button'
check_store_button = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH, check_store_xpath
                ))
            )
check_store_button.click()
clickable_temp_xpath = '//*[@id="portal"]/div/div/div/div/div[2]/div[1]/div[2]/div[1]/fieldset/div/div[2]/label/span'
clickable_temp = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH, clickable_temp_xpath
                ))
            )
print('clickable')
pin_code_input_xpath = '//*[@id="portal"]/div/div/div/div/div[2]/div[1]/div[1]/form/div[1]/div/div[1]/input'
pin_code_input = driver.find_element('xpath', pin_code_input_xpath)
print('pin code input found')
pin_code_input.click()
pin_code_input.clear()
pin_code_input.send_keys('85281')
pin_code_input.send_keys(Keys.RETURN)
nearest_store_xpath = '//*[@id="portal"]/div/div/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/button'
nearest_store_button = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH, nearest_store_xpath
                ))
            )
availability = str(nearest_store_button.text).strip(' ')

if not availability.startswith('Not'):
    message = availability + ' Click on this link - ' + link
    url = f"https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id={CHAT_ID}&text={message}"
    requests.get(url).json()