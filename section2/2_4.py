from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math

def calc_page(browser):
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
  
    x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value')
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

def step_8():
    URL = "http://suninjuly.github.io/explicit_wait2.html"

    try:
        browser = webdriver.Chrome()
        browser.get(URL)

        WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

        button = browser.find_element(By.ID, "book")
        button.click()

        calc_page(browser)
    finally:
        time.sleep(30)
        browser.quit()

step_8()