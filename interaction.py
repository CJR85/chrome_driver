from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("/Users/calvinroberts 1/Dev/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element_by_css_selector("#articlecount a")
# print(article_count.text)

count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(count.text)