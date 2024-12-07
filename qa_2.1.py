from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element(By.CSS_SELECTOR, '#num1').text)
    num2 = int(browser.find_element(By.CSS_SELECTOR, '#num2').text)

    sum = num1 + num2

    sum=str(sum)

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(sum)  # ищем элемент с рассчитанной суммой

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла