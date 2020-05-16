from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


driver =webdriver.Chrome()
driver.get('https://www.londonstockexchange.com/home/homepage.htm')

wait = WebDriverWait(driver,10)

def search(ticker):
	searchEl=driver.find_element_by_id("head_solr_search_input")
	searchEl.send_keys(ticker)
	wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'ui-menu-item')))
	searchEl.send_keys(Keys.DOWN)
	searchEl.send_keys(Keys.DOWN)
	searchEl.send_keys(Keys.ENTER)

def get_stock_url():
	return driver.current_url

def get_last_price():
	return driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/div[2]/div[1]/div[5]/div[1]/table/tbody/tr[2]/td[2]').text
search('UU')
print(get_stock_url())
print(get_last_price())
time.sleep(3)
driver.quit()