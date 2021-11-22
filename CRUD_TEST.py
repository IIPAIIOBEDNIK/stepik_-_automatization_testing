from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://nda.local"

browser = webdriver.Chrome()
#Инструкция wait нужна для того, когда элемент не сразу прогружается не падала ошибка
browser.implicitly_wait(30)

try:
    browser.get(link)

    #CRUD в Справочники
    button_Directories_Open = browser.find_element_by_css_selector("[data-qtip = Справочники]").click()
    button_Pet_Types = browser.find_element_by_css_selector("[data-qtip = 'Pet Types']").click()
    button_Create_Pet_Types = browser.find_element_by_css_selector("[data-qtip = Создать]").click()
    input_Pet_Types = browser.find_element_by_name("Name")
    input_Pet_Types.send_keys("test")
    button_Save_Pet_Types = browser.find_element_by_link_text("Создать").click()
    time.sleep(1)
    tr_Pet_Types_Record = browser.find_element_by_partial_link_text("test").click()
    button_Edit_Pet_Types = browser.find_element_by_css_selector("[data-qtip = Изменить]").click()
    input_Pet_Types = browser.find_element_by_name("Name")
    input_Pet_Types.send_keys("test000")
    button_Save_Pet_Types = browser.find_element_by_link_text("Применить").click()
    time.sleep(1)
    tr_Pet_Types_Record = browser.find_element_by_partial_link_text("test000").click()
    button_Delete_Pet_Types = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-qtip = Удалить]"))).click() 
    button_RecordDelete_Pet_Types = browser.find_element_by_link_text("Удалить").click()


finally:
    time.sleep(10)
    browser.quit()

