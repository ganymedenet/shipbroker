from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import json

# Set up Chrome options for headless mode and performance logging
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Ensures the browser window does not show
chrome_options.add_experimental_option("perfLoggingPrefs", {"enableNetwork": True})
chrome_options.add_argument("--enable-logging")
chrome_options.add_argument("--log-level=0")  # Adjust logging level if necessary

# Set logging preferences for performance monitoring
chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

# Set up the Chrome WebDriver with headless option
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the webpage
driver.get('https://www.marinetraffic.com/en/ais/home')

# Retrieve and process network logs
logs = driver.get_log('performance')
endpoints = []
for entry in logs:
    log = json.loads(entry['message'])['message']
    if log['method'] == 'Network.requestWillBeSent':
        url = log['params']['request']['url']
        endpoints.append(url)

# Print the HTML source of the page
page_source = driver.page_source
# print(page_source)

# Print extracted endpoints
print(endpoints)

# Wait for user input to close
input("Press any key to exit...")
driver.quit()


