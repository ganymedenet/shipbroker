import undetected_chromedriver as uc
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

def main():
    # Get the current working directory
    current_dir = os.getcwd()

    # Define the target URL
    target_url = 'https://www.marinetraffic.com/en/ais/home'

    # Create a simple HTML file with a link to the target URL
    with open('../src/blank.html', 'w') as f:
        f.write(f'<html><body><a href="{target_url}" target="_blank">link</a></body></html>')

    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")

    # Configure undetected_chromedriver to use headless mode
    driver = uc.Chrome(headless=True, options=chrome_options, use_subprocess=False)

    driver.get(target_url)
    driver.execute_script(f"window.open('{target_url}', '_blank')")

    driver.save_screenshot('nowsecure.png')

    input()

    # driver.execute_script("window.open('https://www.marinetraffic.com/en/ais/home', '_blank')")
    # sleep(15)
    # driver.switch_to.window(driver.window_handles[1])
    #
    # # Open the local HTML file in the browser
    # driver.get(f'file://{current_dir}/blank.html')

    # Wait for all elements to load
    # sleep(2)

    # wait = WebDriverWait(driver, 10)

    # Save a screenshot of the page



    # try:
    #     wait = WebDriverWait(driver, 10)
    #     element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "MuiBox-root")))
    #     driver.save_screenshot('nowsecure.png')
    #     driver.execute_script("arguments[0].scrollIntoView();", element)
    # except:
    #     print("Failed to find the MuiBox-root element within the timeout period.")
    #     # Handle the exception (retry, log error, etc.)
    # finally:
        # Ensure the driver quits properly or moves to the next task
    driver.quit()


if __name__ == '__main__':
    main()
