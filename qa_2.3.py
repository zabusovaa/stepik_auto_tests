from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла


# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input1.send_keys('Анна')

    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input2.send_keys('Фролова')

    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input3.send_keys('email')

    file_button = browser.find_element(By.CSS_SELECTOR, '#file')
    file_button.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла