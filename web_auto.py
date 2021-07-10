from selenium import webdriver
import pyttsx3 as p

class info():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://wikipedia.org/")
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')  #xpath of an element is found by doing inspect on it and copy>copy xpath
        search.click()
        search.send_keys(query)

        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        enter.click()

        info = self.driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/p[2]')
        readable_text = info.text
        engine = p.init()
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[1].id)
        engine.say(readable_text)
        engine.runAndWait()

#bot = info()
#bot.get_info("Narendra Modi")


