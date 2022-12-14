from urllib import request
from urllib import parse
import gzip
import time
import json
import re
import random
import pandas
import os

PATH = os.environ['USERPROFILE'] + '\\DESKTOP\\123.xlsx'

# 将返回的json解析为dict对象


def decodeJson(iput: str) -> list:
    patternStart = re.compile(
        '^datatable\d+\((?=\{)')  # 寻找开头的 datatable123456 字样
    patternEnd = re.compile('\);$')  # 寻找结尾的 )" 字样
    iput = re.sub(patternStart, '', iput)
    iput = re.sub(patternEnd, '', iput)
    iput2Dict = json.loads(iput)
    return iput2Dict['result']['data']


headers = {"Accept": "*/*",
           "Accept-Encoding": "gzip, deflate, br",
           "Accept-Language": "zh-CN,zh;q=0.9",
           "Cache-Control": "no-cache",
           "Connection": "keep-alive",
           "Cookie": "qgqp_b_id=2a3842a0ecaec686c2c407500f625c6d; st_si=04881848722754; st_asi=delete; st_pvi=49278017551794; st_sp=2022-11-24%2014%3A55%3A43; st_inirUrl=http%3A%2F%2Fhao.199it.com%2F; st_sn=2; st_psi=20221127124530694-0-5172512268; JSESSIONID=740186ED9639A3CCCC31254971B621F5",
           "Host": "datacenter-web.eastmoney.com",
           "Pragma": "no-cache",
           "Referer": "https://data.eastmoney.com/",
           "sec-ch-ua": '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
           "sec-ch-ua-mobile": "?0",
           "sec-ch-ua-platform": "Windows",
           "Sec-Fetch-Dest": "script",
           "Sec-Fetch-Mode": "no-cors",
           "Sec-Fetch-Site": "same-site",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

payload = {"callback": "",  # JS源码:rnd = 'datatable' + Math.floor(Math.random() * 10000000 + 1);
           "columns": "REPORT_DATE,TIME,NATIONAL_SAME,NATIONAL_BASE,NATIONAL_SEQUENTIAL,NATIONAL_ACCUMULATE,CITY_SAME,CITY_BASE,CITY_SEQUENTIAL,CITY_ACCUMULATE,RURAL_SAME,RURAL_BASE,RURAL_SEQUENTIAL,RURAL_ACCUMULATE",
           "pageNumber": 0,
           "pageSize": 20,
           "sortColumns": "REPORT_DATE",
           "sortTypes": -1,
           "source": "WEB",
           "client": "WEB",
           "reportName": "RPT_ECONOMY_CPI",
           "p": 0,
           "pageNo": 0,
           "pageNum": 0,
           "_": 1669524330497}

url = r'https://datacenter-web.eastmoney.com/api/data/v1/get?'

result = []
for i in range(1, 10):
    payload['pageNumber'], payload['p'], payload['pageNo'], payload['pageNum'], payload['_'], payload['callback'] = i, i, i, i, int(
        time.time()), 'datatable' + str(random.randint(1000000, 9999999))
    data = parse.urlencode(payload)
    userRequest = request.Request(
        url=url + data, headers=headers, method='GET')

    response = request.urlopen(userRequest)
    responseDataList = decodeJson(
        gzip.decompress(response.read()).decode('utf-8'))
    for j in responseDataList:
        result.append(j)

pdList = []
index = 1
for i in result:
    pdList.append(pandas.DataFrame(i, index=[index]))
    index += 1
pandas.concat(pdList).to_excel(PATH)
