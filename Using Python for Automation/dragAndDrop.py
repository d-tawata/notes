from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains # allows Selenium to perform more complex tasks
driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://www.valuelynk.com/int/demos/demo-drag-drop-3.html')
source = driver.find_element(by=By.XPATH, value='//*[@id="box6"]')
#source = driver.find_element_by_xpath('//*[@id="box6"]')
dest = driver.find_element(by=By.XPATH, value='//*[@id="box106"]')
#dest = driver.find_element_by_xpath('//*[@id="box106"]')
actions = ActionChains(driver) # actions stored in a queue
actions.drag_and_drop(source, dest).perform() # performs actions in order of the queue