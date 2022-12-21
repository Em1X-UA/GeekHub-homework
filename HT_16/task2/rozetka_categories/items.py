# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RozetkaCategoriesItem(scrapy.Item):
    item_id = scrapy.Field()
    title = scrapy.Field()
    old_price = scrapy.Field()
    current_price = scrapy.Field()
    href = scrapy.Field()
    brand = scrapy.Field()
    category = scrapy.Field()
