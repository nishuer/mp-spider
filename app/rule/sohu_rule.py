from app.extend import helper


def hasCheckTitle(self):
    TITLE_CLASS_NAME = "wrap_title"

    if (self.hasCheckDriverWait(TITLE_CLASS_NAME)):
        title = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div/div[1]/a')

        return (title.text if helper.titleRead(title.text, self.config['account']['category']) else False)


def openArticle(self):
    url = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div/div[1]/a').get_attribute('href')
    self.openNewWindow(url)


def getTitle(self):
    TITLE_CLASS_NAME = 'text-title'

    if (self.hasCheckDriverWait(TITLE_CLASS_NAME)):
        title = self.driver.find_element_by_xpath('//*[@id="article-container"]/div[2]/div[1]/div[1]/h1')

        return title.text

       
def hideOtherElement(self):
    driver = self.driver
    
    e1s = driver.find_elements_by_xpath("/html/body/div[position() > 1]")
    e2s = driver.find_elements_by_xpath("/html/body/div[1]/*[position() < 3]")
    e3s = driver.find_elements_by_xpath("/html/body/div[1]/*[position() > 3]")
    e4s = driver.find_elements_by_xpath('//*[@id="article-container"]/div[1] | //*[@id="right-side-bar"]')
    e5s = driver.find_elements_by_xpath('//*[@id="article-container"]/div[2]/*[position() > 1]')
    e6s = driver.find_elements_by_xpath('//*[@id="article-container"]/div[2]/div[1]/*[position() > 2]')

    e1 = driver.find_element_by_xpath('//*[@id="article-container"]/div[2]/div[1]/div[1]')
    e2 = driver.find_element_by_xpath('//*[@id="backsohucom"]')

    for _ in e1s:
        driver.execute_script("arguments[0].setAttribute('style', 'display: none')", _)
    for _ in e2s:
        driver.execute_script("arguments[0].setAttribute('style', 'display: none')", _)
    for _ in e3s:
        driver.execute_script("arguments[0].setAttribute('style', 'display: none')", _)
    for _ in e4s:
        driver.execute_script("arguments[0].setAttribute('style', 'display: none')", _)
    for _ in e5s:
        driver.execute_script("arguments[0].setAttribute('style', 'display: none')", _)
    for _ in e6s:
        driver.execute_script("arguments[0].setAttribute('style', 'display: none')", _)

    driver.execute_script("arguments[0].setAttribute('style', 'display: none')", e1)
    driver.execute_script("arguments[0].setAttribute('style', 'display: none')", e2)
