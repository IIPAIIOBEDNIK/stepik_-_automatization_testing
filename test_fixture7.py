import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(30)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, link):
    link = f"{link}"
    browser.get(link)
    def calc(answer):
        return str(answer)
    answer = math.log(int(time.time()))
    input1 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "quiz-component.ember-view")))
    input1.send_keys(calc(answer))









