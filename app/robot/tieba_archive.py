import time
import os
import logging

from .base import Base
from selenium.webdriver.support.ui import Select

class TiebaArchive(Base):
    __main_site = "http://39.155.219.137/gkxc/"

    def __init__(self, lock, queue, config):
        super(TiebaArchive, self).__init__(config)

        self.lock = lock
        self.queue = queue
        self.current_data = None
        self.win_index = 0

    def run(self):
        self.launchWebdriver()
        self.driver.get(self.__main_site)
        time.sleep(15)
        self.driver.get('http://39.155.219.137/gkxc/jsda_list.aspx')

        list = self.logRead()
        
        for item in list:
            str = item.replace('\n', '')
            data = str.split('|')

            self.workFlow({
                'url': data[0],
                'name': data[1],
            })

    def workFlow(self, data):
        print('（档案）有新数据：%s | %s' % (data['url'], data['name']))
        
        addbtn = self.driver.find_element_by_class_name('tijiaoanniu')
        addbtn.click()

        self.win_index = self.win_index + 1

        self.switchWindow(self.win_index)

        time.sleep(3)

        s1 = Select(self.driver.find_element_by_id('drop_jslx'))
        s1.select_by_index(24)
        s2 = Select(self.driver.find_element_by_id('drop_pt'))
        s2.select_by_index(3)
        i1 = self.driver.find_element_by_id('txt_uid_h')
        i1.send_keys(data['name'])
        i2 = self.driver.find_element_by_id('txt_wmnc')
        i2.send_keys(data['name'])
        i3 = self.driver.find_element_by_id('txt_wfxxljdz')
        i3.send_keys(data['url'])

        text = '您好，我是长沙市公安局网警，您的百度贴吧账号"%s"发布的贴文中含违法违规内容，请您自行将其删除。警方提示：利用互联网发布、传播违法信息的，违反《计算机信息网络国际联网安全管理保护办法》、《治安管理处罚法》等法律法规，公安机关将依法予以处理。' % (data['name'])

        i4 = self.driver.find_element_by_id('txt_jsy')
        i4.send_keys(text)

        # b1 = self.driver.find_element_by_id('btnbc')
        # b1.click()

        print('（档案）录入成功！')

        time.sleep(1)

        self.switchWindow(0)

        time.sleep(3)

    def logRead(self):
        with open('%s/app/data/tieba/tiezi_police_log.txt' % (os.getcwd()), 'r', encoding='utf8') as f:
            try:
                list = f.readlines()
                return list
            except ValueError:
                return []