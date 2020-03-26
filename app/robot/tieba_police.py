import time
import os
import logging

from .base import Base


class TiebaPolice(Base):
    __main_site = "https://tieba.baidu.com"

    def __init__(self, lock, queue, config):
        super(TiebaPolice, self).__init__(config)

        self.lock = lock
        self.queue = queue

        self.current_url = ''
        self.current_name = 'sad叫姐姐'
        self.tieba_list = [
            "https://tieba.baidu.com/p/4690557899",
            "https://tieba.baidu.com/p/4309779315",
            "https://tieba.baidu.com/p/4297664757",
            "https://tieba.baidu.com/p/4257349632"
        ]
      
        self.current_index = 145

    def run(self):
        # self.driver.maximize_window()
        # self.driver.get('https://tieba.baidu.com/p/6508968304')
        
        # self.scrollToName()
        # time.sleep(3)

        # self.handleOpenCommentBox()

        self.launchWebdriver()
        self.workFlowSimple()
        # self.workFlow()
        self.driver.quit()

    def workFlowSimple(self):
        for url in self.tieba_list:
            self.current_url = url
            print('（网警）有新数据：%s' % (url))

            self.driver.get(url)

            print('（网警）访问帖子：%s' % (url))

            if self.isPostValid():
                print('（网警）帖子有效！！！')

                time.sleep(1)

                name = self.current_name
                self.scrollToName(name)

                time.sleep(2)

                self.handleOpenCommentBox(name)

                time.sleep(1)

                self.writeContent()
                self.handleSubmit(name)

                time.sleep(1)

                print('（网警）回帖警告成功！')

                self.getScreenshot()
                self.tieziPoliceLogWrite()

                print('（网警）截图并记录帖子数据成功！')

                self.current_index = self.current_index + 1

            else:
                print('（网警）帖子无效！！！')

    def workFlow(self):
        while True:
            time.sleep(0.1)
            self.current_data = self.queue.get()

            self.current_name = self.current_data['name']

            if self.current_data:
                print('（网警）有新数据：%s | %s' % (self.current_data['url'], self.current_name))

                self.driver.get(self.current_data['url'])

                print('（网警）访问帖子：%s' % (self.current_data['url']))

                if self.isPostValid():
                    print('（网警）帖子有效！！！')

                    time.sleep(1)

                    name = self.current_name
                    self.scrollToName(name)

                    time.sleep(2)

                    self.handleOpenCommentBox(name)

                    time.sleep(1)

                    self.writeContent()
                    self.handleSubmit(name)

                    time.sleep(1)

                    print('（网警）回帖警告成功！')

                    self.getScreenshot()
                    self.tieziPoliceLogWrite()

                    print('（网警）截图并记录帖子数据成功！')

                    self.current_index = self.current_index + 1

                else:
                    print('（网警）帖子无效！！！')


    def isPostValid(self):
        try:
            self.driver.find_element_by_xpath("//a[@class='p_author_name j_user_card' and text()='%s']" % (self.current_name))
            return True
        except:
            return False

    def scrollToName(self, name):
        nameElement = self.driver.find_element_by_xpath("//a[@class='p_author_name j_user_card' and text()='%s']" % (name))
        self.driver.execute_script("arguments[0].scrollIntoView();", nameElement)
        time.sleep(1)
        self.scrollAnywhere(-300)

    def handleOpenCommentBox(self, name):
        commentBtnElement = self.driver.find_element_by_xpath("//a[@class='p_author_name j_user_card' and text()='%s']/../../../../div[2]/div[2]/div[1]/div[1]/a" % (name))
        commentBtnElement.click()
    
    def writeContent(self):
        text = '您好，我是长沙市公安局网警，您的百度贴吧账号"%s"发布的贴文中含违法违规内容，请您自行将其删除。警方提示：利用互联网发布、传播违法信息的，违反《计算机信息网络国际联网安全管理保护办法》、《治安管理处罚法》等法律法规，公安机关将依法予以处理。' % (self.current_name)
        commentInputElement = self.driver.find_element_by_xpath('//*[@id="j_editor_for_container"]')
        commentInputElement.send_keys(text)

    def handleSubmit(self, name):
        submitBntElement = self.driver.find_element_by_xpath("//a[@class='p_author_name j_user_card' and text()='%s']/../../../../div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr/td[2]/div[1]/span[1]" % (name))
        submitBntElement.click()

    def getScreenshot(self):
        self.driver.get_screenshot_as_file('%s/app/data/tieba/screenshot/%s.png' % (os.getcwd(), self.current_index))

    def tieziPoliceLogWrite(self):
        with open('%s/app/data/tieba/tiezi_police_log.txt' % (os.getcwd()), 'a', encoding='utf8') as f:
            try:
                f.write('%s|%s\n' % (self.current_url, self.current_name))
            except Exception as e:
                logging.exception(e)