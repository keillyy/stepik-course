from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

def calc_page(browser):
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
  
    x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value')
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

def step_4():
  URL = "http://suninjuly.github.io/alert_accept.html"

  try:
    browser = webdriver.Chrome()
    browser.get(URL)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    calc_page(browser)
  finally:
    time.sleep(30)
    browser.quit()

def step_6():
  URL = "http://suninjuly.github.io/redirect_accept.html"

  try:
    browser = webdriver.Chrome()
    browser.get(URL)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    calc_page(browser)
  finally:
    time.sleep(30)
    browser.quit()

step_6()