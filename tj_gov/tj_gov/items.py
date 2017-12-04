# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

#重点车辆严重违法
class GavAccItem(scrapy.Item):
    """
    type:       公示类型
    code:       决定书编号
    accName:    案件名称
    peoName:    驾驶人名称
    carType:    号码种类
    carNumber:  号牌号码
    result:     处罚结果
    date:       处罚日期
    """
    type = Field()
    code = Field()
    accName = Field()
    peoName = Field()
    carType = Field()
    carNumber = Field()
    result = Field()
    date = Field()

#驾驶人考试作弊行为公示
class CheatItem(scrapy.Item):
    """
    type:   公示类型
    name:   名称
    peoName:被处罚人名称
    result:处理结果
    department: 处理部门
    date:   处理日期
    """
    type = Field()
    name = Field()
    peoName = Field()
    result = Field()
    department = Field()
    date = Field()


#满12分被降级公示
class RelegateItem(scrapy.Item):
    """
    type:   公示类型
    name:   名称
    peoName:被降级人名称
    result:处理结果
    department: 处理部门
    date:   处理日期
    """
    type = Field()
    name = Field()
    peoName = Field()
    result = Field()
    department = Field()
    date = Field()


#死亡事故负有责任人公示
class DeadAccItem(scrapy.Item):
    """
    type:       公示类型
    code:       事故认定书编号
    accName:    案件名称
    peoName:    驾驶人名称
    carType:    号码种类
    carNumber:  号牌号码
    department: 处理部门
    date:       认定日期
    """
    type = Field()
    code = Field()
    accName = Field()
    peoName = Field()
    carType = Field()
    carNumber = Field()
    department = Field()
    date = Field()