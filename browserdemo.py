import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_element_located

from os import listdir
from pathlib import Path

options = webdriver.ChromeOptions()
options.headless = False
browser = webdriver.Chrome(executable_path="/home/toor/Desktop/Option/chromedriver", options=options)
browser.maximize_window()

browser.get("https://expertoption.com/?demo=true")

main_w = browser.current_window_handle
assert len(browser.window_handles) == 1
#time.sleep(3)
html_file = Path.cwd() / "file:///home/toor/Desktop/Option/bitcoin.html"
#browser.execute_script('window.open(html_file.as_uri());')

browser.switch_to.new_window('tab')

#pos1 = browser.find_elements_by_xpath('//*[@id="widget-technical-analysis-container"]/div/div/div/span[2]')
#print('pos1:')
#print(pos1)
#time.sleep(3)
#browser.switch_to_window(main_w)
#time.sleep(3)


browser.get("https://expertoption.com/?demo=true")
try:
    browser.implicitly_wait(100)
    timestamp = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div/div/div/div/div/div/div[4]/div[2]/div/div[1]/div[3]/div[2]/div[2]')
    print('Current timestamp: %s' % (timestamp.text.split(' ')[0]))
finally:
    print(browser.title)
##### change Stock name #############
browser.find_element_by_class_name("button-content").click()
inputelm = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div[3]/div/div/div/div[2]/div[2]/div[1]/form/input')
inputelm.clear()
time.sleep(1)
inputelm.clear()
inputelm.send_keys("Bitcoin")
time.sleep(2)
browser.find_element_by_class_name("item__inner").click()
time.sleep(2)
browser.find_element_by_class_name("save").click()
time.sleep(3)
##### change Amount #############
inputelm = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div/div/div/div/div/div/div[4]/div[2]/div/div[1]/div[1]/div[2]/span[2]/input')
inputelm.clear()
time.sleep(1)
inputelm.clear()
inputelm.send_keys("1")


while 2>=1 :
    Amount = 1
    inputelm.clear()
    inputelm.send_keys(Amount)
    prof = 0
    while prof == 0 :   
    #############  press buy button #############
        browser.find_element_by_class_name("call").click()
    ############## get result of position ##############
        time.sleep(2)
        prof = browser.find_elements_by_xpath('//*[@id="app"]/div/div/div/div[3]/div/div/div/div[2]/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/span')[0].text
        print(prof)
        prof = prof[1]
    ##############
        time.sleep(2)
    #########Close result
        browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div[3]/div/div/div/div[1]/span').click()
        prof = int(prof)
       # print(prof)
        Amount = Amount + Amount + 1
        if Amount == 15:
            Amount = 33
        if Amount == 67:
            Amount = 75
        if Amount == 151:
            Amount = 168
        if Amount == 337 :
            Amount = 379
        if Amount == 759:
            Amount = 853
        if Amount == 1707:
            Amount = 1
            print('Over 9th failed trade!!!')

        inputelm.clear()
        inputelm.send_keys(Amount)


#############  press buy button #############
#############browser.find_element_by_class_name("call").click()

############# get result of position ##############
#############prof = browser.find_elements_by_xpath('//*[@id="app"]/div/div/div/div[3]/div/div/div/div[2]/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/span')[0].text
#############print(prof)
##############






#browser.find_element_by_class_name("Close").click()
# time.sleep(80)
#click(findElement.By.linkText("deal-button call"))
# prof = driver.find_element_by_class_name("money value").text  # deposit
##########################################
#command = input('enter command: ')
#if(command == 'val'):
#    prof = browser.find_elements_by_xpath('//*[@id="app"]/div/div/div/div[3]/div/div/div/div[2]/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/span')[0].text
#    print(prof)
##########################################
# prof = 0
# prof = driver.find_elements_by_class_name("i.currency").text  # profit
# print(prof)

#print(browser.title)
#time.sleep(10)
browser.quit()
