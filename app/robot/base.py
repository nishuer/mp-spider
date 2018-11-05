from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from app.extend import helper

class Base(object):
    def __init__(self, config):
        profile = webdriver.FirefoxProfile(config["profile_dir"])
        self.driver = webdriver.Firefox(firefox_profile=profile)

        # option = webdriver.ChromeOptions()
        # option.add_argument('--user-data-dir=%s' % config["profile_dir"])
        # self.driver = webdriver.Chrome(chrome_options=option)
    

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
        self.driver.execute_script('window.open("%s")' % url, '_blank')


    def switchWindow(self, index):
        self.driver.switch_to_window(self.driver.window_handles[index])


    def __getKeysControlOrCommand(self):
        systemPlatform = helper.getSystem()

        if (systemPlatform == 'Windows'):
            return Keys.CONTROL
        elif(systemPlatform == 'Darwin'):
            return Keys.COMMAND
        else:
            print('Unsupported running environment')


    def actionCopy(self):
        self.action.key_down(self.__getKeysControlOrCommand()).send_keys("c").key_up(self.__getKeysControlOrCommand()).perform()


    def actionPaste(self):
        self.action = ActionChains(self.driver)
        self.action.key_down(self.__getKeysControlOrCommand()).send_keys("v").key_up(self.__getKeysControlOrCommand()).perform()


    def actionSelect(self):
        self.action = ActionChains(self.driver)
        self.action.key_down(self.__getKeysControlOrCommand()).send_keys("a").key_up(self.__getKeysControlOrCommand()).perform()


    def actionEnter(self, element):
        element.send_keys(Keys.ENTER)


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
        