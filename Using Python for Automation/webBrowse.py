from selenium import webdriver
driver = webdriver.Firefox() # initialize webdriver
driver.get('http://demo.seleniumeasy.com/basic-first-form-demo.html')

# single input field
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('Hello World') # inputs message into text box
showMessageButton = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/form/button')
showMessageButton.click()

# two input fields
fieldA = driver.find_element_by_xpath('//*[@id="sum1"]')
fieldA.send_keys('5')
fieldB = driver.find_element_by_xpath('//*[@id="sum2"]')
fieldB.send_keys('12')
getTotalButton = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/form/button')
getTotalButton.click()