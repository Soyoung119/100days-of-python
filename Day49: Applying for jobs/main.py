from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
import time
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

load_dotenv()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(os.environ["URL"])

email = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
checkbox = driver.find_elements(By.CSS_SELECTOR,'label[for="rememberMeOptIn-checkbox"]')
button = driver.find_element(By.CLASS_NAME, "login__form_action_container")

email.send_keys(os.environ["Email"])
password.send_keys(os.environ["Password"])
if checkbox:
    checkbox[0].click()
button.click()

company_index = 0
while True:
    time.sleep(4)
    apply = driver.find_element(By.XPATH, "//button[contains(., 'Easy Apply')]")
    try:
        apply.click()
    except ElementClickInterceptedException:
        pass

    try:
        time.sleep(2)
        next_button = driver.find_elements(By.XPATH, "//button[contains(., 'Next')]")
        if next_button:
            cancel = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss"]')
            cancel.click()
            time.sleep(2)
            discard = driver.find_element(By.XPATH, "//button[contains(., 'Discard')]")
            discard.click()

        else:
            phone_number = driver.find_element(By.XPATH, "//div[contains(., 'Phone*')]/ancestor::div[1]//input")
            follow = driver.find_element(By.XPATH,"//p[contains(., 'Follow')]/ancestor::div[2]//label")
            submit = driver.find_element(By.XPATH, "//button[contains(., 'Submit Application')]")

            if phone_number.text == "":
                phone_number.send_keys(os.environ["Phone_number"])
            if follow.is_selected():
                follow.click()
            submit.click()

        time.sleep(2)
        companies = driver.find_elements(
            By.CSS_SELECTOR,
            'div[componentkey^="job-card-component-ref-"]'
        )
        companies[company_index].click()
        company_index += 1


    except NoSuchElementException:
        continue