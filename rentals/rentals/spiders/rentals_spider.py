import scrapy

from rentals.items import RentalProperty
from scrapy.linkextractors import LinkExtractor


class RentalsSpider(scrapy.Spider):
    name = 'rentals'
    allowed_domains = ['www.realestate.com.au']
    start_urls = [''] # Insert your saved search URL
    
    """
    for each rental link
        get rental property url, save to item object
        follow rental property url, retrieve other properties, save to item object
    also follow pagination
    return list of items
    """

    def parse(self, response):
        for href in response.css("h2.rui-truncate > a::attr('href')"): # To do: fix issue where not every link is extracted
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_property_page)
        next_page = response.css(".nextLink > a::attr('href')")
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse) # recursive loop

    def parse_property_page(self, response):
        item = RentalProperty()
        item['url'] = response.url
        item['property_num']    = response.xpath('//span[@class="property_id"]/text()').re('Property No\. (\d+)')[0]
        item['rent_amount']     = response.xpath('//p[@class="priceText"]/text()')[0].extract()
        try:
            item['bond_amount']     = response.xpath('//div[@class="featureList"]/ul/li[contains(text(),"Bond")]/span/text()').extract()
        except:
            item['bond_amount'] = None
        try:
            item['street_address']  = response.xpath('//span[@itemprop="streetAddress"]/text()').extract()
        except: 
            item['street_address']  = None
        try:
            item['suburb']          = response.xpath('//span[@itemprop="addressLocality"]/text()').extract()
        except:
            item['suburb']          = None
        try:
            item['postcode']        = response.xpath('//span[@itemprop="postalCode"]/text()').extract()
        except:
            item['postcode']        = None
        try:
            item['num_bedrooms']    = response.xpath('//div[@class="featureList"]/ul/li[contains(text(),"Bedrooms")]/span/text()').extract()
        except:
            item['num_bedrooms']    = None
        try:
            item['num_bathrooms']   = response.xpath('//div[@class="featureList"]/ul/li[contains(text(),"Bathrooms")]/span/text()').extract()
        except:
            item['num_bathrooms']   = None
        try: 
            item['num_carport_spaces']   = response.xpath('//div[@class="featureList"]/ul/li[contains(text(),"Carport Spaces")]/span/text()').extract()
            if len(item['num_carport_spaces']) == 0: item['num_carport_spaces'] = '0'
        except: 
            item['num_carport_spaces'] = None
        try:
            item['num_garage_spaces']   = response.xpath('//div[@class="featureList"]/ul/li[contains(text(),"Garage Spaces")]/span/text()').extract()
            if len(item['num_garage_spaces']) == 0: item['num_garage_spaces'] = '0'
        except:
            item['num_garage_spaces'] = None
        try:
            item['property_type']   = response.xpath('//div[@class="featureList"]/ul/li[contains(text(),"Property Type")]/span/text()').extract()
        except:
            item['property_type']   = None
        try:
            item['description']     = "\n".join(response.xpath('//p[@class="body"]/text()').extract())
        except:
            item['description']     = None
        try:
            item['date_available']  = response.xpath('//div[@class="available_date"]/span/text()').extract()
        except:
            item['date_available']  = None
        try:
            item['has_pool']    = response.xpath('//div[@class="featureList"]/ul/li[contains(text(),"Pool")]/span/text()').extract()
        except:
            item['has_pool']    = None
        try:
            item['building_size']   = response.xpath('//div[@class="featureList"]/ul/li[contains(text(),"Building Size")]/span/text()').extract()
        except:
            item['building_size']   = None
        try:
            item['land_size']   = response.xpath('//div[@class="featureList"]/ul/li[contains(text(),"Land Size")]/span/text()').extract()
        except:
            item['land_size']   = None
        try:
            item['indoor_features'] = response.xpath('string(//li[@class="header" and contains(text(),"Indoor Features")]/parent::ul)').extract()
        except:
            item['indoor_features'] = None
        try:
            item['outdoor_features'] = response.xpath('string(//li[@class="header" and contains(text(),"Outdoor Features")]/parent::ul)').extract()
        except:
            item['outdoor_features'] = None
        try:
            item['other_features'] = response.xpath('string(//li[@class="header" and contains(text(),"Other Features")]/parent::ul)').extract()
        except:
            item['other_features'] = None
        try:
            item['allowances'] = response.xpath('string(//li[@class="header" and contains(text(),"Allowances")]/parent::ul)').extract()
        except:
            item['allowances'] = None
        try:
            item['floorplan_tour'] = response.xpath('//li[@class="floorplan"]/@href').extract()
        except:
            item['floorplan_tour'] = None
        yield item