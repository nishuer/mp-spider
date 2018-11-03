import os
import logging
import time
import platform

def titleRead(title, fileName):
    with open('%s/app/data/title_%s_data.txt' % (os.getcwd(), fileName), 'r') as f:
        try:
            f.readlines().index('%s\n' % title)
            return False
        except ValueError:
            return True


def titleWrite(title, fileName):
     with open('%s/app/data/title_%s_data.txt' % (os.getcwd(), fileName), 'a', encoding='utf8') as f:
        try:
            f.write('%s\n' % title)
        except Exception as e:
            logging.exception(e)


def getSystem():
    return platform.system()


# 获取当前时分秒
def getDate():
        return time.strftime("%H:%M:%S", time.localtime())


# 判断目录是否存在
def hasDir(dir):
    return os.path.isdir(dir)