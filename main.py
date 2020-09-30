from selenium import webdriver

username = 'xxxxx'
password = 'xxxxx'

url = 'https://www.facebook.com/'

driver = webdriver.Chrome("/Users/AMISH/Desktop/Facebook Automation/chromedriver")

driver.get(url)

driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_id('loginbutton').click()
