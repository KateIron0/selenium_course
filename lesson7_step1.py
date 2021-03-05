import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

from selenium import webdriver

try:
    link = "http://suninjuly.github.io/math.html"
    browser=webdriver.Chrome()
    browser.get(link)

    x_element=browser.find_element_by_css_selector("span.nowrap")
    x=x_element.text
    y=calc(x)

    input=browser.find_element_by_id("answer")
    input.send.keys(y)

    option1=browser.find_element_by_id("robotCheckbox")
    option1.click()

    option2=browser.find_element_by_id("peopleRule")
    option2.click()

    button=browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()


