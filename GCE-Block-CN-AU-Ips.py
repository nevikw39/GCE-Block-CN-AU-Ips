from bs4 import BeautifulSoup
import requests
import os
header = {
'HOST': 'www.countryipblocks.net',
'Connection': 'keep-alive',
'Content-Length': '66',
'Cache-Control': 'max-age=0',
'Origin': 'https://www.countryipblocks.net',
'Upgrade-Insecure-Requests': '1',
'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Referer': 'https://www.countryipblocks.net/country_selection.php',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie': 'PHPSESSID=3b39ce9953453684b87c6b121d4ab936'
}
r=requests.post("https://www.countryipblocks.net/country_selection.php",headers=header,data="countries%5B%5D=CN&format1=1&get_acl=Create+ACL")
soup = BeautifulSoup(r.text,features="lxml")
elems = soup.select('#right_content > textarea')
ips = elems[0].text
for i, ip in enumerate(ips.splitlines()) :
	if len(ip)<1 or ip[0]=='#' :
		continue
	print("(" + str(i) + " / " + str(len(ips)) + ") gcloud compute firewall-rules create blockcnau"+str(i)+" --action DENY	--rules tcp,udp --direction OUT --destonation-ranges "+str(ip))
	os.system("gcloud compute firewall-rules create blockcnau"+str(i)+" --action DENY --rules tcp,udp --direction OUT --destination-ranges "+str(ip))
