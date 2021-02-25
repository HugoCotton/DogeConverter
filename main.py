from selenium import webdriver
import time

#locates chrome driver
driver = webdriver.Chrome(executable_path= 'D:\Downloads\chromedriver_win32\chromedriver')

#numb of my dogecoin - DIAMOND HANDS
DogecoinNumb = 1605.1471

#site with required information
search_query = 'https://uk.tradingview.com/symbols/DOGEUSDT/'

#what do you think
driver.get(search_query)
time.sleep(5)
#gets sprecific element from page
Dogecoin_Price_USDT = driver.find_element_by_xpath('//*[@id="anchor-page-1"]/div/div[3]/div[1]/div/div/div/div[1]/div[1]').get_attribute('innerHTML')
#gets string from site - with certain unnesscery(spelling) stuff
Dogecoin_Price_USDT = Dogecoin_Price_USDT.replace('<span class="">', '')
Dogecoin_Price_USDT = Dogecoin_Price_USDT.replace('<span class="tv-symbol-price-quote__value--growing">', '')
Dogecoin_Price_USDT = Dogecoin_Price_USDT.replace('<span class="tv-symbol-price-quote__value--falling">', '')
Dogecoin_Price_USDT = Dogecoin_Price_USDT.replace('</span>', '')
#remove sum bulshite
Dogecoin_Price_USDT = float(Dogecoin_Price_USDT)
Dogecoin_Price_USDT *= 100000000
Dogecoin_Price_USDT = int(Dogecoin_Price_USDT)
#convert to float then int for calcs


#same shit again
search_query = 'https://uk.tradingview.com/symbols/USDTGBP/'

driver.get(search_query)
time.sleep(5)
USDT_Price_GBP = driver.find_element_by_xpath('//*[@id="anchor-page-1"]/div/div[3]/div[1]/div/div/div/div[1]/div[1]').get_attribute('innerHTML')
USDT_Price_GBP = USDT_Price_GBP.replace('</span>', '')
USDT_Price_GBP = USDT_Price_GBP.replace('<span>', '')
USDT_Price_GBP = USDT_Price_GBP.replace('<span class="">', '')
USDT_Price_GBP = float(USDT_Price_GBP)
USDT_Price_GBP *= 100000000
USDT_Price_GBP = int(USDT_Price_GBP)

#calculates
USDT_Value = (DogecoinNumb*Dogecoin_Price_USDT)/100000000
GBP_Value = (USDT_Price_GBP*USDT_Value)/100000000

print(f'Your Dogecoin is worth ${round(USDT_Value, 2)} USDT')
print(f'or £{round(GBP_Value, 2)} GBP')

if GBP_Value > 70.07:
    print(f'You have a profit of {round(GBP_Value - 70.07, 2)} GBP!')
elif GBP_Value < 70.07:
    print(f'You have a loss of £{round(70.07 - GBP_Value, 2)} GBP')