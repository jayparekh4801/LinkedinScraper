import scrapy
from selenium import webdriver 
import time
from scrapy.selector import Selector
class UserScraper(scrapy.Spider) :
    name = "userscraper"
    allowed_domains = ["linkedin.com"]

    def __init__(self, name=None, user_urls = "https://www.linkedin.com/in/jay-parekh-a2a5b81a4/"):
        self.start_urls = [user_urls]
    
    def start_requests(self):
        wb = webdriver.Chrome()

        wb.get('https://www.linkedin.com/')
        time.sleep(3)

        wb.find_element_by_xpath('//a[text() = "Sign in"]').click()
        time.sleep(3)

        username = wb.find_element_by_xpath('//input[@id = "username"]')
        username.send_keys("jayparekh0408@gmail.com")
        time.sleep(0.5)

        password = wb.find_element_by_xpath('//input[@id = "password"]')
        password.send_keys("vnhmhJi#7li")
        time.sleep(0.5)

        wb.find_element_by_xpath('//button[@type = "submit"]').click()
        time.sleep(5)

        wb.get("https://in.linkedin.com/in/mudit-aggarwal-549b44158")
        time.sleep(1000)

        # yield scrapy.Request(url=self.start_urls[0], callback=self.parse)


    def parse(self, response) :
        print(response.body)