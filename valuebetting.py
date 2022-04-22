from selenium import webdriver
import time

web = 'https://22bet.co.ke/line/'
path = r'C:\Users\EliteBook 8560p\.wdm\drivers\chromedriver\win32\100.0.4896.60'

driver = webdriver.Chrome(path)
driver.get(web)

time.sleep(5) #add implicit wait, if necessary
accept = driver.find_element_by_xpath('//*[@id="_evidon-accept-button"]')
accept.click()
