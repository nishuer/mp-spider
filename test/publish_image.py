from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os

driver = webdriver.Firefox()

driver.get("https://www.toutiao.com")

c1 = {u"name":u"uid_tt",u"value": u"d3aea42d20fde5f79a5a141ad8dc9d18",u"domain":u".toutiao.com"}
c2 = {u"name":u"ccid",u"value": u"6e47f9e62642f5666c997ae542d3b10b",u"domain":u".toutiao.com"}
c3 = {u"name":u"sid_tt",u"value":u"911a66cf4c923901f97c0355f3605c78",u"domain":u".toutiao.com"}

driver.add_cookie(c1)
driver.add_cookie(c2)
driver.add_cookie(c3)

driver.get("https://mp.toutiao.com/profile_v3/graphic/figure")

time.sleep(3)

openUploadModalBtnNode = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[3]/div[1]/button[1]')

openUploadModalBtnNode.click()

uploadNode = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[2]/span/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/div/div[1]/span/input')

driver.execute_script("arguments[0].setAttribute('style', 'display: block')", uploadNode)

uploadNode.send_keys('%s/images/47475/0.jpg' % os.getcwd())

# action = ActionChains(driver)

# action.move_to_element_with_offset(text, 0, 0)
# action.click_and_hold()
# action.move_by_offset(100, 0)
# action.release()
# action.perform()

# action.key_down(Keys.COMMAND).send_keys("c").key_up(Keys.COMMAND).perform()

# c1 = {u"name":u"uid_tt",u"value": u"8e7aaaca3ea51397034b5aeb5dd4e301",u"domain":u".toutiao.com"}
# c2 = {u"name":u"ccid",u"value": u"3caa67295422191672595c00c082f815",u"domain":u".toutiao.com"}
# c4 = {u"name":u"sid_tt",u"value":u"c7aec0b2d374767f67dffba040b89989",u"domain":u".toutiao.com"}

# driver.add_cookie(c1)
# driver.add_cookie(c2)
# driver.add_cookie(c4)

# driver.get("https://mp.toutiao.com/profile_v3/graphic/publish")

# time.sleep(3)

# publishTextareaElement = driver.find_element_by_class_name("ql-editor")
# publishTextareaElement.click()

# time.sleep(2)

# action = ActionChains(driver)
# action.key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()

