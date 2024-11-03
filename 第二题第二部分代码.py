import requests
import urllib.parse as urp
import re
from appium import webdriver
from appium.options.android import UiAutomator2Options
import time



url = "http://10.100.1.24:8988/web/Common/Tsm.html"
#获取用户请求
in_building=input("请输入你所在的楼栋：")
in_buildingid=(input("请输入楼栋id："))
in_room=(input("请输入房间号："))
in_num=int(input("请输入你期望的提醒的频率(*小时/次)："))
in_count=int(input("请输入你期望的提醒的次数："))
num=in_num*3600
#制作请求所需的参数
in_jsondata={ "query_elec_roominfo": { "aid":"0030000000002505", "account": "367686","room": { "roomid": f'{in_room}', "room": f"{in_room}" },  "floor": { "floorid": "", "floor": "" }, "area": { "area": "青岛校区", "areaname": "青岛校区" }, "building": { "buildingid": f"{in_buildingid}", "building": f"{in_building}" } } }

data={
"jsondata":	 re.sub(r"'",'''"''',str(in_jsondata)),
"funname": "synjones.onecard.query.elec.roominfo",
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
elec=response.json().get("query_elec_roominfo").get("errmsg")

a=0
while a<=in_count:
  # 创建模拟器
  server = "http://localhost:4723/wd/hub"
  options = UiAutomator2Options().load_capabilities({
    "platformName": "Android",
    "platVersion": "7.1.2",
    "deviceName": "SM-G977N",
    "appPackage": "com.tencent.androidqqmail",
    "appActivity": "com.tencent.qqmail.WelcomePagesActivity"
  })
  driver = webdriver.Remote(server, options=options)

  # 自动登录qq邮箱并发送电量提醒脚本
  one = driver.find_element("id", "com.tencent.androidqqmail:id/bb5")
  one.click()
  time.sleep(2)
  two = driver.find_element("id", "com.tencent.androidqqmail:id/hz")
  two.click()
  time.sleep(2)
  three = driver.find_element("id", "com.tencent.androidqqmail:id/aqa")
  three.click()
  time.sleep(2)
  four = driver.find_element("id", "com.tencent.androidqqmail:id/b3m")
  four.click()
  time.sleep(2)
  five = driver.find_element("id", "com.android.packageinstaller:id/permission_allow_button")
  five.click()
  time.sleep(2)
  five.click()
  time.sleep(3)
  six = driver.find_element("xpath", '''//android.widget.ImageView[@content-desc="QQ邮箱"]''')
  six.click()
  time.sleep(3)
  seven = driver.find_element("id", "com.tencent.androidqqmail:id/a45")
  seven.click()
  time.sleep(3)
  nine = driver.find_element("id", "com.tencent.mobileqq:id/fds")
  nine.click()
  time.sleep(3)
  ten = driver.find_element("id", "com.tencent.androidqqmail:id/bd4")
  ten.click()
  time.sleep(3)
  elev = driver.find_element("accessibility id", "通讯录")
  elev.click()
  time.sleep(3)
  twel = driver.find_element("xpath",'''(//android.widget.RelativeLayout[@resource-id="com.tencent.androidqqmail:id/wx"])[3]/android.widget.LinearLayout''')
  twel.click()
  time.sleep(3)
  thir = driver.find_element("xpath", '''//android.widget.Button[@text="写邮件"]''')
  thir.click()
  time.sleep(3)
  tthir = driver.find_element("xpath", "//android.webkit.WebView")
  tthir.click()
  time.sleep(3)
  fou = driver.find_element("xpath", '''//android.widget.EditText[@resource-id="QMUIEditor"]''')
  fou.send_keys(f"您的{elec}")
  time.sleep(3)
  fif = driver.find_element("id", "com.tencent.androidqqmail:id/af5")
  fif.click()
  time.sleep(3)
  sixt = driver.find_element("xpath", '''//android.widget.Button[@text="继续发送"]''')
  sixt.click()
  time.sleep(num)
