from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def step_5():
  URL = "https://suninjuly.github.io/math.html"

  def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

  try:
      browser = webdriver.Chrome()
      browser.get(URL)

      x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value')
      x = x_element.text
      y = calc(x)

      input = browser.find_element(By.ID, "answer")
      input.send_keys(y)

      checkBox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
      checkBox.click()

      radioButton = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
      radioButton.click()

      button = browser.find_element(By.CSS_SELECTOR, "button.btn")
      button.click()
  finally:
      time.sleep(30)
      browser.quit()

def step_7():
  URL = "http://suninjuly.github.io/get_attribute.html"

  def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

  try:
      browser = webdriver.Chrome()
      browser.get(URL)

      x_element = browser.find_element(By.CSS_SELECTOR, 'img#treasure')
      x = x_element.get_attribute("valuex")
      y = calc(x)

      input = browser.find_element(By.ID, "answer")
      input.send_keys(y)

      checkBox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
      checkBox.click()

      radioButton = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
      radioButton.click()

      button = browser.find_element(By.CSS_SELECTOR, "button.btn")
      button.click()
  finally:
      time.sleep(30)
      browser.quit()
   
step_7()