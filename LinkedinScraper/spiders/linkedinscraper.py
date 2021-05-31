# import scrapy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from scrapy.selector import Selector
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
username.send_keys("jayparekh0408@gmail.com")
time.sleep(0.5)

password = wb.find_element_by_xpath('//input[@id = "password"]')
password.send_keys("Jayparelh@01")
time.sleep(0.5)

wb.find_element_by_xpath('//button[@type = "submit"]').click()
time.sleep(5)

wb.get('https://www.google.com/')
time.sleep(3)

search_input = wb.find_element_by_xpath('//input[@type = "text"]')
search_input.send_keys('site:linkedin.com/in/ AND "python developer" AND "india"')
time.sleep(0.5)

search_input.send_keys(Keys.RETURN)
time.sleep(2)

sele = Selector(text=wb.page_source)
profiles = sele.xpath('//div/a[contains(@href, "https://in.linkedin.com")]/@href').getall()

for profile in profiles :
    wb.get(profile)
    time.sleep(4)
    sele = Selector(text=wb.page_source)
    name = sele.xpath('//h1[contains(@class, "inline")]/text()').get().strip()
    job_disc = sele.xpath('//div[contains(@class, "break-words")]/text()').get().strip()
    loc = sele.xpath('//div[@class = "pb2"]/span[1]/text()').get().strip()
    linkedin_url = wb.current_url

    print({
        "name" : name,
        "job_disc" : job_disc,
        "loc" : loc,
        "linkedin_url" : linkedin_url
    })