import scrapy


class PeopleSpider(scrapy.Spider):
    name = "people"

    def start_requests(self):
        pageids = list(range(1, 3267))
        urls = []
        for x in pageids:
            url = 'https://creativemornings.com/people?active_only=true&faces_only=true&page=' + str(x)
            urls.append(url)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'people-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)