import os
import importlib
import time

from .base import Base
from app.extend import helper


class ToutiaoArticleRobot(Base):
    __publish_site = "https://www.toutiao.com"
    __publish_site_url = "https://mp.toutiao.com/profile_v3/graphic/publish"


    def __init__(self, config):
        super(ToutiaoArticleRobot, self).__init__(config)

        self.config = config
        _source = importlib.import_module('app.source.%s_source' % config['source']['platform'])
        self.source = getattr(_source, config['source']['category'])

        self.rule = importlib.import_module('app.rule.%s_rule' % config['source']['platform'])
        

    def run(self):
        self.workFlow()


    def workFlow(self):
        self.loginAccount()
        self.navigatePublishPage()

        while True:
            self.openSource()


    def loginAccount(self):
        self.driver.get(self.__publish_site)
        self.driver.maximize_window()

        if (self.hasCheckDriverWait("login-button")):
            self.addCookies(self.config['account'])
        else:
            self.loginAccount()


    def navigatePublishPage(self):
        try:
            self.driver.get(self.__publish_site_url)
        except TimeoutError:
            print('网页打开超时，重新刷新页面')
            self.navigatePublishPage()
        
        if (self.hasCheckDriverWait("ql-container")):
            self.__tempHandle()
        else:
            self.navigatePublishPage()


    # 处理临时的页面特殊问题
    def __tempHandle(self):
        # 处理青云计划弹窗
        # if (self.hasCheckDriverWait('pgc-dialog', 3)):
        #     dialogElement = self.driver.find_element_by_class_name("pgc-dialog")
        #     self.hideElement(dialogElement)
            
        #     bodyElement = self.driver.find_elements_by_xpath("/html/body")
        #     self.setElementAttr(bodyElement)('class')

        # 处理撤销
        if (self.hasCheckDriverWait('//*[@id="syl-fixed-alert"]/div/span', 3, 'XPATH')):
            time.sleep(3)
            revokeElement = self.driver.find_element_by_xpath('//*[@id="syl-fixed-alert"]/div/span')
            revokeElement.click()


    def writeTitle(self, title):
        titleInputElement = self.driver.find_element_by_class_name("tui2-input")
        titleInputElement.send_keys(title)
    
    
    def writeContent(self):
        publishTextareaElement = self.driver.find_element_by_class_name("ql-editor")
        publishTextareaElement.click()
        time.sleep(1)
        self.actionPaste()

        time.sleep(3)
        self.scrollBottom()
        self.clickAutoCover()


    def publishArticle(self):
        publishBtnElement = self.driver.find_element_by_xpath("//*[@id='publish']")
        publishBtnElement.click()


    def clickAutoCover(self):
        autoCoverElement = self.driver.find_element_by_xpath("//*[@class='article-cover']/div/div/label[last()]")
        autoCoverElement.click()


    def openSource(self):
        for url in self.source:
            self.__handleSingleSource(url)


    def reset(self):
        self.switchWindow(1)
        self.driver.close()

        try:
            self.switchWindow(1)
            self.driver.close()
        except:
            pass
        finally:
            self.switchWindow(0)
            self.navigatePublishPage()

            time.sleep(10)


    # 单一资源处理流程
    def __handleSingleSource(self, url):
        self.openNewWindow(url)

        self.switchWindow(1)
        
        if (self.rule.hasCheckTitle(self)):

            self.rule.openArticle(self)

            self.switchWindow(2)

            title = self.rule.getTitle(self)

            if (title):
                
                helper.titleWrite(title, self.config['source']['category'])

                self.switchWindow(0)

                self.writeTitle(title)

                self.switchWindow(2)

                self.rule.hideOtherElement(self)

                time.sleep(1)

                self.actionSelect()
                self.actionCopy()

                self.switchWindow(0)
                
                time.sleep(1)
                
                self.writeContent()

                self.publishArticle()

                time.sleep(2)
            else:
                print('不是图文，跳过 %s' % helper.getDate())
        else:
            print('已经发布，跳过 %s' % helper.getDate())

        self.reset()
