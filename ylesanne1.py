import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from PIL import Image


searches = ["Armando"]


driver = uc.Chrome()
driver.get("https://www.google.com")
try:
   element = WebDriverWait(driver, 20).until(
   EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[1]/div'))


)
except:
   pass   
element.click()
time.sleep(2)
box = driver.find_element("name", "q")
time.sleep(1)
box.send_keys(searches)
time.sleep(1.5)
box.submit()
print("Otsisin:", searches)
time.sleep(1)


driver.save_screenshot("Pictures/random.png")




time.sleep(5)
driver.quit()
