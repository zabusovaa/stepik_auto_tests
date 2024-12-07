from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#treasure')
    valuex = x_element.get_attribute('valuex')
    #x = x_element.text
    y = calc(valuex)

    input = browser.find_element(By.CSS_SELECTOR, '#answer')
    input.send_keys(y)

    radio = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    radio.click()

    check = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    check.click()

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла