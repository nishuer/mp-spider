import time

from .base import Base
from app.source.tieba_source import tiezi_list, tiezi_text
from app.account.tieba_account import tieba_account_list
from random import randrange
from app.api import request

class TiebaPoster(Base):
    __main_site = "https://tieba.baidu.com"

    def __init__(self, lock, queue, config):
        super(TiebaPoster, self).__init__(config)

        self.lock = lock
        self.queue = queue
        self.current_account = {}
        self.post_num = 50

    def run(self):
        self.workFlow()

    def workFlow(self):
        for index, account in enumerate(tieba_account_list):
            self.loginAccount(account)
            self.current_account = account

            print('************** 当前账号：%s *************' % (account['name']))
            
            for url in tiezi_list[index * self.post_num:(index + 1) * self.post_num]:
                self.driver.get(url)

                print('当前帖子：%s' % (url))

                if self.isDeleted() or not self.isCanPost() or self.isPosted():
                    print('帖子不符合回帖规则，跳过！')
                    continue

                self.scrollBottom()

                time.sleep(randrange(6, 9))

                self.publish_poster()

                time.sleep(8)

                if self.isAccountInvail():
                    print('账号开始需要验证，切换下一个账号')
                    break

                if self.isPosted():
                    print('回帖成功且有效！！！')
                    self.queue.put({
                        'url': url,
                        'name': self.current_account['name']
                    })
                    print('推送至网警进程，内容：%s | %s' % (url, self.current_account['name']))
                else:
                    print('回帖成功但被秒删！！！')

                print('-----------------------------------')
                
                time.sleep(randrange(8, 16))

            # self.driver.quit()

        print('程序结束！！！')

    def getProxyIP(self):
        res = request.get('http://dps.kdlapi.com/api/getdps/?orderid=958279722770632&num=1&pt=1&dedup=1&format=json&sep=1')
        ip = res.json()['data']['proxy_list'][0]
        print('提取新IP：%s' % ip)
        return ip

    def isPosted(self):
        try:
            self.driver.find_element_by_xpath("//a[@class='p_author_name j_user_card' and text()='%s']" % (self.current_account['name']))
            return True
        except:
            return False

    def isCanPost(self):
        try:
            self.driver.find_element_by_xpath("//a[text()='下一页']")
            return False
        except:
            return True
    
    def isDeleted(self):
        try:
            self.driver.find_element_by_xpath("//h1[text()='很抱歉，该贴已被删除。']")
            return True
        except:
            return False

    def loginAccount(self, account):
        # ip = self.getProxyIP()
        self.launchWebdriver()
        self.driver.get(self.__main_site)
        self.addCookies(account)
        self.driver.refresh()

    def publish_poster(self):
        index = randrange(0, len(tiezi_text))
        text = tiezi_text[index]
        # self.writeTitle(text['title'])
        self.writeContent(text['text'])
        time.sleep(randrange(3, 5))
        self.handleSubmit()

    def writeTitle(self, title):
        titleInputElement = self.driver.find_element_by_class_name("editor_title")
        titleInputElement.send_keys(title)
    
    def writeContent(self, text):
        publishTextareaElement = self.driver.find_element_by_id("ueditor_replace")
        publishTextareaElement.send_keys(text)
        count = 0
        while (count < 3):
            self.insertFace()
            count = count + 1

    def insertFace(self):
        face_list = [
            "https://tb2.bdstatic.com/tb/editor/images/face/i_f59.gif?t=20140803",
            "https://tb2.bdstatic.com/tb/editor/images/face/i_f54.gif?t=20140803",
            "https://tb2.bdstatic.com/tb/editor/images/face/i_f68.gif?t=20140803",
            "https://tb2.bdstatic.com/tb/editor/images/face/i_f53.gif?t=20140803",
            "https://tb2.bdstatic.com/tb/editor/images/face/i_f53.gif?t=20140803",
            "https://tb2.bdstatic.com/tb/editor/images/face/i_f51.gif?t=20140803",
            "https://tb2.bdstatic.com/tb/editor/images/ali/ali_016.gif?t=20140803",
            "https://tb2.bdstatic.com/tb/editor/images/ali/ali_017.gif?t=20140803",
            "https://tb2.bdstatic.com/tb/editor/images/ali/ali_018.gif?t=20140803",
            "https://tb2.bdstatic.com/tb/editor/images/ali/ali_019.gif?t=20140803",
            "https://tb2.bdstatic.com/tb/editor/images/face/i_f65.gif?t=20140803",
            "https://tb2.bdstatic.com/tb/editor/images/face/i_f66.gif?t=20140803",
        ]

        face = face_list[randrange(0, len(face_list))]
        scriptString = 'var img=new Image();img.src="%s";img.width="80";img.height="80";document.getElementById("ueditor_replace").appendChild(img);' % face
        self.driver.execute_script(scriptString)


    def handleSubmit(self):
        publishBtnElement = self.driver.find_element_by_class_name("poster_submit")
        publishBtnElement.click()
    
    # 账号是否开始需要验证了
    def isAccountInvail(self):
        try:
            self.driver.find_element_by_class_name("pass-forceverify-wrapper")
            return True
        except:
            return False