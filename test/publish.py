from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()

browser.get("https://www.toutiao.com/")

c1 = {u"name":u"uid_tt",u"value": u"3158caff5aaa4b5a1487e3d29b974c91",u"domain":u".toutiao.com"}
c2 = {u"name":u"ccid",u"value": u"80b594c0df5e31f4277d233198cc7958",u"domain":u".toutiao.com"}
c3 = {u"name":u"ckmts",u"value": u"PUbINLAQ,qrJNPQ0Q,L6cINLAQ",u"domain":u".toutiao.com"}
c4 = {u"name":u"sid_tt",u"value":u"82bf7a025d30f69084caf10ec7987935",u"domain":u".toutiao.com"}

browser.add_cookie(c1)
browser.add_cookie(c2)
browser.add_cookie(c3)
browser.add_cookie(c4)

time.sleep(3)

browser.get("https://mp.toutiao.com/profile_v3/graphic/publish")

time.sleep(3)

publishTextarea = browser.find_element_by_class_name("ql-container")

publishTextarea.click()

time.sleep(3)

# publishTextarea.send_keys(Keys.COMMAND, 'v')

action = ActionChains(browser)

action.key_down(Keys.COMMAND).send_keys("v").key_up(Keys.COMMAND).perform()