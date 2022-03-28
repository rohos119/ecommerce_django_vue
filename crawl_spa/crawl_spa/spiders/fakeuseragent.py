import scrapy


class FakeuseragentSpider(scrapy.Spider):
    name = 'fakeuseragent'
    start_urls = ["http://quotes.toscrape.com/"]
    custom_settings = dict(
        DOWNLOADER_MIDDLEWARES={
            "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
            "scrapy.downloadermiddlewares.retry.RetryMiddleware": None,
            "scrapy_fake_useragent.middleware.RandomUserAgentMiddleware": 400,
            "scrapy_fake_useragent.middleware.RetryUserAgentMiddleware": 401,
        },
        FAKEUSERAGENT_PROVIDERS=[
            "scrapy_fake_useragent.providers.FakerProvider",
            "scrapy_fake_useragent.providers.FakeUserAgentProvider",
            "scrapy_fake_useragent.providers.FixedUserAgentProvider",
        ],
    )

    def parse(self, response):
        # Print out the user-agent of the request to check they are random
        print(response.request.headers.get("User-Agent").decode())

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
