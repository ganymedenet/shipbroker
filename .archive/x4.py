# import undetected_chromedriver.v2 as uc
import undetected_chromedriver.v2 as uc


def main():
    driver = uc.Chrome(headless=True, use_subprocess=False)

    driver = uc.Chrome()
    with driver:
        driver.get('https://www.marinetraffic.com')

    # driver.implicitly_wait(10)
    # # driver.get('https://nowsecure.nl')
    # driver.get('https://www.marinetraffic.com')
    # driver.implicitly_wait(10)
        driver.save_screenshot('nowsecure1.png')

    driver.quit()


if __name__ == '__main__':
    main()
