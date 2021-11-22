from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://nda.local"

browser = webdriver.Chrome()
#Инструкция wait нужна для того, когда элемент не сразу прогружается не падала ошибка
browser.implicitly_wait(30)

def test_crud_filtre():
    try:
        browser.get(link)

        button_Directories_Open = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-qtip = Справочники]"))).click()
        button_Pet_Types = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-qtip = 'Pet Types']"))).click()
        item = browser.find_element_by_css_selector(".x-grid-data-row:last-child")
        x = item.text
        Input_Filtre = browser.find_element_by_class_name("x-form-item-input-row>.x-form-item-body>.x-form-field.x-form-text")
        Input_Filtre.send_keys(x)
        time.sleep(10)

    finally:
        browser.quit()