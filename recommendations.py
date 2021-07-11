from selenium import webdriver

class recom():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')

    def recom_info(self):
        self.driver.get(url='https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm')
        select1 = self.driver.find_element_by_xpath('//*[@id="lister-sort-by-options"]/option[2]')
        select1.click()

bot = recom()
bot.recom_info()