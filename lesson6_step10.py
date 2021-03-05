from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)

    # Ваш код, который заполняет обязательные поля
    inputs = browser.find_elements_by_css_selector('input:required')
    first_name = browser.find_element_by_xpath('//input[contains(@placeholder, "first name")]')
    last_name = browser.find_element_by_xpath('//input[contains(@placeholder, "last name")]')
    email = browser.find_element_by_xpath('//input[contains(@placeholder, "email")]')
    first_name.send_keys('123')
    last_name.send_keys('123')
    email.send_keys('123')
    time.sleep(4)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
browser.quit()
