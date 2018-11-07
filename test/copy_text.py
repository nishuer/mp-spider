from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()

driver.get("http://kuaibao.qq.com/s/20181107A09HUL00")

e1s = driver.find_elements_by_xpath("/html/body/div[position() > 2]")
e2s = driver.find_elements_by_xpath('//*[@id="con_wrap"]/*[position() > 1]')
e3s = driver.find_elements_by_xpath('//*[@id="con_wrap"]/div[1]/*[position() > 1]')
e4s = driver.find_elements_by_xpath('//*[@id="content"]/*[position() < 3]')

e1 = driver.find_element_by_xpath('//*[@id="top_downloader"]')
e2 = driver.find_element_by_xpath('//*[@class="downloader-bar"]')

for _ in e1s:
    driver.execute_script("arguments[0].setAttribute('style', 'display: none')", _)
for _ in e2s:
    driver.execute_script("arguments[0].setAttribute('style', 'display: none')", _)
for _ in e3s:
    driver.execute_script("arguments[0].setAttribute('style', 'display: none')", _)
for _ in e4s:
    driver.execute_script("arguments[0].setAttribute('style', 'display: none')", _)

driver.execute_script("arguments[0].setAttribute('style', 'display: none')", e1)
driver.execute_script("arguments[0].setAttribute('style', 'display: none')", e2)
