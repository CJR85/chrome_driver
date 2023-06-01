from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager  # pip install webdriver-manager
from selenium.webdriver.common.by import By
 
# chrome_driver_path = "path to your chromedriver"
# OR BETTER...
# Keep your chromedriver up to date. You can specify the path if you wish.
chrome_driver_path = ChromeDriverManager().install()
 
# See https://www.selenium.dev/documentation/webdriver/browsers/chrome/
# See https://chromedriver.chromium.org/capabilities#h.p_ID_102 for a list of options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # Keeps the browser open when the script finishes - unless you use driver.quit()
 
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
 
driver.get("https://python.org")
 
# Find an element
# element = driver.find_element(by=By.CLASS_NAME, value="some_class")

# CHALLENGE

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)

driver.quit()