from selenium import webdriver
import time

driver = webdriver.Chrome(r"C:\Users\gaurav sahani\Desktop\chromedriver_win32\chromedriver.exe")
time.sleep(1)

User_name = "lovishgarg0709@gmail.com"
Password = "subscribemychannel"

driver.get('http://facebook.com')
time.sleep(2)

driver.find_element_by_xpath('//*[@id="email"]').send_keys(User_name)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="pass"]').send_keys(Password)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="u_0_b"]').click()
time.sleep(1)
