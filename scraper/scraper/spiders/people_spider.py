import scrapy
import json


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

         for person in response.css('article.person'):
            yield {
                'profilelink': person.css('a.person-link').extract(),
                'name': person.css('h1.person-name').extract()
            }

class ProfileSpider(scrapy.Spider):
    name = "profile"

    with open("people.json", 'r') as infile:
        contents = json.load(infile)

        start_urls = []
        for item in contents:
            profile = str(item['profilelink'])
            profile = "https://creativemornings.com" + profile.partition("href=")[2].partition(">View")[0].strip('\"')
            start_urls.append(profile)


    def parse(self, response):

        for profile in response.css('div.ariaMain'):

            yield {
            'name': profile.css('a.user-name-inner::text').extract(),
            'city': profile.css('div.chapter-box::text').extract_first(),
            'picture': profile.css('img.avatar-bg::attr(src)').extract(),
            'desc': profile.css('div.user-details::text').extract(),
            'links': profile.css('div.has-sites a::attr(href)').extract(),
            'social': profile.css('a.social-link::attr(href)').extract(), # unsure if grabs 1 
            'bio': profile.css('div.user-bio').extract(),
            'watchlater': profile.css('a.profile-stat>strong::text').extract()[0],
            'attended': profile.css('a.profile-stat>strong::text').extract()[1],
            'skills': profile.css('div.user-skill-bubbles a::text').extract(),
            'uploads': profile.css('article.gallery-item::attr(data-item)').extract(),
            'questions': profile.css('article.user-answer label.cm-label::text').extract(),
            'answers': profile.css('article.user-answer div.answer-text>p').extract(),
            'qa': profile.css('article.user-answer').extract(),
            'activity': profile.css('article.iso-item a.talk-text::attr(href)').extract()
            }