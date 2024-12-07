from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    input = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x=input.text
    y=calc(x)

    ans = browser.find_element(By.CSS_SELECTOR, "#answer")
    ans.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла