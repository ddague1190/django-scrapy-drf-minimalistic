import scrapy

class BikezSpider(scrapy.Spider):
    name = 'bikez'
    allowed_domains = ['bikez.com/models']
    mfgs_of_interest = [
        'bmw', 
        'kawasaki',
        'honda', 
        'ktm',
        'yamaha',
        'moto_guzzi',
        'suzuki',
        'triumph',
        'ducati',
        'harley-davidson',
        'aprilia',
        'beta',
        'husqvarna',
        'ural',
        'indian'
    ]
    def start_requests(self):
        for mfg in self.mfgs_of_interest:
            url = f"https://bikez.com/models/{mfg}_models.php"
            yield scrapy.Request(url=url, callback=self.parse, meta={'mfg': mfg}) 

    def parse(self, response):
        mfg = response.meta['mfg']
        for row in response.xpath("//tr[@class='even']"):
            yield {
                'mfg': mfg,
                'model': row.xpath("td[2]/a/text()").get(),
                'years_made':row.xpath("td[4]/text()").get(),
                }
