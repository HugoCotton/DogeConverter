from selenium import webdriver
import time
import pandas as pd
caps = DesiredCapabilities.CHROME
caps["chromeOptions"] = {}
caps["chromeOptions"]["excludeSwitches"] = ["disable-popup-blocking"]

driver = webdriver.Chrome(executable_path= 'D:\Downloads\chromedriver_win32\chromedriver')

search_query = 'https://www.binance.com/en/trade/DOGE_USDT'

driver.get(search_query)
time.sleep(5)
Dogecoin_Price_USDT = driver.find_element_by_xpath('//*[@id="__APP"]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]').get_attribute('innerHTML')
print(Dogecoin_Price_USDT)

search_query = 'https://www.binance.com/en/trade/GBP_USDT'

driver.get(search_query)
time.sleep(5)
USDT_Price_GBP = driver.find_element_by_xpath('//*[@id="__APP"]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]').get_attribute('innerHTML')
print(USDT_Price_GBP)


