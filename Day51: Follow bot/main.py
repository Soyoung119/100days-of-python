from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv()

SIMILAR_ACCOUNT = "chefsteps"
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_options)
        self.driver.get("https://www.instagram.com/?hl=en")

    def login(self):
        time.sleep(2)
        cookie = self.driver.find_element(By.CSS_SELECTOR, "button._a9--._ap36._a9_1")
        cookie.click()

        time.sleep(5)
        email = self.driver.find_element(By.NAME, "email")
        email.send_keys(USERNAME)
        password = self.driver.find_element(By.NAME, "pass")
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

        time.sleep(40)
        not_now = self.driver.find_element(By.XPATH, "//div[@role='button' and text()='Not now']")
        not_now.click()

        time.sleep(2)
        notification = self.driver.find_element(By.CSS_SELECTOR, "button._a9--._ap36._a9_1")
        notification.click()

    def find_followers(self):
        time.sleep(3)
        button = self.driver.find_element(By.XPATH, "//a[@role='link' and @href='/explore/']")
        button.click()

        time.sleep(5)
        search = self.driver.find_element(By.CSS_SELECTOR, "input[aria-label='Search input']")
        search.send_keys(SIMILAR_ACCOUNT)

        time.sleep(2)
        chefs = self.driver.find_elements(By.XPATH, "//a[@role='link']")
        # for i, chef in enumerate(chefs):
        #     print(i, chef.get_attribute("href"))
        chef = chefs[11]
        chef.click()

        time.sleep(5)
        check_followers = self.driver.find_element(By.XPATH, "//span[text()=' followers']")
        check_followers.click()

    def follow(self):
        time.sleep(10)
        follow_buttons = self.driver.find_elements(
            By.XPATH, "//button[.//div[normalize-space()='Follow']]"
        )

        for follow_button in follow_buttons[1:10]:
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});",
                follow_button
            )
            # follow_button.click()

insta = InstaFollower()
insta.login()
insta.find_followers()
insta.follow()



