from selenium import webdriver

class music():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')

    def play(self, name):
        self.driver.get(url='https://youtube.com/results?search_query='+name)
        video= self.driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
        video.click()

#bot = music()
#bot.play("Don't let me down")