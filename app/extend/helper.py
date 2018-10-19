
def addCookies(driver):
    c1 = {u"name": u"uid_tt", u"value": u"94a43bbf53e7ff7cef8a5a21103fa793",
          u"domain": u".toutiao.com"}
    c2 = {u"name": u"ccid", u"value": u"d863e681bde46657136c13f1c4c1bd65",
          u"domain": u".toutiao.com"}
    c3 = {u"name": u"ckmts", u"value": u"PUUrOYsQ,qrUrOYsQ,L64rOYsQ",
          u"domain": u".toutiao.com"}
    c4 = {u"name": u"sid_tt", u"value": u"7a4eaf65acc29cb04b6cdebcab76aaab",
          u"domain": u".toutiao.com"}

    driver.add_cookie(c1)
    driver.add_cookie(c2)
    driver.add_cookie(c3)
    driver.add_cookie(c4)