# import undetected_chromedriver as uc
# from selenium import webdriver
#
# options = webdriver.ChromeOptions()
# options.headless = True
# options.add_argument("start-maximized")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# driver = uc.Chrome(options=options)
# driver.get('https://bet365.com')
#
#

# https://stackoverflow.com/questions/68289474/selenium-headless-how-to-bypass-cloudflare-detection-using-selenium
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import undetected_chromedriver as uc

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

options.add_experimental_option("perfLoggingPrefs", {"enableNetwork": True})
options.add_argument("--enable-logging")
options.add_argument("--log-level=0")  # Adjust logging level if necessary
options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})


driver = uc.Chrome(options=options)

# driver = webdriver.Chrome(options=options)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

# driver.get("https://www.marinetraffic.com/en/ais/home")
driver.get("https://www.marinetraffic.com/en/ais/home/centerx:27.516/centery:40.967/zoom:13")

try:
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "MuiBox-root")))
    driver.execute_script("arguments[0].scrollIntoView();", element)
except TimeoutException:
    print("Failed to find the MuiBox-root element within the timeout period.")
    # Handle the exception (retry, log error, etc.)
finally:
    # Ensure the driver quits properly or moves to the next task
    driver.quit()

page_source = driver.page_source
print(page_source)

# MuiBox-root
logs = driver.get_log('performance')
endpoints = []
redirects = []

# for entry in logs:
#     log = json.loads(entry['message'])['message']
#     if log['method'] == 'Network.requestWillBeSent':
#         url = log['params']['request']['url']
#         endpoints.append(url)

for entry in logs:
    log = json.loads(entry['message'])['message']
    if log['method'] == 'Network.requestWillBeSent':
        url = log['params']['request']['url']
        endpoints.append(url)
        # Check if there is a redirect response
        if 'redirectResponse' in log['params']:
            redirect_info = {
                'url': url,
                'redirected_to': log['params']['request']['url'],
                'status_code': log['params']['redirectResponse']['status'],
                'status_text': log['params']['redirectResponse']['statusText']
            }
            redirects.append(redirect_info)

for endpoint in endpoints:
    print(endpoint)

with open("../src/test.html", "w") as file:
    file.write(page_source)

# Wait for user input to close
# input("Press any key to exit...")
# driver.quit()
