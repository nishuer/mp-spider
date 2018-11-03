from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def test():
    if (True):
        return not ("大地主刘文彩病逝之后，他的妻妾和子女都去了哪里，结局又如何？" == "大地主刘文彩病逝之后，他的妻妾和子女都去了哪里，结局又如何？")

    return True



print(test())

# driver = webdriver.Firefox()

# driver.get("https://www.toutiao.com")

# driver.execute_script('window.open("%s")' % "")

# driver.switch_to_window(driver.window_handles[1])

# driver.get("https://www.toutiao.com/search/")

# input = driver.find_element_by_xpath("//input[@name='keyword']")

# input.send_keys('李自成打进北京城前，明朝还有一次活命的机会，但却被他们糟蹋了')

# input.send_keys(Keys.ENTER)

# time.sleep(3)

# title = driver.find_element_by_xpath("//span[@class='J_title']")

# print(title.text)