# tj_gov_time

使用scarpy做的天津交通数据实时爬虫

实时逻辑主要依靠mysql数据库设计，设置主键使数据插入无重复值，由于刷新频率不是很快，因此每隔1个小时再次爬取前10页即可
