import requests
import pandas as pd
import urllib.parse as urp

#通过抓包软件可得电费查询的请求方式是post请求，返回的是json格式的数据

url = "http://10.100.1.24:8988/web/Common/Tsm.html"

#获取楼栋的buildingid
data={
"jsondata":	'{ "query_elec_building": { "aid": "0030000000002505", "account": "367686", "area": {"area": "青岛校区", "areaname": "青岛校区"  } } }',
"funname": "synjones.onecard.query.elec.building",
"json"	: "true"
}

data_r=urp.urlencode(data).encode("utf-8")

headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 12; 24031PN0DC Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36",
  'Accept': "application/json, text/javascript, */*; q=0.01",
  'Accept-Encoding': "gzip, deflate",
  'Pragma': "no-cache",
  'Cache-Control': "no-cache",
  'X-Requested-With': "XMLHttpRequest",
  'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
  'Origin': "http://10.100.1.24:8988",
  'Referer': "http://10.100.1.24:8988/web/common/checkEle.html?ticket=F53F9FCEDA0C41B8A376B86E254D0715&from=ehall&cometype=&timestamp=20241102114743325",
  'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
  'Cookie': "JSESSIONID=3A42D57348A58375187472682C8A5A99"
}
response = requests.post(url=url, data=data_r, headers=headers)
#得到装有所有楼栋id和名字的列表
id_list=response.json().get("query_elec_building").get('buildingtab')
#下载到表格中储存
building_data=[]
for i in id_list:
    building_name=i['building']
    building_id=i["buildingid"]
    building_data.append((building_name,building_id))
df = pd.DataFrame(building_data, columns=('楼栋', '楼栋id'))
df.to_excel('楼栋id.xlsx')









