# import scrapy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# class LinkedinscraperSpider(scrapy.Spider):
#     name = 'linkedinscraper'
#     allowed_domains = ['linkedin.com/']
#     start_urls = ['http://linkedin.com//']

#     def parse(self, response):
#         pass

wb = webdriver.Chrome()

wb.get('https://www.linkedin.com/')
time.sleep(3)

wb.find_element_by_xpath('//a[text() = "Sign in"]').click()
time.sleep(3)

username = wb.find_element_by_xpath('//input[@id = "username"]')
username.send_keys("example@gmail.com")
time.sleep(0.5)

password = wb.find_element_by_xpath('//input[@id = "password"]')
password.send_keys("xxxxxxxxx")
time.sleep(0.5)

wb.find_element_by_xpath('//button[@type = "submit"]').click()
time.sleep(5)

wb.get('https://www.google.com/')
time.sleep(3)

search_input = wb.find_element_by_xpath('//input[@type = "text"]')
search_input.send_keys('site:linkedin.com/in/ AND "python developer" AND "india"')
search_input.send_keys(Keys.RETURN)
# wb.find_elements_by_xpath('//input[@name = "btnK"]')[1].click()