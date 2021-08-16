from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import string
import random
import time

list_text = string.ascii_lowercase + string.digits

# Load webdriver using local gecko driver
driver = webdriver.Firefox(executable_path="geckodriver.exe")

# Open the website
driver.get("https://popcat.click/")

# Wait for the pape fisnish loading
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]')))

# use body element to for sending keys
element = driver.find_element_by_tag_name("body")

while(True): 
  # Random send keys text from a-z and 0-9
  text = random.choice(list_text)
  # Random wait time 5 , 20 means 5 to 20 ms
  # dont be to fast or the website might think you as a bot (i am not so sure either cuz there's no solid proof for this)
  wait_time = random.randint(5, 20) / 1000
  # wait (for human behavior click time)
  time.sleep(wait_time)
  # send keys text
  element.send_keys(text)
  
