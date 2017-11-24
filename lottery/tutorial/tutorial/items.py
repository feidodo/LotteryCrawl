# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class LotteryItem(scrapy.Item):
    Itype = scrapy.Field()
    Id = scrapy.Field()
    num_prefix = scrapy.Field()
    num_postfix = scrapy.Field()
    sales = scrapy.Field()
    pool = scrapy.Field()
    date = scrapy.Field()
    detail_link = scrapy.Field()

class DetailItem(scrapy.Item):
    #类型
    Itype = scrapy.Field()
    #期数
    Id = scrapy.Field()
    #使用的第几套球
    ball = scrapy.Field()
    #一等奖
    win1_base_num = scrapy.Field()
    win1_base_bonus = scrapy.Field()
    win1_base_bonus_sum = scrapy.Field()
    win1_add_num = scrapy.Field()
    win1_add_bonus = scrapy.Field()
    win1_add_bonus_sum = scrapy.Field()
    #二等奖
    win2_base_num = scrapy.Field()
    win2_base_bonus = scrapy.Field()
    win2_base_bonus_sum = scrapy.Field()
    win2_add_num = scrapy.Field()
    win2_add_bonus = scrapy.Field()
    win2_add_bonus_sum = scrapy.Field()
    #三等奖
    win3_base_num = scrapy.Field()
    win3_base_bonus = scrapy.Field()
    win3_base_bonus_sum = scrapy.Field()
    win3_add_num = scrapy.Field()
    win3_add_bonus = scrapy.Field()
    win3_add_bonus_sum = scrapy.Field()
    #四等奖
    win4_base_num = scrapy.Field()
    win4_base_bonus = scrapy.Field()
    win4_base_bonus_sum = scrapy.Field()
    win4_add_num = scrapy.Field()
    win4_add_bonus = scrapy.Field()
    win4_add_bonus_sum = scrapy.Field()
    #五等奖
    win5_base_num = scrapy.Field()
    win5_base_bonus = scrapy.Field()
    win5_base_bonus_sum = scrapy.Field()
    win5_add_num = scrapy.Field()
    win5_add_bonus = scrapy.Field()
    win5_add_bonus_sum = scrapy.Field()
    #六等奖
    win6_base_num = scrapy.Field()
    win6_base_bonus = scrapy.Field()
    win6_base_bonus_sum = scrapy.Field()
    #合计
    bonus_total = scrapy.Field()
    #一等奖出处
    win1_comefrom = scrapy.Field()
    #兑奖截至日期
    deadline = scrapy.Field()
