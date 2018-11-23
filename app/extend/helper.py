import os
import logging
import time
import platform
import importlib
import re

from app.config.default import SOURCE_LIST, API_SOURCE_LIST


def getSourcePlatform(url):
    source = ''

    for value in SOURCE_LIST:
        try:
            url.index(value)
            source = value
            break
        except ValueError as e:
            print(e)

    return source


def getSourceList(config):
    list = ()

    for value in config['source']:
        try:
            API_SOURCE_LIST.index(value)
            continue
        except ValueError:
            _source = importlib.import_module('app.source.%s_source' % value)
            list = list + getattr(_source, config['account']['category'])
        
    return list


def getApiSourceList(config):
    list = ()

    for value in config['source']:
        try:
            API_SOURCE_LIST.index(value)
            _source = importlib.import_module('app.api.%s_api' % value)
            list = list + getattr(_source, config['account']['category'])()
        except ValueError:
            continue
            
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


def titleSimilarityLog(title, target_title, num):
     with open('%s/app/log/%s.txt' % (os.getcwd(), 'title_similarity'), 'a', encoding='utf8') as f:
        try:
            f.write('%s\n' % title)
            f.write('%s\n' % target_title)
            f.write('%s\n' % num)
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