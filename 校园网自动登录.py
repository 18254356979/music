import requests
import json
url = "http://10.224.2.3:8182/"
data = {
"is_auto_land": "false",
"usernameHidden": "190507060208",
"username_tip": "Username",
"username": "190507060208",
"strTypeAu": "", 
"uuidQrCode": "",
"authorMode": "",
"pwd_tip": "Password",
"pwd": "270031",
"net_access_type": "(unable to decode value)"
}
header = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9",
"Cache-Control": "max-age=0",
"Connection": "keep-alive",
"Content-Length": "188",
"Content-Type": "application/x-www-form-urlencoded",
"Cookie": "EPORTAL_USER_GROUP=2019%u7EA7%u5B66%u751F; EPORTAL_COOKIE_USERNAME=; EPORTAL_COOKIE_PASSWORD=; EPORTAL_AUTO_LAND=false; JSESSIONID=E37147C6FEB30EDECDE51EF3A2300AE3",
"Host": "10.224.2.3:8182",
"Origin": "http://10.224.2.3:8182",
"Referer": "http://10.224.2.3:8182/eportal/index.jsp?wlanuserip=35b8fdf7878011ed17ba92f7bee2a280&wlanacname=05a109411fa0f18293711ea750ead47f&ssid=&nasip=6d6c917f8c030bfb4f7db845faa6c560&snmpagentip=&mac=f01871947eca8af6cc6010011447d3b4&t=wireless-v2&url=14567fcb0da04819e325d01784247b4d3e6b0a75c15aa8f82a91f77de273f7dc&apmac=&nasid=05a109411fa0f18293711ea750ead47f&vid=446bb8b09fe1e926&port=3d4f21af9b2ba77b&nasportid=968d1cccc7437664e09f278ad1f631fe01a522a5b350d66e893dca105e79ccc0",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"

}
response = requests.post(url, data = json.dumps(data), headers = header).status_code
print("回应代码{}".format(response))