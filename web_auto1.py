from selenium import webdriver

class movie():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')

    def movie_review(self, name):
        self.driver.get(url='https://www.google.com')
        search = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        search.click()
        search.send_keys(name + " movie")
        submit = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/center/input[1]')
        submit.click()

#bot = movie()
#bot.movie_review("Black")