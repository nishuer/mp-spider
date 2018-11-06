import os
import logging
import time
import platform
import importlib
import re

from app.config.default import source_list


def getSourcePlatform(url):
    source = ''

    for value in source_list:
        try:
            url.index('value%s' % '.')
            source = value
            break
        except ValueError:
            pass

    return source


def getSourceList(config):
    list = ()

    for value in config.source:
        _source = importlib.import_module('app.source.%s_source' % value)
        list = list + getattr(_source, config['account']['category'])

    return list


def titleRead(title, fileName):
    with open('%s/app/data/title_%s_data.txt' % (os.getcwd(), fileName), 'r', encoding='utf8') as f:
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