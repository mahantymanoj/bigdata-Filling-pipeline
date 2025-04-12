from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from coinmarket.coinmarketcap.spiders.cryptocurrency import CryptocurrencySpider

def run_scrapy():
    process = CrawlerProcess(get_project_settings())
    process.crawl(CryptocurrencySpider)
    process.start()

# if __name__ == "__main__":
#     run_scrapy()
