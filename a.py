# # driver = webdriver.Chrome("./driver/chromedriver.exe", options=options)  # Optional argument, if not specified will search path.
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)  # Optional argument, if not specified will search path.


import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install())  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/')
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()