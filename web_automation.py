from selenium import webdriver

class music():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')

    def play(self, name):
        self.driver.get(url='https://youtube.com')


bot = music()
bot.play("See you again")