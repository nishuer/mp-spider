from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()

driver.get("http://mp.sohu.com/profile?xpt=Z2p6bTg4QHNvaHUuY29t")

title = driver.find_element_by_class_name("wrap_title")

print(title.text)

# c1 = {u"name":u"uid_tt",u"value": u"3158caff5aaa4b5a1487e3d29b974c91",u"domain":u".toutiao.com"}
# c2 = {u"name":u"ccid",u"value": u"80b594c0df5e31f4277d233198cc7958",u"domain":u".toutiao.com"}
# c3 = {u"name":u"ckmts",u"value": u"PUbINLAQ,qrJNPQ0Q,L6cINLAQ",u"domain":u".toutiao.com"}
# c4 = {u"name":u"sid_tt",u"value":u"82bf7a025d30f69084caf10ec7987935",u"domain":u".toutiao.com"}

# browser.add_cookie(c1)
# browser.add_cookie(c2)
# browser.add_cookie(c3)
# browser.add_cookie(c4)

# try:
#     element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "login2-button")))
#     print(element)
# finally:
#     driver.close()

# browser.get("https://mp.toutiao.com/profile_v3/weitoutiao/")

# time.sleep(6)

# publishTextarea = browser.find_element_by_tag_name("textarea")
# publishBtn = browser.find_element_by_class_name("tui-btn")

# publishTextarea.send_keys("哈哈，今天大家在看什么动漫呢？")
# publishBtn.click()

# time.sleep(2)

# browser.refresh()

# time.sleep(6)

# publishTextarea = browser.find_element_by_tag_name("textarea")
# publishBtn = browser.find_element_by_class_name("tui-btn")

# publishTextarea.send_keys("大家想看什么动漫图，私信我哦～")
# publishBtn.click()

# time.sleep(2)

# browser.refresh()