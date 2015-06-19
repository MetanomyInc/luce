# -*- coding: utf-8 -*-

# Scrapy settings for rumours project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'rumours'

SPIDER_MODULES = ['rumours.spiders']
NEWSPIDER_MODULE = 'rumours.spiders'
DOWNLOAD_DELAY = 0.25
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'rumours (+http://www.yourdomain.com)'
