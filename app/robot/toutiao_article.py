import os
import importlib
import time

from .base import Base
from app.extend import helper
from app.rule import ruler


class ToutiaoArticleRobot(Base):
    __publish_site = "https://www.toutiao.com"
    __publish_site_url = "https://mp.toutiao.com/profile_v3/graphic/publish"
    __publish_search_url = "https://www.toutiao.com/search"


    def __init__(self, config):
        super(ToutiaoArticleRobot, self).__init__(config)

        self.config = config
        self.sourceList = helper.getSourceList(config)


    def run(self, lock):
        self.lock = lock
        self.workFlow()


    def workFlow(self):
        self.openSearch()
        self.loginAccount()
        self.navigatePublishPage()

        while True:
            self.openSource()


    def loginAccount(self, isInit = True):
        if (isInit):
            self.openNewWindow("")
            self.switchWindow(1)

        self.driver.get(self.__publish_site)

        self.addCookies(self.config['account'])


    def navigatePublishPage(self):
        try:
            self.driver.get(self.__publish_site_url)
        except TimeoutError:
            print('发布网页打开超时，重新刷新页面')
            self.navigatePublishPage()
        
        if (self.hasCheckDriverWait("ql-container")):
            self.__tempHandle()
        else:
            self.navigatePublishPage()


    def openSearch(self):
        try:
            self.driver.get(self.__publish_search_url)
            self.driver.maximize_window()
        except TimeoutError:
            print('搜索网页打开超时，重新刷新页面')
            self.openSearch()


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


    def checkTitleRepeat(self, title):
        self.switchWindow(0)
        self.driver.get(self.__publish_search_url)

        searchInput = self.driver.find_element_by_xpath("//input[@name='keyword']")
        
        searchInput.send_keys(title)
        self.actionEnter(searchInput)

        if (self.hasCheckDriverWait("//span[@class='J_title']", 10, 'XPATH')):
            searchTitle = self.driver.find_element_by_xpath("//span[@class='J_title']")
            print(title)
            print(searchTitle.text)
            return not (title == searchTitle.text)
           
        return False


    def openSource(self):
        for url in self.sourceList:
            self.lock.acquire()

            try:
                self.__handleSingleSource(url)
            finally:
                self.lock.release()


    def reset(self):
        self.switchWindow(2)
        self.driver.close()

        try:
            self.switchWindow(2)
            self.driver.close()
        except:
            pass
        finally:
            self.switchWindow(1)
            self.navigatePublishPage()

            time.sleep(6)


    # 单一资源处理流程
    def __handleSingleSource(self, url):
        self.openNewWindow(url)

        self.switchWindow(2)

        title = ruler.hasCheckTitle(self, url)
        
        if (title and self.checkTitleRepeat(title)):

            self.switchWindow(2)

            ruler.openArticle(self, url)

            self.switchWindow(3)

            title = ruler.getTitle(self, url)

            if (title):
                
                self.switchWindow(1)

                self.writeTitle(title)

                self.switchWindow(3)

                ruler.hideOtherElement(self, url)

                time.sleep(1)

                self.actionSelect()
                self.actionCopy()

                self.switchWindow(1)
                
                time.sleep(1)
                
                self.writeContent()

                self.publishArticle()

                helper.titleWrite(title, self.config['account']['category'])

                time.sleep(2)
            else:
                print('不是图文，跳过 %s' % helper.getDate())
        else:
            print('已经发布，跳过 %s' % helper.getDate())

        self.reset()
