from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()

# driver.get("https://m.sohu.com/a/270826132_100294332")
# driver.get("https://m.sohu.com/a/271183961_100058701")
driver.get("http://www.sohu.com/a/271264384_451027")

time.sleep(3)

e1s = driver.find_elements_by_xpath("/html/body/*[position() > 1]")
e2s = driver.find_elements_by_xpath("/html/body/div[1]/*[position() < 3]")
e3s = driver.find_elements_by_xpath("/html/body/div[1]/*[position() > 3]")
e4s = driver.find_elements_by_xpath('//*[@id="article-container"]/div[1] | //*[@id="right-side-bar"]')
e5s = driver.find_elements_by_xpath('//*[@id="article-container"]/div[2]/*[position() > 1]')
e6s = driver.find_elements_by_xpath('//*[@id="article-container"]/div[2]/div[1]/*[position() > 2]')

e1 = driver.find_element_by_xpath('//*[@id="article-container"]/div[2]/div[1]/div[1]')
e2 = driver.find_element_by_xpath('//*[@id="backsohucom"]')

for _ in e1s:
    driver.execute_script("arguments[0].setAttribute('style', 'display: none')", _)
for _ in e2s:
    driver.execute_script("arguments[0].setAttribute('style', 'display: none')", _)
for _ in e3s:
    driver.execute_script("arguments[0].setAttribute('style', 'display: none')", _)
for _ in e4s:
    driver.execute_script("arguments[0].setAttribute('style', 'display: none')", _)
for _ in e5s:
    driver.execute_script("arguments[0].setAttribute('style', 'display: none')", _)
for _ in e6s:
    driver.execute_script("arguments[0].setAttribute('style', 'display: none')", _)

driver.execute_script("arguments[0].setAttribute('style', 'display: none')", e1)
driver.execute_script("arguments[0].setAttribute('style', 'display: none')", e2)

# # 优先清除文章中的广告，解决无法点击“查看全文”按钮的问题
# try:
#     e6 = driver.find_element_by_class_name('nice-container')
#     driver.execute_script("arguments[0].setAttribute('style', 'display: none')", e6)
# except Exception as e:
#     print(e)

# try:
#     readFullArticleBtn = driver.find_element_by_xpath('//*[@id="artLookAll"]')
#     driver.execute_script("window.scrollTo(0, 1800)")
#     readFullArticleBtn.click()
# except Exception as e:
#     print(e)

# e1s = driver.find_elements_by_xpath('//*[@id="backTop"] | //*[@id="toastDialog"] | //*[@id="webClip"]')
# e2 = driver.find_element_by_xpath('/html/body/div[3]/div[1]')

# try:
#     driver.find_element_by_class_name('top-bill-wrapper')
# except:
#     e3s = driver.find_elements_by_xpath('/html/body/div[3]/div[2]/*[position() < 3]')
#     e8s = driver.find_elements_by_xpath('/html/body/div[3]/div[2]/*[position() > 3]')
# else:
#     e3s = driver.find_elements_by_xpath('/html/body/div[3]/div[2]/*[position() < 4]')
#     e8s = driver.find_elements_by_xpath('/html/body/div[3]/div[2]/*[position() > 4]')

# e4 = driver.find_element_by_class_name('article-footer')

# try:
#     driver.find_element_by_class_name('hidden-content')
# except:
#     e7s = driver.find_elements_by_xpath('//*[@id="articleContent"]/*[position() > 1]')
# else:
#     e7s = driver.find_elements_by_xpath('//*[@id="articleContent"]/div[3]/*[last()] | //*[@id="articleContent"]/div[3]/*[last() - 1]')

# e5s = driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div[3]/*[position() > 1]')

# driver.execute_script("arguments[0].setAttribute('style', 'display: none')", e2)
# driver.execute_script("arguments[0].setAttribute('style', 'display: none')", e4)

# for _ in e1s:
#     driver.execute_script("arguments[0].setAttribute('style', 'display: none')", _)
# for _ in e3s:
#     driver.execute_script("arguments[0].setAttribute('style', 'display: none')", _)
# for _ in e8s:
#     driver.execute_script("arguments[0].setAttribute('style', 'display: none')", _)
# for _ in e7s:
#     driver.execute_script("arguments[0].setAttribute('style', 'display: none')", _)
# for _ in e5s:
#     driver.execute_script("arguments[0].setAttribute('style', 'display: none')", _)

# headerElement = driver.find_element_by_xpath("//*[@id='root']/div/div")
# disclaimerElement = driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div/div/div[2]")
# otherElement = driver.find_elements_by_xpath("//*[@id='root']/div/div[position() > 2]")

# driver.execute_script("arguments[0].setAttribute('style', 'display: none')", headerElement)
# driver.execute_script("arguments[0].setAttribute('style', 'display: none')", disclaimerElement)

# for _ in otherElement:
#     driver.execute_script("arguments[0].setAttribute('style', 'display: none')", _)


# action = ActionChains(driver)
# action.key_down(Keys.COMMAND).send_keys("a").key_up(Keys.COMMAND).perform()
# action.key_down(Keys.COMMAND).send_keys("c").key_up(Keys.COMMAND).perform()


# driver.execute_script('window.open("https://www.toutiao.com/")')

# driver.switch_to_window(driver.window_handles[1])

# time.sleep(3)

# c1 = {u"name":u"uid_tt",u"value": u"94a43bbf53e7ff7cef8a5a21103fa793",u"domain":u".toutiao.com"}
# c2 = {u"name":u"ccid",u"value": u"d863e681bde46657136c13f1c4c1bd65",u"domain":u".toutiao.com"}
# c3 = {u"name":u"ckmts",u"value": u"PUUrOYsQ,qrUrOYsQ,L64rOYsQ",u"domain":u".toutiao.com"}
# c4 = {u"name":u"sid_tt",u"value":u"7a4eaf65acc29cb04b6cdebcab76aaab",u"domain":u".toutiao.com"}

# driver.add_cookie(c1)
# driver.add_cookie(c2)
# driver.add_cookie(c3)
# driver.add_cookie(c4)

# driver.get("https://mp.toutiao.com/profile_v3/graphic/publish")

# time.sleep(3)

# publishTextarea = driver.find_element_by_class_name("ql-container")

# publishTextarea.click()

# time.sleep(3)

# action = ActionChains(driver)

# action.key_down(Keys.COMMAND).send_keys("v").key_up(Keys.COMMAND).perform()

# time.sleep(2)

# driver.close()