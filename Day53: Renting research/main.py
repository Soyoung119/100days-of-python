from appier import seconds_eval
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://www.myhome.ie/residential/dublin/property-for-sale-in-dublin-6"
Google_form = "https://docs.google.com/forms/d/e/1FAIpQLSdAhH3tl5ZY-SpQKKc1jc2bgKsIgeLlvZ85V6oTeA0eAWCugw/viewform?usp=publish-editor"

response = requests.get(URL)
renting = response.text
soup = BeautifulSoup(renting, 'html.parser')


listing_link = soup.find_all(name='a', class_="text-decoration-none d-block")
prices = soup.find_all(name="h2", class_="card-title my-2 fs-1")
address = soup.find_all(name="h3", class_="card-text mt-2")


link_list = []
price_list = []
add_list = []

for rent in listing_link:
    link = rent.get('href')
    if link not in link_list:
        link_list.append(link)

for rent in prices:
    price = rent.text
    price_list.append(price)

for rent in address:
    add = rent.text
    add_list.append(add)

print(link_list)
print(price_list)
print(add_list)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(Google_form)

n=0
while True:
    time.sleep(3)
    answers = driver.find_elements(By.CSS_SELECTOR, "input.whsOnd.zHQkBf")
    first = answers[0]
    first.send_keys(add_list[n])

    second = answers[1]
    second.send_keys(price_list[n])

    third = answers[2]
    third.send_keys(f"myhome.ie{link_list[n]}")

    n += 1

    submit_button = driver.find_element(By.XPATH, "//span[text()='Submit']")
    submit_button.click()

    time.sleep(2)
    another_response = driver.find_element(By.XPATH, "//a[text()='Submit another response']")
    another_response.click()

