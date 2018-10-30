from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from app.extend import helper

class Base(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
    

    def hasCheckDriverWait(self, elementName, timeout = 6, byType = 'CLASS_NAME'):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((getattr(By, byType), elementName)))
            return True
        except:
            return False


    def addCookies(self, account):
        for key in account['cookies'].keys():
            cookie = {
                "domain": account['domain'],
                "name": key,
                "value": account['cookies'][key],
                'path': '/',
                'expires': None
            }
            self.driver.add_cookie(cookie)


    def openNewWindow(self, url):
        self.driver.execute_script('window.open("%s")' % url)


    def switchWindow(self, index):
        self.driver.switch_to_window(self.driver.window_handles[index])


    def actionCopy(self):
        self.action.key_down(Keys.COMMAND).send_keys("c").key_up(Keys.COMMAND).perform()


    def actionPaste(self):
        self.action = ActionChains(self.driver)
        self.action.key_down(Keys.COMMAND).send_keys("v").key_up(Keys.COMMAND).perform()


    def actionSelect(self):
        self.action = ActionChains(self.driver)
        self.action.key_down(Keys.COMMAND).send_keys("a").key_up(Keys.COMMAND).perform()


    def hideElement(self, element):
        self.driver.execute_script("arguments[0].setAttribute('style', 'display: none')", element)


    def setElementAttr(self, element):
        def attr(name, value = ''):
            self.driver.execute_script("arguments[0].setAttribute('%s', '%s')" % (name, value), element)

        return attr


    def scrollBottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
   
   
    def scrollTop(self):
        self.driver.execute_script("window.scrollTo(0, 0)")