import time
from selenium import webdriver

driver = webdriver.Chrome('/home/toor/Desktop/Option/chromedriver')
driver.get('https://expertoption.com/?demo=true')
time.sleep(40)
#webdriver.findElement(By.linkText("deal-button call")).click()
webdriver.driver.findElement(By.linkText("deal-button call")).click()
#click(findElement.By.linkText("deal-button call"))
print(driver.title)
time.sleep(20)
driver.quit()