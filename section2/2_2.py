from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

def step_3():
  URL = "http://suninjuly.github.io/selects1.html"

  try:
    browser = webdriver.Chrome()
    browser.get(URL)

    num1 = browser.find_element(By.ID, "num1")
    num2 = browser.find_element(By.ID, "num2")

    options = browser.find_element(By.CSS_SELECTOR, "option[value='" + str(int(num1.text) + int(num2.text)) + "']")
    options.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
  finally:
      time.sleep(30)
      browser.quit()

def step_6():
  URL = "http://suninjuly.github.io/execute_script.html"

  def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

  try:
    browser = webdriver.Chrome()
    browser.get(URL)

    x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value')
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input.send_keys(y)

    checkBox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkBox)
    checkBox.click()

    radioButton = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radioButton)
    radioButton.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
  finally:
    time.sleep(30)
    browser.quit()
   
def step_8():
  URL = "https://suninjuly.github.io/file_input.html"

  current_dir = os.path.abspath(os.path.dirname(__file__))
  TXT_PATH = os.path.join(current_dir, 'task.txt')

  def create_txt():
    with open(TXT_PATH, "w") as file:
        file.write("by llnnly")

  create_txt()

  try:
    browser = webdriver.Chrome()
    browser.get(URL)

    firstName = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    firstName.send_keys("Ivan")
    lastName = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
    lastName.send_keys("Ivanov")
    email = browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
    email.send_keys("ivan@example.com")

    file = browser.find_element(By.CSS_SELECTOR, 'input[name="file"]')
    file.send_keys(TXT_PATH)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
  finally:
    time.sleep(30)
    browser.quit()

step_8()