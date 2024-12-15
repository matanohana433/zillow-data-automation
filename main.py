import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



CLONE_URL = "https://appbrewery.github.io/Zillow-Clone/"
google_form_link = "https://docs.google.com/forms/d/e/1FAIpQLSfxjo4O9gYlMLgfmEaPsp--2vPa8oM_sKxkKBGjgdRRTeFjaA/viewform?usp=dialog"

response = requests.get(CLONE_URL)
zillow_page = response.text
soup = BeautifulSoup(zillow_page, "html.parser")

addresses = soup.select('div address')
addresses_list = [address.text.strip() for address in addresses]


prices = soup.find_all(name="span", attrs={"data-test": "property-card-price"})
prices_list = []
for price in prices:
    cost = price.text[:6]
    prices_list.append(cost)


links = soup.find_all(name="a", attrs={"data-test":"property-card-link"})
links_list = [link['href'] for link in links]


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

for i in range(len(links_list)):
    driver.get(google_form_link)
    time.sleep(2)
    address = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    address.send_keys(addresses_list[i])
    price.send_keys(prices_list[i])
    link.send_keys(links_list[i])
    submit_button.click()



