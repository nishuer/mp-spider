from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# option = webdriver.FirefoxProfile("/Users/nishu/Library/Application Support/Firefox/Profiles/2m3vd669.robot")
driver = webdriver.Chrome()

driver.get("https://www.toutiao.com/")

time.sleep(2)

driver.execute_script('window.open("%s")' % "http://www.baidu.com")

# text = driver.find_element_by_xpath('//*[@id="rightModule"]/div[2]/div/div/p')
# inputEle = driver.find_element_by_xpath('//*[@id="rightModule"]/div[1]/div/div/div/input')

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

