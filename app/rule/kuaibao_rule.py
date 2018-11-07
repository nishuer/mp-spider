from app.extend import helper


def hasCheckTitle(self):
    TITLE_XPATH = '//*[@id="root"]/div/div/div[3]/div[2]/a[1]/div/div/div[1]'

    if (self.hasCheckDriverWait(TITLE_XPATH, type="XPATH")):
        title = self.driver.find_element_by_xpath(TITLE_XPATH)
        return (title.text if helper.titleRead(title.text, self.config['account']['category']) else False)


def openArticle(self):
    TITLE_XPATH = '//*[@id="root"]/div/div/div[3]/div[2]/a[1]'

    url = self.driver.find_element_by_xpath(TITLE_XPATH).get_attribute('href')
    self.openNewWindow(url)


def getTitle(self):
    TITLE_XPATH = '//*[@id="content"]/p'

    if (self.hasCheckDriverWait(TITLE_XPATH, type="XPATH") and self.hasCheckElementVisibility('//*[@id="con_wrap"]/div[4]', type="XPATH")):
        title = self.driver.find_element_by_xpath(TITLE_XPATH)
        return title.text

       
def hideOtherElement(self):
    driver = self.driver
    
    e1s = driver.find_elements_by_xpath("/html/body/div[position() > 2]")
    e2s = driver.find_elements_by_xpath('//*[@id="con_wrap"]/*[position() > 1]')
    e3s = driver.find_elements_by_xpath('//*[@id="con_wrap"]/div[1]/*[position() > 1]')
    e4s = driver.find_elements_by_xpath('//*[@id="content"]/*[position() < 3]')

    e1 = driver.find_element_by_xpath('//*[@id="top_downloader"]')
    e2 = driver.find_element_by_xpath('//*[@class="downloader-bar"]')

    for _ in e1s:
        driver.execute_script("arguments[0].setAttribute('style', 'display: none')", _)
    for _ in e2s:
        driver.execute_script("arguments[0].setAttribute('style', 'display: none')", _)
    for _ in e3s:
        driver.execute_script("arguments[0].setAttribute('style', 'display: none')", _)
    for _ in e4s:
        driver.execute_script("arguments[0].setAttribute('style', 'display: none')", _)

    driver.execute_script("arguments[0].setAttribute('style', 'display: none')", e1)
    driver.execute_script("arguments[0].setAttribute('style', 'display: none')", e2)
