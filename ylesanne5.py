import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = uc.Chrome()
driver.get("https://the-internet.herokuapp.com/")


# Click on the Checkboxes thingy
button = WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/ul/li[6]/a')))

button.click()

time.sleep(2)

# Check the checkbox
check = WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.XPATH, '//*[@id="checkboxes"]/input[1]')))

check.click()
time.sleep(2)

# Go back
driver.back()


time.sleep(200)
