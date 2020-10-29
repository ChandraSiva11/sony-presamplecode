from selenium import webdriver


driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://google.com')
driver.find_element_by_name("q").send_keys("Selenium Automation")
driver.find_element_by_name("btnK").click()
driver.close()
driver.quit()
print("Test completed")