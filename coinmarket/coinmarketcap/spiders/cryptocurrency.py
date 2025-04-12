import json
import scrapy
from fake_useragent import UserAgent
from utility.user_agent_utils import get_custom_user_agent


class CryptocurrencySpider(scrapy.Spider):
    name = "cryptocurrency"
    custom_settings = {
        'DOWNLOAD_DELAY': 1,
        'CONCURRENT_REQUESTS': 4,
        'USER_AGENT': get_custom_user_agent(),
        'ROBOTSTXT_OBEY': False,
        # 'LOG_LEVEL': 'INFO',
        # 'FEED_URI': 'output/crypto.json',
        # 'FEED_FORMAT': 'json'
    }
    def __init__(self):
        self.url = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=1000&sortBy=market_cap&sortType=desc&convert=USD,BTC,ETH&cryptoType=all&tagType=all&audited=false&aux=ath,atl,high24h,low24h,num_market_pairs,cmc_rank,date_added,max_supply,circulating_supply,total_supply,volume_7d,volume_30d,self_reported_circulating_supply,self_reported_market_cap"
        self.user_agent = get_custom_user_agent()
        self.headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7,mr;q=0.6',
            'origin': 'https://coinmarketcap.com',
            'platform': 'web',
            'referer': 'https://coinmarketcap.com/',
            'user-agent': self.user_agent
            }
   
    def start_requests(self):
        yield scrapy.Request(url=self.url, headers=self.headers,callback=self.get_cryto_currency_list)

    def get_cryto_currency_list(self, response):
        if response.status == 200:
            try:
                data = json.loads(response.text)  # parse JSON
                yield data
            except json.JSONDecodeError:
                self.logger.error("Failed to decode JSON")
                yield {}
        else:
            self.logger.warning(f"Non-200 response: {response.status}")
            yield {}


