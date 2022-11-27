from urllib import request
from urllib import parse
import gzip
import json

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

payload = {"callback": "datatable6013649",
        "columns": "REPORT_DATE,TIME,NATIONAL_SAME,NATIONAL_BASE,NATIONAL_SEQUENTIAL,NATIONAL_ACCUMULATE,CITY_SAME,CITY_BASE,CITY_SEQUENTIAL,CITY_ACCUMULATE,RURAL_SAME,RURAL_BASE,RURAL_SEQUENTIAL,RURAL_ACCUMULATE",
        "pageNumber": 3,
        "pageSize": 20,
        "sortColumns": "REPORT_DATE",
        "sortTypes": -1,
        "source": "WEB",
        "client": "WEB",
        "reportName": "RPT_ECONOMY_CPI",
        "p": 3,
        "pageNo": 3,
        "pageNum": 3,
        "_": 1669524330497}

url = r'https://datacenter-web.eastmoney.com/api/data/v1/get?'
data = parse.urlencode(payload)



userRequest = request.Request(url=url + data, headers=headers, method='GET')

response = request.urlopen(userRequest)
gzip.decompress(response.read()).decode('utf-8')
