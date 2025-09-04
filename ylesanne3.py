import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = uc.Chrome()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

i = 0
j = 0


try:
    elements = WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.TAG_NAME, 'button')))


except TimeoutError:
    pass


while i < 5: 
    elements.click()
    i = i + 1


time.sleep(3)

def finddelete():
    try:
        elements2 = WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.CLASS_NAME, 'added-manually')))

        elements2.click()
    except TimeoutError:
        pass



finddelete()
finddelete()
finddelete()
finddelete()
finddelete()


time.sleep(20)

driver.quit()