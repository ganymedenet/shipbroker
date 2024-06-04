import undetected_chromedriver as uc
import time

options = uc.ChromeOptions()
options.headless = True  # Set headless to False to run in non-headless mode
# https://www.zenrows.com/blog/selenium-cloudflare-bypass#cloudfalre-bypass-using-undetected-chromedriver
driver = uc.Chrome(use_subprocess=True, options=options)
driver.get("https://www.marinetraffic.com/en/ais/home/centerx:27.516/centery:40.967/zoom:13")
driver.maximize_window()

time.sleep(5)
driver.save_screenshot("datacamp.png")
driver.close()


