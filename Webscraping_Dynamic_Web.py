#make sure using correct version of Chrome.

from selenium import webdriver
import pandas as pd

url='https://www.XXXXXXXXXXX'

driver=webdriver.Chrome()

driver=.get(url)

Dogs=driver.find_elements_by_class_name('')

for dog in dogs:
  attribute_1=driver.find_elements_by_xpath('')
  attribute_2=driver.find_elements_by_xpath('')
  attribute_3=driver.find_elements_by_xpath('')
  
Dog_item={
  'attribute_1':attribute_1,
  'attribute_2':attribute_2,
  'attribute_3':attribute_3,
}

df=pd.DataFrame(Dog_item)
