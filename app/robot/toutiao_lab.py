import os
import time

from .base import Base
from app.extend import helper
from app.api import rise_keyword_api
from app.config.default import MATCH_RISE_KEYWORD_SWITCH


class ToutiaoLab():
    def __init__(self, config):
        self.config = config


    def updateRiseKeyword(self):
        category = self.config['account']['category']
        list = getattr(rise_keyword_api, 'getRiseKeyword')(category)
    
        helper.riseKeywordWrite(category, list)


    def matchRiseKeyword(self, title):
        try:
            if (not self.config['match_rise_keyword']):
                return True
        except KeyError:
            return True

        if (not MATCH_RISE_KEYWORD_SWITCH):
            return True

        category = self.config['account']['category']
        list = helper.riseKeywordRead(category)

        for keyword in list:
            if (title.find(keyword) > -1):
                return True

        return False