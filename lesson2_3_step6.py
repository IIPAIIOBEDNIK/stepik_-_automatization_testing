from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    button1 = browser.find_element_by_tag_name("button").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    element_x = browser.find_element_by_id("input_value")
    x = element_x.text

    input = browser.find_element_by_id("answer")
    input.send_keys(calc(x))

    button2 = browser.find_element_by_tag_name("button").click()

finally:

    time.sleep(30)
    browser.quit()














