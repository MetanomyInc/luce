# -*- coding: utf-8 -*-

from scrapy import Item, Field

class RumoursItem(Item):
    title = Field()
    author = Field()
    views = Field()
    num_replies = Field()
    url = Field()
    replies = Field()

class RumoursPost(Item):
    username = Field()
    join_date = Field()
    location = Field()
    age = Field()
    posts = Field()
    datetime = Field()
    content = Field()