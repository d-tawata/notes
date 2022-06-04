from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
driver.get('https://www.vogue.com/')
wait = WebDriverWait(driver, 10) # throws exception after 10 seconds if condition not satisfied
searchButton = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="google_ads_iframe_3379/conde.vogue.cm/nav-cta/homepage/bundle/1_0"]')))
searchButton.click()

