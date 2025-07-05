import scrapy
from bs4 import BeautifulSoup
import requests

class GenderSpider(scrapy.Spider):
    name = "aclu"
    start_urls = [
        "https://www.aclu.org/news/by-issue/transgender-rights",
    ]

    # Get the links to the articles, pass them to parse_article 
    def parse(self, response):
        article_page_links = response.css("div.hp__article_list div div a::attr('href')")
        yield from response.follow_all(article_page_links, self.parse_article)

        # Go to the next page of results
        next_page = response.css('a.next::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    # get the text from the individual articles
    def parse_article(self, response):
        # Use BeautifulSoup to parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        text = soup.find("div", class_="wp-components").get_text().replace('\n', ' ')
        s = text.strip()
        s2 = s.replace('  ', ' ')
        s3 = s2.replace('   ', ' ')

        yield {
            'title': soup.find("title").get_text(strip=True),
            'author': soup.find("a", class_="hp__author_link").get_text(strip=True),
            'date': soup.find("span", class_="is-size-7").get_text(strip=True),
            'url': response.url,
            # check if summary exists, if not, insert "n/a"
            'summary': soup.find("div", class_="article-desc__fullbleed").get_text(strip=True) if soup.find("div", class_="article-desc__fullbleed") else "n/a",
            'text': s3
        }


        # Find the main content of the article
        # yield {
        #     'title': response.css("span.is-print-background::text").get().strip(),
        #     'author': response.css("a.hp__author_link::text").get().strip(),
        #     'date': response.css("span.is-size-7::text").get().strip(),
        #     'url': response.url,
        #     'summary':response.css("div.article-desc__fullbleed::text").get().strip(),
        #     'text': full_content
        # }
