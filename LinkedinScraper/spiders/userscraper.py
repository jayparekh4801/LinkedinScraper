import scrapy


class UserScraper(scrapy.Spider) :
    name = "userscraper"
    allowed_domains = ["linkedin.com"]

    def __init__(self, name=None, user_url = "https://www.linkedin.com/in/jay-parekh-a2a5b81a4/"):
        self.start_urls = [user_url]
    
    