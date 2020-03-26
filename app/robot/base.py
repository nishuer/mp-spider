from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app.extend import helper

class Base(object):
    def __init__(self, config):
        self.profile = webdriver.FirefoxProfile(config["profile_dir"])

        self.options = webdriver.FirefoxOptions()
        # self.options.set_headless(True)
        # chorme 设置
        # option = webdriver.ChromeOptions()
        # option.add_argument('--user-data-dir=%s' % config["profile_dir"])
        # self.driver = webdriver.Chrome(chrome_options=option)

    def launchWebdriver(self, myProxy = ''):
        if myProxy:
            firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
            firefox_capabilities['marionette'] = True
            firefox_capabilities['proxy'] = {
                "proxyType": "MANUAL",
                "httpProxy": myProxy,
                "ftpProxy": myProxy,
                "sslProxy": myProxy
            }

            self.driver = webdriver.Firefox(
                capabilities=firefox_capabilities,
                firefox_profile=self.profile,
                options=self.options
            )
        else:
            self.driver = webdriver.Firefox(
                firefox_profile=self.profile,
                options=self.options
            )

        self.driver.set_page_load_timeout(120)
        self.driver.maximize_window()
    

    def hasCheckDriverWait(self, elementName, timeout = 6, type = 'CLASS_NAME'):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((getattr(By, type), elementName)))
            return True
        except:
            return False
    
    
    def hasCheckElementVisibility(self, elementName, timeout = 6, type = 'CLASS_NAME'):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((getattr(By, type), elementName)))
            return True
        except:
            return False


    def addCookies(self, account):
        self.driver.delete_all_cookies()
        for key in account['cookies'].keys():
            cookie = {
                "domain": account['domain'] if key == 'BDUSS' else account['tieba_domain'],
                "name": key,
                "value": account['cookies'][key],
            }
            self.driver.add_cookie(cookie)


    def openNewWindow(self, url):
        self.driver.execute_script('window.open("")')
        self.switchWindow(len(self.driver.window_handles) - 1)

        try:
            self.driver.get(url)
        except TimeoutError:
            self.driver.refresh()


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

    def scrollAnywhere(self, value):
        self.driver.execute_script("window.scrollTo(0, document.documentElement.scrollTop + %d)" % (value))
        