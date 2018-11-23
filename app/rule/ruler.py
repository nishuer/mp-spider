from app.extend import helper

from . import kuaibao_rule
from . import sohu_rule
from . import uczzd_rule
from app.config.default import SOHU_PLATFORM, KUAIBAO_PLATFORM, UC_PLATFORM


def hasCheckTitle(self, url):
    source = helper.getSourcePlatform(url)

    if (source == SOHU_PLATFORM):
        return sohu_rule.hasCheckTitle(self)

    if (source == KUAIBAO_PLATFORM):
        return kuaibao_rule.hasCheckTitle(self)

    if (source == UC_PLATFORM):
        return uczzd_rule.hasCheckTitle(self)


def openArticle(self, url):
    source = helper.getSourcePlatform(url)

    if (source == SOHU_PLATFORM):
        return sohu_rule.openArticle(self)

    if (source == KUAIBAO_PLATFORM):
        return kuaibao_rule.openArticle(self)


def getTitle(self, url):
    source = helper.getSourcePlatform(url)

    if (source == SOHU_PLATFORM):
        return sohu_rule.getTitle(self)

    if (source == KUAIBAO_PLATFORM):
        return kuaibao_rule.getTitle(self)

       
def hideOtherElement(self, url):
    source = helper.getSourcePlatform(url)

    if (source == SOHU_PLATFORM):
        return sohu_rule.hideOtherElement(self)

    if (source == KUAIBAO_PLATFORM):
        return kuaibao_rule.hideOtherElement(self)

    if (source == UC_PLATFORM):
        return uczzd_rule.hideOtherElement(self)