from selenium import webdriver

username = '7083593642'
password = 'amis#@111'

url = 'https://www.facebook.com/'

driver = webdriver.Chrome("/Users/AMISH/Desktop/Facebook Automation/chromedriver")

driver.get(url)

driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_id('loginbutton').click()