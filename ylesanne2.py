import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = uc.Chrome()
driver.get("https://quotes.toscrape.com")






try:
   elements = WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.CLASS_NAME, 'text')))
   auth = driver.find_elements('class name', 'author')
   elem = driver.find_elements('class name', 'text')




   for e, a in zip(elem, auth):
       print(f"Quote: {e.text} - {a.text}")


except TimeoutError:
   pass


time.sleep(2)


driver.quit()