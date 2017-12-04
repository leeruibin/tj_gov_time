# -*- coding: utf-8 -*-
import scrapy
from ..items import GavAccItem,CheatItem,RelegateItem,DeadAccItem
from time import time
from time import sleep
from scrapy.http import Request, FormRequest
from scrapy.http import TextResponse
import json
class AccidentSpider(scrapy.Spider):

    name = 'accident'
    allowed_domains = ['tj.122.gov.cn']
    start_urls = ['http://tj.122.gov.cn/']

    def __init__(self):
        self.headers = {
            'Referer':'http://tj.122.gov.cn/views/mfjjpub.html',
            'Origin':'http://tj.122.gov.cn',
            'Proxy-Connection':'keep-alive',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest',
            'Host':'tj.122.gov.cn',
            'Cookie': 'qt=470163; accessToken=/MaeFAuQh0BS5kSE3QpmlkjFamiJx/scf1YndJpXAQ7VtH/79hJQNcvtP4rdn5zq7W7VK5iRGmXdgWh9uLoCYLDCt8QzUWHekA0wPcsTziZb+uQWJw7wWJo1YqonkhRNvC5W+piyF22gQWDrkmQUlu0nowKY611iHOSqytPpUcP8L7fw8RIJ6BxZWubrz9ac; JSESSIONID-L=a7f3dd13-8ef5-4297-baa8-296e1f12771b; tmri_csfr_token=A9A605979F926F441F695BF9EE630987'
        }



    def start_requests(self):

        while 1:
            start = time()
            #  重点车辆严重违法行为公示  部分
            i = 1
            while 1:
                if i==11:
                    break
                yield FormRequest(
                    url='http://tj.122.gov.cn/m/viopub/getVioPubList',
                    method='POST',
                    headers=self.headers,
                    dont_filter=True,
                    meta={'type': 1},
                    formdata={
                        'page': str(i),
                        'size': '20',
                        'startTime': '',
                        'endTime': '',
                        'gsyw': '01'
                    },
                    callback=self.parseJson
                )
                i = i + 1
            #  驾驶人考试作弊行为公示 部分

            #  满12分被降级驾驶人公示 部分
            i = 1
            while 1:
                    if i==11:
                        break
                    yield FormRequest(
                        url='http://tj.122.gov.cn/m/viopub/getVioPubList',
                        method='POST',
                        headers=self.headers,
                        dont_filter=True,
                        meta={'type': 3},
                        formdata={
                            'page': str(i),
                            'size': '20',
                            'startTime': '',
                            'endTime': '',
                            'gsyw': '03'
                        },
                        callback=self.parseJson
                    )
                    i = i + 1

            #死亡事故负有责任驾驶人公示   部分
            i = 1
            while 1:
                if i==11:
                    break
                yield FormRequest(
                    url='http://tj.122.gov.cn/m/viopub/getVioPubList',
                    method='POST',
                    headers=self.headers,
                    dont_filter=True,
                    meta={'type': 4},
                    formdata={
                        'page': str(i),
                        'size': '20',
                        'startTime': '',
                        'endTime': '',
                        'gsyw': '04'
                    },
                    callback=self.parseJson
                )
                i = i + 1

            while 1:
                stop = time()
                if stop-start > 5:
                    print('----------------------------------'+str(stop-start)+'\n')
                    break
            #程序休眠1个小时
            print("休息一下")
            sleep(3600)



    def parseJson(self,response):
        data = json.loads(response.body.decode("utf-8"))
        data = data['data']
        lists = data['list']
        lists = lists['content']
        type = response.meta['type']
        if type==1:
            for list in lists:
                if list['gslx']=='1':
                    type = '新增'
                else:
                    type = '撤销'
                code = list['gsjdsbh']
                accName = list['gsajmc']
                peoName = list['gsjsrxm']
                carType = list['gshpzl']
                carNumber = list['gshphm']
                result = list['gscfjg']
                date = list['gscfrq']

                yield GavAccItem(type=type,code=code,accName=accName,peoName=peoName,
                                 carType=carType,carNumber=carNumber,result=result,date=date)
        elif type == 2:
            pass
        elif type == 3:
            for list in lists:
                if list['gslx']=='1':
                    type = '新增'
                else:
                    type = '撤销'
                name = list['gsajmc']
                peoName = list['gsjsrxm']
                result = list['gscfjg']
                department = list['gscfbm']
                date = list['gscfrq']

                yield RelegateItem(type=type,name=name,peoName=peoName,
                                 department=department,result=result,date=date)

        elif type == 4:
            for list in lists:
                if list['gslx']=='1':
                    type = '新增'
                else:
                    type = '撤销'
                code = list['gsjdsbh']
                accName = list['gsajmc']
                peoName = list['gsjsrxm']
                carType = list['gshpzl']
                carNumber = list['gshphm']
                department = list['gscfbm']
                date = list['gscfrq']

                yield DeadAccItem(type=type,code=code,accName=accName,peoName=peoName,
                                 carType=carType,carNumber=carNumber,
                                 department=department,date=date)
        else:
            pass



