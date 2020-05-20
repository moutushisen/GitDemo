from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

#driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")

driver.get("http://uat.mypolicynow.com/")

driver.find_element_by_id("open-login-pop-up").click()
driver.find_element_by_name("username").send_keys("9987793988")
# driver.find_element_by_css_selector("input[name='name']").send_keys("9987793988")
driver.find_element_by_name("password").send_keys("9987793988")
driver.find_element_by_id("password").click()
driver.find_element_by_xpath("//button[@id='login_submit']").click()
driver.back()
driver.get("http://uat.mypolicynow.com/quotation/privatecar")

driver.refresh()
driver.close()