from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

load_dotenv()

TWITTER_EMAIL = os.environ["EMAIL"]
TWITTER_PASSWORD = os.environ["PASSWORD"]
USERNAME = os.environ["USERNAME"]

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        go = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button')
        go.click()

        time.sleep(60)
        down = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/h3').text
        print(f"down: {down}")
        up = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[2]/div/h3').text
        print(f"up: {up}")

    def tweet_at_provider(self):
        self.driver.get("https://x.com/home")
        # self.driver.get("https://x.com/")
        time.sleep(2)
        cookie = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div[2]/button[2]/div/div/span/span')
        cookie.click()
        email = self.driver.find_element(By.NAME, "username_or_email")
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)

        time.sleep(2)
        username = self.driver.find_element(By.ID, "jf-input-challenge_response")
        username.send_keys(USERNAME)
        username.send_keys(Keys.ENTER)