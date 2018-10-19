from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()

driver.get("https://view.inews.qq.com/a/20181017A04ABZ00?tbkt=C1&uid=")

time.sleep(2)

driver.execute_script("window.scrollTo(0, 1000)")

readFullArticleBtn = driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[2]/div/div[2]/img")

readFullArticleBtn.click()

driver.execute_script("window.scrollTo(0, 0)")

headerElement = driver.find_element_by_xpath("//*[@id='root']/div/div")
disclaimerElement = driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div/div/div[2]")
otherElement = driver.find_elements_by_xpath("//*[@id='root']/div/div[position() > 2]")

driver.execute_script("arguments[0].setAttribute('style', 'display: none')", headerElement)
driver.execute_script("arguments[0].setAttribute('style', 'display: none')", disclaimerElement)

for _ in otherElement:
    driver.execute_script("arguments[0].setAttribute('style', 'display: none')", _)


action = ActionChains(driver)
action.key_down(Keys.COMMAND).send_keys("a").key_up(Keys.COMMAND).perform()
action.key_down(Keys.COMMAND).send_keys("c").key_up(Keys.COMMAND).perform()


driver.execute_script('window.open("https://www.toutiao.com/")')

driver.switch_to_window(driver.window_handles[1])

time.sleep(3)

c1 = {u"name":u"uid_tt",u"value": u"94a43bbf53e7ff7cef8a5a21103fa793",u"domain":u".toutiao.com"}
c2 = {u"name":u"ccid",u"value": u"d863e681bde46657136c13f1c4c1bd65",u"domain":u".toutiao.com"}
c3 = {u"name":u"ckmts",u"value": u"PUUrOYsQ,qrUrOYsQ,L64rOYsQ",u"domain":u".toutiao.com"}
c4 = {u"name":u"sid_tt",u"value":u"7a4eaf65acc29cb04b6cdebcab76aaab",u"domain":u".toutiao.com"}

driver.add_cookie(c1)
driver.add_cookie(c2)
driver.add_cookie(c3)
driver.add_cookie(c4)

driver.get("https://mp.toutiao.com/profile_v3/graphic/publish")

time.sleep(3)

publishTextarea = driver.find_element_by_class_name("ql-container")

publishTextarea.click()

time.sleep(3)

action = ActionChains(driver)

action.key_down(Keys.COMMAND).send_keys("v").key_up(Keys.COMMAND).perform()

time.sleep(2)

driver.close()