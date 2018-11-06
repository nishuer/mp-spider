from app.extend import helper

from . import kuaibao_rule
from . import sohu_rule


def hasCheckTitle(self, url):
    source = helper.getSourcePlatform(url)

    if (source == 'sohu'):
        return sohu_rule.hasCheckTitle(self)

    if (source == 'kuaibao'):
        return kuaibao_rule.hasCheckTitle(self)


def openArticle(self, url):
    source = helper.getSourcePlatform(url)

    if (source == 'sohu'):
        return sohu_rule.openArticle(self)

    if (source == 'kuaibao'):
        return kuaibao_rule.openArticle(self)


def getTitle(self, url):
    source = helper.getSourcePlatform(url)

    if (source == 'sohu'):
        return sohu_rule.openArticle(self)

    if (source == 'kuaibao'):
        return kuaibao_rule.openArticle(self)

       
def hideOtherElement(self, url):
    source = helper.getSourcePlatform(url)

    if (source == 'sohu'):
        return sohu_rule.hideOtherElement(self)

    if (source == 'kuaibao'):
        return kuaibao_rule.hideOtherElement(self)