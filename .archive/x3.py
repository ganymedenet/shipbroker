import time

from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

# Create an instance of ChromeOptions
options = webdriver.ChromeOptions()

# User-agent rotation
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
]

user_agent = random.choice(user_agents)
options.add_argument(f"user-agent={user_agent}")
options.add_argument("--disable-popup-blocking")

# Initialize the WebDriver with options
driver = webdriver.Chrome(options=options)

# Apply stealth settings to the driver
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True)

# Navigate to the site
driver.get("https://www.marinetraffic.com/en/ais/home")
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 30)

try:
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/button[2]'))).click()
except:
    print("AGree button did not show up")

driver.save_screenshot("stealth-example.png")

search = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/header/div/div')))
driver.execute_script("arguments[0].setAttribute('value', 'Vessel')", search)

time.sleep(15)
# # Use WebDriverWait to wait until a specific element is loaded
# try:
#     # Wait for a specific element that indicates the page is fully loaded
#     element_present = EC.presence_of_element_located((By.CLASS_NAM, "MuiBox-root"))  # Update the ID based on your needs
#     WebDriverWait(driver, 10).until(element_present)
# except:
#     print("Timed out waiting for page to load")

# Take a screenshot of the result


# Close browser
driver.quit()
