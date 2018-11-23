from app.extend import helper


def hasCheckTitle(self):
    TITLE_XPATH = '//*[@id="header"]/h1'

    if (self.hasCheckDriverWait(TITLE_XPATH, type="XPATH")):
        title = self.driver.find_element_by_xpath(TITLE_XPATH)
        return (title.text if helper.titleRead(title.text, self.config['account']['category']) else False)

       
def hideOtherElement(self):
    driver = self.driver
    
    e1s = driver.find_elements_by_xpath("//*[@id='wrapper'][position() > 2]")
    e1 = driver.find_element_by_xpath('//*[@id="header"]')

    for _ in e1s:
        driver.execute_script("arguments[0].setAttribute('style', 'display: none')", _)

    driver.execute_script("arguments[0].setAttribute('style', 'display: none')", e1)