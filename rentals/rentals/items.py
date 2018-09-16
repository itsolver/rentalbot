# -*- coding: utf-8 -*-

# The model for the RentalProperty scraped item

import scrapy


class RentalProperty(scrapy.Item):
    property_num    	= scrapy.Field()
    rent_amount 	    = scrapy.Field()
    bond_amount		    = scrapy.Field()
    street_address	    = scrapy.Field()
    suburb			    = scrapy.Field()
    postcode 		    = scrapy.Field()
    num_bedrooms 	    = scrapy.Field()
    num_bathrooms 	    = scrapy.Field()
    num_carport_spaces	= scrapy.Field()
    num_garage_spaces	= scrapy.Field()
    property_type 	    = scrapy.Field()
    url 			    = scrapy.Field()
    description		    = scrapy.Field()
    date_available	    = scrapy.Field()
    has_pool            = scrapy.Field()
    building_size       = scrapy.Field()
    land_size           = scrapy.Field()
    indoor_features     = scrapy.Field()
    outdoor_features    = scrapy.Field()
    other_features      = scrapy.Field()
    allowances          = scrapy.Field()
    floorplan_tour      = scrapy.Field()
    has_nbn			    = scrapy.Field()
    nbn_type            = scrapy.Field()