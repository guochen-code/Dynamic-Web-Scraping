# automate web login
from selenium import webdriver
from selenium.webdriver.common.keys import keys

driver=webdriver.Chrome()

url='http://XXXXXXXXXXXXXXX'

driver.get(url)

driver.find_elements_by_xpath('').send_keys('')
driver.find_elements_by_xpath('').send_keys('')
driver.find_elements_by_xpath('').click()

driver.quit()
