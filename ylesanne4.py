import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = uc.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

#tomsmith ja parool SuperSecretPassword!. 

try:
    box1 = WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.ID, 'username')))
    box1.send_keys("tomsmith")

except TimeoutError:
    pass

try:
    box2 = WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.ID, 'password')))
    box2.send_keys("SuperSecretPassword!")

except TimeoutError:
    pass

button = WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.TAG_NAME, 'i')))


button.click()

time.sleep(20)
