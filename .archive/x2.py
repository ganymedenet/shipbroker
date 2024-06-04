from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
import random
#create an instance of ChromeOptions
options = webdriver.ChromeOptions()
#user-agent rotation
user_agents = [
    #add your list of user agents here
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
]

user_agent = random.choice(user_agents)
options.add_argument(f"user-agent={user_agent}")

#initialize the WebDriver with options
driver = webdriver.Chrome(options=options)

#apply stealth settings to the driver
stealth(
    driver,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
)
#navigate to the site
driver.get("https://www.marinetraffic.com/en/ais/home")
#take a screenshot of the result
driver.save_screenshot("stealth-example.png")
#close browser
driver.quit()