
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get('https://www.amazon.in/ref=nav_logo')

search_box = driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('apple')
click_search_button = driver.find_element(By.ID, 'nav-search-submit-button').click()

wait = WebDriverWait(driver, 10)


